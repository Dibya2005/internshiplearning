from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
import torch

model_path = r"C:\Users\nilam\Desktop\internship\phi3-mini-model"

tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    local_files_only=True,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto" if torch.cuda.is_available() else None,
    local_files_only=True,
    trust_remote_code=True,
    attn_implementation="eager"
)

prompt = "Explain what an LLM is."

inputs = tokenizer(prompt, return_tensors="pt")

if torch.cuda.is_available():
    inputs = inputs.to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=100
)

response = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print(response)