from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "sshleifer/tiny-gpt2"
save_path = "./models/tiny-gpt2"

# Download and save the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.save_pretrained(save_path)

# Download and save the model
model = AutoModelForCausalLM.from_pretrained(model_id)
model.save_pretrained(save_path)
