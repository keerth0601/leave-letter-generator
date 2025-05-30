from flask import Flask, request, jsonify
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import os

app = Flask(__name__)

# Use absolute path to avoid Hugging Face repo name errors
model_path = os.path.abspath("finetuned_tinygpt2")

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained(model_path, local_files_only=True)

model = GPT2LMHeadModel.from_pretrained(
    model_path,
    local_files_only=True,
    trust_remote_code=True
)

model.eval()

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    name = data.get("name", "")
    from_date = data.get("from_date", "")
    to_date = data.get("to_date", "")
    reason = data.get("reason", "")
    to = data.get("to", "")

    input_text = f"From: {name}\nTo: {to}\nDates: {from_date} to {to_date}\nReason: {reason}\nLetter:\n"
    inputs = tokenizer.encode(input_text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=300,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            pad_token_id=tokenizer.eos_token_id
        )

    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    letter_start = output_text.find("Letter:\n")
    final_letter = output_text[letter_start + len("Letter:\n"):] if letter_start != -1 else output_text

    return jsonify({"letter": final_letter.strip()})

if __name__ == "__main__":
    app.run(debug=True)
