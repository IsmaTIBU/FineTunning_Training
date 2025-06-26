# =============================================================================
# MODEL TESTING FOR LOCAL MACHINE - SAFE VERSION FOR OLD PYTORCH
# =============================================================================

import sys
import os
import json
from datetime import datetime
import warnings

# Setup path for local machine
sys.path.append('.')

# Import transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load test data
from DATA.test import test_data

print(f"📊 Test data loaded: {len(test_data)} examples")
print(f"🔍 PyTorch version: {torch.__version__}")

# Check PyTorch version
def check_pytorch_version():
    version = torch.__version__
    major, minor = map(int, version.split('.')[:2])
    
    if major > 2 or (major == 2 and minor >= 6):
        return True, "✅ PyTorch version is compatible"
    else:
        return False, f"⚠️ PyTorch {version} detected. Version 2.6+ recommended for security."

is_compatible, version_msg = check_pytorch_version()
print(version_msg)

# =============================================================================
# CONFIGURATION FOR LOCAL MACHINE
# =============================================================================
CONFIG = {
    'model_name': 'Salesforce/codet5-base',
    'model_path': './models/best_robotics_model.pth',
    'max_length': 256,
    'device': 'cuda' if torch.cuda.is_available() else 'cpu'
}

print(f"\n⚙️ Configuration:")
for key, value in CONFIG.items():
    print(f"   • {key}: {value}")

print(f"\n💻 Device detected: {CONFIG['device']}")

# =============================================================================
# SAFE MODEL LOADING WITH PYTORCH VERSION HANDLING
# =============================================================================
def safe_torch_load(file_path, map_location='cpu'):
    """Safe torch.load with fallback for older PyTorch versions"""
    
    try:
        # Try standard loading first
        return torch.load(file_path, map_location=map_location)
    except ValueError as e:
        if "torch.load" in str(e) and "weights_only" in str(e):
            print("⚠️ PyTorch version issue detected")
            print("🔄 Trying alternative loading method...")
            
            try:
                # Try with weights_only=False (less secure but works)
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    return torch.load(file_path, map_location=map_location, weights_only=False)
            except Exception as e2:
                print(f"❌ Alternative loading also failed: {e2}")
                raise e
        else:
            raise e

def load_model_safe(config):
    """Load model with safe handling for PyTorch version issues"""
    
    print(f"\n🤖 Loading model...")
    
    try:
        # Load tokenizer
        print("📝 Loading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(config['model_name'])
        print("✅ Tokenizer loaded successfully")
        
        # Load base model architecture
        print("🏗️ Loading base model architecture...")
        
        try:
            model = AutoModelForSeq2SeqLM.from_pretrained(config['model_name'])
            print("✅ Base model loaded successfully")
        except ValueError as e:
            if "torch.load" in str(e):
                print("❌ Cannot load base model due to PyTorch version")
                print("💡 Solution: pip install --upgrade torch>=2.6.0")
                return None, None, "PYTORCH_VERSION_ERROR"
            else:
                raise e
        
        # Try to load trained weights
        model_status = "BASE MODEL (FALLBACK)"
        
        if os.path.exists(config['model_path']):
            print(f"📂 Found trained model: {config['model_path']}")
            
            # Check file size
            file_size_mb = os.path.getsize(config['model_path']) / (1024*1024)
            print(f"📏 Model file size: {file_size_mb:.2f} MB")
            
            if file_size_mb < 10:
                print("⚠️ File too small, likely corrupted. Using base model.")
            else:
                try:
                    print("🔄 Loading trained weights...")
                    state_dict = safe_torch_load(config['model_path'], map_location=config['device'])
                    model.load_state_dict(state_dict)
                    model_status = "TRAINED MODEL"
                    print("✅ Trained weights loaded successfully!")
                    
                except Exception as e:
                    print(f"❌ Error loading trained weights: {e}")
                    print("🔄 Falling back to base model")
        else:
            print(f"⚠️ Trained model not found at: {config['model_path']}")
            print("🔄 Using base model instead")
        
        # Move to device
        print(f"📱 Moving model to {config['device']}...")
        model = model.to(config['device'])
        model.eval()
        
        print(f"✅ Model ready on {config['device']}")
        print(f"✅ Parameters: {model.num_parameters():,}")
        
        return tokenizer, model, model_status
        
    except Exception as e:
        print(f"❌ Critical error loading model: {e}")
        
        if "torch.load" in str(e):
            print("\n🔧 SOLUTION:")
            print("   Your PyTorch version is too old and has security vulnerabilities.")
            print("   Please update PyTorch:")
            print("   pip install --upgrade torch>=2.6.0 torchvision torchaudio")
            print("   Then run this script again.")
        
        return None, None, "ERROR"

# Load model
tokenizer, model, model_status = load_model_safe(CONFIG)

if model is None:
    print("\n❌ Cannot proceed without a working model.")
    print("🔧 Please update PyTorch and try again:")
    print("   pip install --upgrade torch>=2.6.0")
    print("\n🛑 Exiting...")
    exit(1)

# =============================================================================
# TESTING FUNCTION (SIMPLIFIED FOR COMPATIBILITY)
# =============================================================================
def test_model_performance_safe(model, test_data, tokenizer, device, config, model_name="Model"):
    """Simplified testing function with better error handling"""
    print(f"\n🔍 TESTING {model_name}")
    print("=" * 60)
    
    test_examples = [item['input'] for item in test_data]
    perfect = 0
    bad = 0
    total = 0
    detailed_results = []
    generation_errors = 0
    
    start_time = datetime.now()
    
    for i, test_input in enumerate(test_examples):
        print(f"\n--- Test {i+1}/{len(test_examples)} ---")
        print(f"INPUT: {test_input}")
        
        try:
            # Tokenize input
            inputs = tokenizer(
                test_input, 
                return_tensors="pt", 
                max_length=config['max_length'], 
                truncation=True,
                padding=True
            )
            inputs = {k: v.to(device) for k, v in inputs.items()}
            
            # Generate prediction with safer parameters
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_length=config['max_length'],
                    num_beams=2,  # Further reduced for stability
                    do_sample=False,
                    early_stopping=True,
                    pad_token_id=tokenizer.pad_token_id,
                    eos_token_id=tokenizer.eos_token_id
                )
            
            # Decode result
            result = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(f"OUTPUT: {result}")
            
        except Exception as e:
            print(f"❌ Generation error: {e}")
            result = '{"operacion": "error", "parametros": {}}'
            generation_errors += 1
        
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
        
        # Store results
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
            elapsed = datetime.now() - start_time
            avg_time = elapsed.total_seconds() / (i + 1)
            remaining = len(test_examples) - (i + 1)
            eta_minutes = (remaining * avg_time) / 60
            
            print(f"\n📊 Progress: {i+1}/{len(test_examples)} - Accuracy: {current_accuracy:.2f}%")
            print(f"⏱️ ETA: {eta_minutes:.1f} minutes - Errors: {generation_errors}")
    
    # Calculate metrics
    accuracy = (perfect / total) * 100 if total > 0 else 0
    valid_json_count = sum(1 for r in detailed_results if r['is_valid_json'])
    json_accuracy = (valid_json_count / total) * 100 if total > 0 else 0
    operation_correct_count = sum(1 for r in detailed_results if r['is_operation_correct'])
    operation_accuracy = (operation_correct_count / total) * 100 if total > 0 else 0
    
    total_time = datetime.now() - start_time
    
    print(f"\n📊 {model_name} Performance Summary:")
    print(f"   • Perfect cases: {perfect}/{total} ({accuracy:.2f}%)")
    print(f"   • Failed cases: {bad}/{total} ({(bad/total)*100:.2f}%)")
    print(f"   • Valid JSON: {valid_json_count}/{total} ({json_accuracy:.2f}%)")
    print(f"   • Correct operation: {operation_correct_count}/{total} ({operation_accuracy:.2f}%)")
    print(f"   • Generation errors: {generation_errors}")
    print(f"   ⏱️ Total time: {total_time.total_seconds():.1f} seconds")
    
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
        'generation_errors': generation_errors,
        'detailed_results': detailed_results,
        'total_time_seconds': total_time.total_seconds()
    }

