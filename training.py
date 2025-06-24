# =============================================================================
# TRAINING WITH SPLIT DATA - COMPLETE VERSION WITH BASE vs TRAINED COMPARISON
# =============================================================================

import sys
import os
import json
from datetime import datetime

# Setup path
sys.path.append('/content/PRUEBA')

# Import transformers (CORRECTED)
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW  # ← From torch, not from transformers
import torch

# Load split data (created in setup.py)
from DATA.train import train_data
from DATA.val import val_data
from DATA.test import test_data

print(f"📊 Split data loaded:")
print(f"   • Train: {len(train_data)} examples")
print(f"   • Val: {len(val_data)} examples")
print(f"   • Test: {len(test_data)} examples")

# CONFIGURATION FOR A100 (THIS WAS MISSING)
CONFIG = {
    'model_name': 'Salesforce/codet5-base',      #'google-t5/t5-base'
    'batch_size': 6,        # Conservative for small dataset
    'learning_rate': 5e-5,
    'epochs': 25,
    'max_length': 256,
    'device': 'cuda'
}

print(f"\n⚙️ Configuration:")
for key, value in CONFIG.items():
    print(f"   • {key}: {value}")

# Load model
print(f"\n🤖 Loading {CONFIG['model_name']}...")
tokenizer = AutoTokenizer.from_pretrained(CONFIG['model_name'])
model = AutoModelForSeq2SeqLM.from_pretrained(CONFIG['model_name'])
model = model.to(CONFIG['device'])

print(f"✅ Model loaded on GPU")
print(f"✅ Parameters: {model.num_parameters():,}")

# Dataset class
class RoboticsDataset(Dataset):
    def __init__(self, data, tokenizer, max_length=256):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        item = self.data[idx]
        
        # Tokenize input
        input_encoding = self.tokenizer(
            item['input'],
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        
        # Tokenize target
        target_encoding = self.tokenizer(
            item['output'],
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        
        return {
            'input_ids': input_encoding['input_ids'].flatten(),
            'attention_mask': input_encoding['attention_mask'].flatten(),
            'labels': target_encoding['input_ids'].flatten()
        }

# Create datasets
train_dataset = RoboticsDataset(train_data, tokenizer, CONFIG['max_length'])
val_dataset = RoboticsDataset(val_data, tokenizer, CONFIG['max_length'])
test_dataset = RoboticsDataset(test_data, tokenizer, CONFIG['max_length'])

# Create dataloaders
train_loader = DataLoader(train_dataset, batch_size=CONFIG['batch_size'], shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=CONFIG['batch_size'], shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=CONFIG['batch_size'], shuffle=False)

# Optimizer
optimizer = AdamW(model.parameters(), lr=CONFIG['learning_rate'])

print("✅ Datasets and optimizer configured")

# =============================================================================
# FUNCTION TO TEST MODEL PERFORMANCE
# =============================================================================
def test_model_performance(model, test_data, tokenizer, device, config, model_name="Model"):
    """Test model and return detailed results"""
    model.eval()
    
    print(f"\n🔍 TESTING {model_name}")
    print("=" * 60)
    
    test_examples = [item['input'] for item in test_data]
    perfect = 0
    bad = 0
    total = 0
    detailed_results = []
    
    for i, test_input in enumerate(test_examples):
        print(f"\n--- Test {i+1} ---")
        print(f"INPUT: {test_input}")
        
        inputs = tokenizer(test_input, return_tensors="pt", max_length=config['max_length'], truncation=True)
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=config['max_length'],
                num_beams=5,
                temperature=0.1,
                do_sample=False
            )
        
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"OUTPUT: {result}")
        
        # Validate JSON
        is_valid_json = False
        try:
            parsed = json.loads(result)
            print(f"✅ Valid JSON - Operation: {parsed.get('operacion', 'N/A')}")
            is_valid_json = True
        except:
            print(f"❌ Invalid JSON")
        
        expected_output = test_data[i]['output']  # Expected output
        print(f"EXPECTED: {expected_output}")
        
        # Exact comparison
        is_perfect = result.strip() == expected_output.strip()
        if is_perfect:
            print("✅ PERFECT PREDICTION")
            perfect += 1
        else:
            print("❌ DIFFERENCES FOUND")
            bad += 1
        
        total += 1
        
        # Store detailed results
        detailed_results.append({
            'test_id': i + 1,
            'input': test_input,
            'expected': expected_output,
            'predicted': result,
            'is_perfect': is_perfect,
            'is_valid_json': is_valid_json
        })
    
    # Calculate metrics
    accuracy = (perfect / total) * 100 if total > 0 else 0
    valid_json_count = sum(1 for r in detailed_results if r['is_valid_json'])
    json_accuracy = (valid_json_count / total) * 100 if total > 0 else 0
    
    print(f"\n📊 {model_name} Performance Summary:")
    print(f"   • Perfect cases: {perfect}/{total} ({accuracy:.2f}%)")
    print(f"   • Failed cases: {bad}/{total} ({(bad/total)*100:.2f}%)")
    print(f"   • Valid JSON outputs: {valid_json_count}/{total} ({json_accuracy:.2f}%)")
    
    return {
        'model_name': model_name,
        'perfect': perfect,
        'bad': bad,
        'total': total,
        'accuracy': accuracy,
        'valid_json_count': valid_json_count,
        'json_accuracy': json_accuracy,
        'detailed_results': detailed_results
    }

