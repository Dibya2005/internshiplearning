from transformers import AutoTokenizer
import os

# Create output directory
os.makedirs("results", exist_ok=True)

# Load tokenizers
tokenizers = {
    "bert-base-uncased": AutoTokenizer.from_pretrained("bert-base-uncased"),
    "distilbert-base-uncased": AutoTokenizer.from_pretrained("distilbert-base-uncased"),
    "gpt2": AutoTokenizer.from_pretrained("gpt2")
}

# GPT2 has no pad token by default
tokenizers["gpt2"].pad_token = tokenizers["gpt2"].eos_token

sentences = [
    "I love learning Natural Language Processing.",
    "Transformers have revolutionized NLP."
]

# Original sentence, tokens, token IDs, attention mask, total token count
for i, sentence in enumerate(sentences, start=1):

    print("\n" + "=" * 80)
    print(f"Sentence {i}")
    print("=" * 80)

    for name, tokenizer in tokenizers.items():

        encoding = tokenizer(sentence)

        tokens = tokenizer.convert_ids_to_tokens(
            encoding["input_ids"]
        )

        print(f"\nTokenizer: {name}")

        print("Original Sentence:")
        print(sentence)

        print("\nTokens:")
        print(tokens)

        print("\nToken IDs:")
        print(encoding["input_ids"])

        print("\nAttention Mask:")
        print(encoding["attention_mask"])

        print("\nTotal Token Count:")
        print(len(encoding["input_ids"]))

        print("-" * 80)

# Compare tokenization results
print("\n\nTOKENIZER COMPARISON")

for sentence in sentences:

    print("\n" + "=" * 80)
    print("Sentence:", sentence)
    print("=" * 80)

    for name, tokenizer in tokenizers.items():

        tokens = tokenizer.tokenize(sentence)

        print(f"\n{name} Tokens:")
        print(tokens)


#trucation and padding
short_sentence = "I love NLP."

long_sentence = """
Transformers have revolutionized natural language processing by enabling
models to understand context better and achieve state-of-the-art performance
across many different NLP tasks and applications.
"""

max_len = 15
tokenizer=tokenizers["bert-base-uncased"] 

for sentence in [short_sentence, long_sentence]:

    encoding = tokenizer(
        sentence,
        padding="max_length",
        truncation=True,
        max_length=max_len
    )

    tokens = tokenizer.convert_ids_to_tokens(
        encoding["input_ids"]
    )

    print("\n" + "=" * 80)
    print("Original Sentence:")
    print(sentence)

    print("\nTokens:")
    print(tokens)

    print("\nToken IDs:")
    print(encoding["input_ids"])

    print("\nAttention Mask:")
    print(encoding["attention_mask"])

    print("\nFinal Sequence Length:")
    print(len(encoding["input_ids"]))