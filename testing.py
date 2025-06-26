# =============================================================================
# MODEL TESTING ONLY - FOR ALREADY TRAINED MODELS
# =============================================================================

import sys
import os
import json
from datetime import datetime

# Setup path
sys.path.append('/content/PRUEBA')

# Import transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load test data
from DATA.test import test_data

print(f"📊 Test data loaded: {len(test_data)} examples")

# =============================================================================
# CONFIGURATION
# =============================================================================
CONFIG = {
    'model_name': 'Salesforce/codet5-base',  # Base model name
    'model_path': './models/robotics_codet5_final.pth',  # Path to your trained model
    'max_length': 256,
    'device': 'cuda' if torch.cuda.is_available() else 'cpu'
}

print(f"\n⚙️ Configuration:")
for key, value in CONFIG.items():
    print(f"   • {key}: {value}")

# =============================================================================
# LOAD MODEL AND TOKENIZER
# =============================================================================
print(f"\n🤖 Loading model...")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(CONFIG['model_name'])

# Load base model architecture
model = AutoModelForSeq2SeqLM.from_pretrained(CONFIG['model_name'])

# Load trained weights if they exist
if os.path.exists(CONFIG['model_path']):
    print(f"📂 Loading trained weights from: {CONFIG['model_path']}")
    model.load_state_dict(torch.load(CONFIG['model_path'], map_location=CONFIG['device']))
    model_status = "TRAINED MODEL"
else:
    print(f"⚠️ Trained model not found at {CONFIG['model_path']}")
    print(f"🔄 Using base model instead")
    model_status = "BASE MODEL (FALLBACK)"

model = model.to(CONFIG['device'])
model.eval()

print(f"✅ Model loaded on {CONFIG['device']}")
print(f"✅ Parameters: {model.num_parameters():,}")

# =============================================================================
# TESTING FUNCTION
# =============================================================================
def test_model_performance(model, test_data, tokenizer, device, config, model_name="Model"):
    """Test model and return detailed results"""
    print(f"\n🔍 TESTING {model_name}")
    print("=" * 60)
    
    test_examples = [item['input'] for item in test_data]
    perfect = 0
    bad = 0
    total = 0
    detailed_results = []
    
    for i, test_input in enumerate(test_examples):
        print(f"\n--- Test {i+1}/{len(test_examples)} ---")
        print(f"INPUT: {test_input}")
        
        # Tokenize input
        inputs = tokenizer(
            test_input, 
            return_tensors="pt", 
            max_length=config['max_length'], 
            truncation=True,
            padding=True
        )
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        # Generate prediction
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=config['max_length'],
                num_beams=5,
                temperature=0.1,
                do_sample=False,
                early_stopping=True
            )
        
        # Decode result
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"OUTPUT: {result}")
        
        # Validate JSON
        is_valid_json = False
        operation_detected = "N/A"
        try:
            parsed = json.loads(result)
            operation_detected = parsed.get('operacion', 'N/A')
            print(f"✅ Valid JSON - Operation: {operation_detected}")
            is_valid_json = True
        except Exception as e:
            print(f"❌ Invalid JSON - Error: {str(e)[:50]}...")
        
        # Expected output
        expected_output = test_data[i]['output']
        print(f"EXPECTED: {expected_output}")
        
        # Extract expected operation for comparison
        expected_operation = "N/A"
        try:
            expected_parsed = json.loads(expected_output)
            expected_operation = expected_parsed.get('operacion', 'N/A')
        except:
            pass
        
        # Exact comparison
        is_perfect = result.strip() == expected_output.strip()
        
        # Operation comparison (more lenient)
        is_operation_correct = operation_detected == expected_operation
        
        if is_perfect:
            print("✅ PERFECT PREDICTION")
            perfect += 1
        else:
            print("❌ DIFFERENCES FOUND")
            if is_operation_correct and is_valid_json:
                print("   ℹ️ Operation correct, but parameters differ")
            bad += 1
        
        total += 1
        
        # Store detailed results
        detailed_results.append({
            'test_id': i + 1,
            'input': test_input,
            'expected': expected_output,
            'predicted': result,
            'is_perfect': is_perfect,
            'is_valid_json': is_valid_json,
            'operation_detected': operation_detected,
            'expected_operation': expected_operation,
            'is_operation_correct': is_operation_correct
        })
        
        # Progress indicator
        if (i + 1) % 10 == 0:
            current_accuracy = (perfect / (i + 1)) * 100
            print(f"\n📊 Progress: {i+1}/{len(test_examples)} - Current accuracy: {current_accuracy:.2f}%")
    
    # Calculate final metrics
    accuracy = (perfect / total) * 100 if total > 0 else 0
    valid_json_count = sum(1 for r in detailed_results if r['is_valid_json'])
    json_accuracy = (valid_json_count / total) * 100 if total > 0 else 0
    operation_correct_count = sum(1 for r in detailed_results if r['is_operation_correct'])
    operation_accuracy = (operation_correct_count / total) * 100 if total > 0 else 0
    
    print(f"\n📊 {model_name} Performance Summary:")
    print(f"   • Perfect cases: {perfect}/{total} ({accuracy:.2f}%)")
    print(f"   • Failed cases: {bad}/{total} ({(bad/total)*100:.2f}%)")
    print(f"   • Valid JSON outputs: {valid_json_count}/{total} ({json_accuracy:.2f}%)")
    print(f"   • Correct operation: {operation_correct_count}/{total} ({operation_accuracy:.2f}%)")
    
    return {
        'model_name': model_name,
        'perfect': perfect,
        'bad': bad,
        'total': total,
        'accuracy': accuracy,
        'valid_json_count': valid_json_count,
        'json_accuracy': json_accuracy,
        'operation_correct_count': operation_correct_count,
        'operation_accuracy': operation_accuracy,
        'detailed_results': detailed_results
    }

