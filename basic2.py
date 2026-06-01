from transformers import AutoTokenizer

model_path = r"C:\Users\nilam\Desktop\internship\phi3-mini-model"

tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    local_files_only=True,
    trust_remote_code=True
)

sentence = "hope you are doing good"

# Tokenize text
inputs = tokenizer(sentence, return_tensors="pt")

# Get input IDs
token_ids = inputs["input_ids"]

print("Token IDs:")
print(token_ids)