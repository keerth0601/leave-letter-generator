from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling
import os

# Paths
model_name = "gpt2"
dataset_path = "./leave_letters_dataset.jsonl"
output_dir = "./finetuned_tinygpt2"

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Make sure tokenizer has padding token
tokenizer.pad_token = tokenizer.eos_token

# Convert JSONL to plain text (required for TextDataset)
def convert_jsonl_to_text(jsonl_path, output_text_path):
    import json
    with open(jsonl_path, 'r', encoding='utf-8') as fin, open(output_text_path, 'w', encoding='utf-8') as fout:
        for line in fin:
            data = json.loads(line)
            fout.write(data['text'].strip() + "\n\n")

plain_text_path = "./leave_letters.txt"
convert_jsonl_to_text(dataset_path, plain_text_path)

# Load dataset
dataset = TextDataset(
    tokenizer=tokenizer,
    file_path=plain_text_path,
    block_size=128
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False
)

# Training arguments
training_args = TrainingArguments(
    output_dir=output_dir,
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=500,
    save_total_limit=1,
    logging_steps=100
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset
)

# Train the model
trainer.train()

# Save model and tokenizer locally
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)

print(f"✅ Fine-tuned model saved to {output_dir}")