# =============================================================================
# RUN TEST
# =============================================================================
results = test_model_performance(
    model, test_data, tokenizer, CONFIG['device'], CONFIG, model_status
)

# =============================================================================
# PERFORMANCE BY OPERATION TYPE
# =============================================================================
print(f"\n📈 PERFORMANCE BY OPERATION TYPE:")
print("-" * 50)

operation_stats = {}
for result in results['detailed_results']:
    expected_op = result['expected_operation']
    detected_op = result['operation_detected']
    
    if expected_op not in operation_stats:
        operation_stats[expected_op] = {
            'perfect': 0, 
            'total': 0, 
            'valid_json': 0,
            'correct_operation': 0
        }
    
    operation_stats[expected_op]['total'] += 1
    
    if result['is_perfect']:
        operation_stats[expected_op]['perfect'] += 1
    
    if result['is_valid_json']:
        operation_stats[expected_op]['valid_json'] += 1
    
    if result['is_operation_correct']:
        operation_stats[expected_op]['correct_operation'] += 1

for op, stats in sorted(operation_stats.items()):
    if stats['total'] > 0:
        perfect_pct = (stats['perfect'] / stats['total']) * 100
        json_pct = (stats['valid_json'] / stats['total']) * 100
        op_pct = (stats['correct_operation'] / stats['total']) * 100
        
        print(f"   • {op}:")
        print(f"     - Perfect: {stats['perfect']}/{stats['total']} ({perfect_pct:.1f}%)")
        print(f"     - Valid JSON: {stats['valid_json']}/{stats['total']} ({json_pct:.1f}%)")
        print(f"     - Correct Operation: {stats['correct_operation']}/{stats['total']} ({op_pct:.1f}%)")

# =============================================================================
# SAVE RESULTS
# =============================================================================
timestamp = datetime.now().strftime("%Y%m%d_%H%M")

# Create results directory
os.makedirs('./test_results', exist_ok=True)

# Save detailed report
test_report = {
    'timestamp': timestamp,
    'config': CONFIG,
    'model_status': model_status,
    'overall_results': {
        'accuracy': results['accuracy'],
        'json_accuracy': results['json_accuracy'],
        'operation_accuracy': results['operation_accuracy'],
        'total_tests': results['total']
    },
    'operation_performance': operation_stats,
    'detailed_results': results['detailed_results']
}

report_file = f'./test_results/test_report_{timestamp}.json'
with open(report_file, 'w') as f:
    json.dump(test_report, f, indent=2)

print(f"\n📄 Detailed test report saved as: {report_file}")

# =============================================================================
# SHOW SOME EXAMPLE FAILURES (IF ANY)
# =============================================================================
failures = [r for r in results['detailed_results'] if not r['is_perfect']]

if failures:
    print(f"\n❌ SHOWING FIRST 5 FAILURES:")
    print("-" * 50)
    
    for i, failure in enumerate(failures[:5]):
        print(f"\nFailure {i+1}:")
        print(f"   INPUT: {failure['input']}")
        print(f"   EXPECTED: {failure['expected']}")
        print(f"   PREDICTED: {failure['predicted']}")
        print(f"   ISSUES: ", end="")
        issues = []
        if not failure['is_valid_json']:
            issues.append("Invalid JSON")
        if not failure['is_operation_correct']:
            issues.append("Wrong operation")
        print(", ".join(issues) if issues else "Parameter differences")
else:
    print(f"\n🎉 NO FAILURES FOUND! Perfect model!")

# =============================================================================
# INTERACTIVE TESTING (OPTIONAL)
# =============================================================================
print(f"\n🎮 INTERACTIVE TESTING MODE")
print("Enter 'quit' to exit, or type a robotics command to test:")
print("-" * 50)

while True:
    try:
        user_input = input("\n>>> ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        
        if user_input.strip() == "":
            continue
            
        # Test the input
        inputs = tokenizer(
            user_input, 
            return_tensors="pt", 
            max_length=CONFIG['max_length'], 
            truncation=True
        )
        inputs = {k: v.to(CONFIG['device']) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=CONFIG['max_length'],
                num_beams=5,
                temperature=0.1,
                do_sample=False
            )
        
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        print(f"Model output: {result}")
        
        # Validate JSON
        try:
            parsed = json.loads(result)
            print(f"✅ Valid JSON - Operation: {parsed.get('operacion', 'N/A')}")
        except:
            print(f"❌ Invalid JSON")
            
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")

print(f"\n🎉 TESTING COMPLETED!")
print(f"📊 Final Results: {results['accuracy']:.2f}% accuracy ({results['perfect']}/{results['total']})")
print(f"💾 Report saved in ./test_results/")

# Clear GPU memory
torch.cuda.empty_cache()
print(f"🧹 GPU memory cleared")