# Import AutoTokenizer class
# This automatically loads the correct tokenizer
# for the model you are using.
from transformers import AutoTokenizer


# Import AutoModelForCausalLM
# "CausalLM" means:
# the model predicts the next token sequentially.
# Used in GPT-like models.
from transformers import AutoModelForCausalLM


# Import PyTorch library
# Used for tensors, GPU operations, model execution.
import torch


# Path where your model exists locally.
# r"" means raw string.
# Prevents issues with Windows backslashes.
model_path = r"C:\Users\nilam\Desktop\internship\phi3-mini-model"


# Load tokenizer from local folder.
tokenizer = AutoTokenizer.from_pretrained(

    # Location of tokenizer files.
    model_path,

    # Prevents downloading from internet.
    # Only loads local files.
    local_files_only=True,

    # Allows custom tokenizer/model code.
    # Needed for some models like Phi.
    trust_remote_code=True
)


# Load the actual language model.
model = AutoModelForCausalLM.from_pretrained(

    # Path of local model.
    model_path,

    # Set datatype:
    # If GPU available -> FP16
    # Else -> FP32 for CPU.
    dtype=torch.float16 if torch.cuda.is_available()
    else torch.float32,

    # Automatically place model on GPU.
    # If no GPU -> None.
    device_map="auto" if torch.cuda.is_available()
    else None,

    # Only use local files.
    local_files_only=True,

    # Trust custom model implementation.
    trust_remote_code=True,

    # Attention implementation mode.
    # "eager" is safer and compatible.
    attn_implementation="eager"
)


# Input text prompt.
# This is what user asks the model.
prompt = "Explain what an LLM is."


# Convert text into tokens/tensors.
inputs = tokenizer(

    # Text input.
    prompt,

    # Return PyTorch tensors.
    return_tensors="pt"
)


# Check if GPU exists.
if torch.cuda.is_available():

    # Move tensors to GPU.
    # Important because model is on GPU.
    inputs = inputs.to(model.device)


# Generate response from model.
outputs = model.generate(

    # Pass tokenized input tensors.
    **inputs,

    # Maximum number of new tokens
    # model can generate.
    max_new_tokens=100
)


# Convert generated tokens back to text.
response = tokenizer.decode(

    # Take first generated sequence.
    outputs[0],

    # Remove special tokens like
    # <eos>, <pad>, etc.
    skip_special_tokens=True
)


# Print final generated response.
print(response)