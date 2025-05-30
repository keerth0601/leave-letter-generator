from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load fine-tuned model
model_path = "./finetuned_tinygpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Function to generate leave letter
def generate_letter(name, to, reason, from_date, to_date):
    prompt = f"From: {name}\nTo: {to}\nReason: {reason}\nFrom Date: {from_date}\nTo Date: {to_date}\nLeave Letter:\n"
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]

    # Generate output
    output = model.generate(
        input_ids,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.9,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )

    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return result[len(prompt):].strip()

# Example
if __name__ == "__main__":
    letter = generate_letter("Keerth", "Priya", "I am sick", "2025-05-15", "2025-05-24")
    print("\nGenerated Leave Letter:\n")
    print(letter)
