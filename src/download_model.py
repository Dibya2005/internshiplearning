import os
from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    model_name = "distilgpt2"
    
    # 1. Find the exact directory this script is inside (the 'src' folder)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Go up one level to the project root
    project_root = os.path.dirname(script_dir)
    
    # 3. Join the root with 'models/downloaded_model'
    save_path = os.path.join(project_root, "models", "downloaded_model")

    print(f"Target save path resolved to: {save_path}")

    # Ensure the directory exists
    os.makedirs(save_path, exist_ok=True)

    print(f"Loading Tokenizer: '{model_name}'...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    print(f"Loading Model: '{model_name}' (This might take a minute to download)...")
    model = AutoModelForCausalLM.from_pretrained(model_name)

    print(f"\nSaving tokenizer and model locally to: {save_path}")
    tokenizer.save_pretrained(save_path)
    model.save_pretrained(save_path)

    print("\nSuccess! The model is now saved in the correct root models/ directory.")

if __name__ == "__main__":
    main()