# =============================================================================
# RUN TEST
# =============================================================================
print(f"\n🚀 Starting model testing...")
if CONFIG['device'] == 'cpu':
    print(f"💡 Running on CPU - this may take 10-20 minutes for 89 tests")

results = test_model_performance_safe(
    model, test_data, tokenizer, CONFIG['device'], CONFIG, model_status
)

# =============================================================================
# SAVE RESULTS AND SUMMARY
# =============================================================================
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
os.makedirs('./test_results', exist_ok=True)

# Quick summary
print(f"\n🎉 TESTING COMPLETED!")
print(f"📊 Final Results:")
print(f"   • Accuracy: {results['accuracy']:.2f}% ({results['perfect']}/{results['total']})")
print(f"   • Valid JSON: {results['json_accuracy']:.2f}%")
print(f"   • Correct Operations: {results['operation_accuracy']:.2f}%")
print(f"   • Generation Errors: {results['generation_errors']}")
print(f"   ⏱️ Total Time: {results['total_time_seconds']:.1f} seconds")

# Save basic report
basic_report = {
    'timestamp': timestamp,
    'pytorch_version': torch.__version__,
    'model_status': model_status,
    'device': CONFIG['device'],
    'results_summary': {
        'accuracy': results['accuracy'],
        'json_accuracy': results['json_accuracy'],
        'operation_accuracy': results['operation_accuracy'],
        'total_tests': results['total'],
        'generation_errors': results['generation_errors'],
        'total_time_seconds': results['total_time_seconds']
    }
}

report_file = f'./test_results/test_summary_{timestamp}.json'
with open(report_file, 'w', encoding='utf-8') as f:
    json.dump(basic_report, f, indent=2)

print(f"📄 Summary report saved: {report_file}")

# Show a few examples if there are failures
failures = [r for r in results['detailed_results'] if not r['is_perfect']]
if failures and len(failures) > 0:
    print(f"\n❌ First 3 failures:")
    for i, failure in enumerate(failures[:3]):
        print(f"   {i+1}. INPUT: {failure['input'][:60]}...")
        print(f"      PREDICTED: {failure['predicted'][:60]}...")

print(f"\n💡 Recommendation:")
if results['accuracy'] < 50:
    print("   • Model seems to be using base weights (low accuracy)")
    print("   • Try updating PyTorch and loading the trained model")
else:
    print("   • Model performance looks good!")

print(f"\n🔧 To improve performance:")
print(f"   1. Update PyTorch: pip install --upgrade torch>=2.6.0")
print(f"   2. Use GPU if available")
print(f"   3. Ensure trained model weights are loading correctly")

if CONFIG['device'] == 'cpu':
    print(f"✅ CPU testing completed successfully!")