# =============================================================================
# TEST BASE MODEL (BEFORE TRAINING) - COMMENTED OUT
# =============================================================================
# print("\n🔬 TESTING BASE MODEL (BEFORE TRAINING)")
# print("=" * 80)

# # Create a copy of the base model for testing
# base_model = AutoModelForSeq2SeqLM.from_pretrained(CONFIG['model_name'])
# base_model = base_model.to(CONFIG['device'])

# base_results = test_model_performance(
#     base_model, test_data, tokenizer, CONFIG['device'], CONFIG, "BASE MODEL"
# )

# # Clear memory
# del base_model
# torch.cuda.empty_cache()

# PLACEHOLDER for base_results when not testing base model
base_results = {
    'model_name': 'BASE MODEL (SKIPPED)',
    'perfect': 0,
    'bad': 0, 
    'total': 0,
    'accuracy': 0.0,
    'valid_json_count': 0,
    'json_accuracy': 0.0,
    'detailed_results': []
}

# =============================================================================
# TRAINING PHASE
# =============================================================================
print("\n🚀 STARTING FINE-TUNING ON A100")
print("=" * 60)

# Create directory for models
os.makedirs('./models', exist_ok=True)

# Training function
def train_epoch(model, dataloader, optimizer, device):
    model.train()
    total_loss = 0
    
    for batch_idx, batch in enumerate(dataloader):
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        
        # Forward pass
        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels
        )
        
        loss = outputs.loss
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        
        print(f"   Batch {batch_idx+1}/{len(dataloader)}, Loss: {loss.item():.4f}")
    
    return total_loss / len(dataloader)

# Validation function
def validate(model, dataloader, device):
    model.eval()
    total_loss = 0
    
    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)
            
            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels
            )
            
            total_loss += outputs.loss.item()
    
    return total_loss / len(dataloader)

# MAIN TRAINING LOOP
best_val_loss = float('inf')
training_history = []

for epoch in range(CONFIG['epochs']):
    print(f"\n📈 EPOCH {epoch + 1}/{CONFIG['epochs']}")
    print("-" * 40)
    
    # Train
    train_loss = train_epoch(model, train_loader, optimizer, CONFIG['device'])
    
    # Validate
    val_loss = validate(model, val_loader, CONFIG['device'])
    
    # Save best model
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        torch.save(model.state_dict(), './models/best_robotics_model.pth')
        print(f"   💾 Best model saved (val_loss: {val_loss:.4f})")
    
    # Log
    print(f"   📊 Train Loss: {train_loss:.4f}")
    print(f"   📊 Val Loss: {val_loss:.4f}")
    
    training_history.append({
        'epoch': epoch + 1,
        'train_loss': train_loss,
        'val_loss': val_loss
    })

# Final evaluation on test set
print(f"\n🧪 FINAL EVALUATION ON TEST SET")
test_loss = validate(model, test_loader, CONFIG['device'])
print(f"📊 Test Loss: {test_loss:.4f}")

# =============================================================================
# TEST TRAINED MODEL (AFTER TRAINING)
# =============================================================================
trained_results = test_model_performance(
    model, test_data, tokenizer, CONFIG['device'], CONFIG, "TRAINED MODEL"
)

# =============================================================================
# COMPARISON ANALYSIS
# =============================================================================
print("\n🔬 DETAILED COMPARISON: BASE vs TRAINED MODEL")
print("=" * 80)

print(f"\n📊 OVERALL PERFORMANCE COMPARISON:")
print(f"   BASE MODEL:")
print(f"      • Accuracy: {base_results['accuracy']:.2f}% ({base_results['perfect']}/{base_results['total']})")
print(f"      • Valid JSON: {base_results['json_accuracy']:.2f}% ({base_results['valid_json_count']}/{base_results['total']})")
print(f"   TRAINED MODEL:")
print(f"      • Accuracy: {trained_results['accuracy']:.2f}% ({trained_results['perfect']}/{trained_results['total']})")
print(f"      • Valid JSON: {trained_results['json_accuracy']:.2f}% ({trained_results['valid_json_count']}/{trained_results['total']})")

# Calculate improvement
accuracy_improvement = trained_results['accuracy'] - base_results['accuracy']
json_improvement = trained_results['json_accuracy'] - base_results['json_accuracy']

print(f"\n📈 IMPROVEMENT:")
print(f"   • Accuracy improvement: {accuracy_improvement:+.2f} percentage points")
print(f"   • JSON validity improvement: {json_improvement:+.2f} percentage points")

# Detailed case-by-case comparison
print(f"\n🔍 CASE-BY-CASE COMPARISON:")
print("-" * 80)

for i in range(len(test_data)):
    # base_case = base_results['detailed_results'][i]
    trained_case = trained_results['detailed_results'][i]
    
    # print(f"\nTest {i+1}: {base_case['input'][:50]}...")
    # print(f"   Base model:    {'✅' if base_case['is_perfect'] else '❌'} Perfect | {'✅' if base_case['is_valid_json'] else '❌'} JSON")
    print(f"   Trained model: {'✅' if trained_case['is_perfect'] else '❌'} Perfect | {'✅' if trained_case['is_valid_json'] else '❌'} JSON")
    
    # if base_case['is_perfect'] != trained_case['is_perfect']:
    #     if trained_case['is_perfect']:
    #         print(f"   🎉 IMPROVED: Base failed → Trained succeeded")
    #     else:
    #         print(f"   ⚠️ DEGRADED: Base succeeded → Trained failed")

# Save final model
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
torch.save(model.state_dict(), f'./models/robotics_codet5_final_{timestamp}.pth')

print(f"\n🎉 FINE-TUNING COMPLETED!")
print(f"💾 Models saved in ./models/")

# Show training summary
print(f"\n📊 TRAINING SUMMARY:")
for h in training_history:
    print(f"   Epoch {h['epoch']}: Train={h['train_loss']:.4f}, Val={h['val_loss']:.4f}")

# Save comparison results to file - MODIFIED FOR TRAINED MODEL ONLY
comparison_report = {
    'timestamp': timestamp,
    'config': CONFIG,
    # 'base_model_results': base_results,  # Commented out when base model not tested
    'trained_model_results': trained_results,
    'training_history': training_history,
    # 'improvements': {  # Commented out when no base model comparison
    #     'accuracy': accuracy_improvement,
    #     'json_validity': json_improvement
    # }
}

with open(f'./models/comparison_report_{timestamp}.json', 'w') as f:
    json.dump(comparison_report, f, indent=2)

print(f"\n📄 Detailed comparison report saved as: comparison_report_{timestamp}.json")
print(f"\n🚀 Model trained and ready to use!")