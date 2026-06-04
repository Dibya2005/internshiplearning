"""
Task 2: Understand Hugging Face Tokenizers
------------------------------------------
Loads bert-base-uncased, distilbert-base-uncased, and gpt2 tokenizers.
Tokenizes 10 English sentences, compares output, demonstrates padding
and truncation, and saves all output to results/tokenization_examples.txt.

Run:
    python src/load_tokenizer.py
"""

import os
from transformers import AutoTokenizer

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MODELS = [
    "bert-base-uncased",
    "distilbert-base-uncased",
    "gpt2",
]

SENTENCES = [
    "Artificial intelligence is transforming the world.",
    "Machine learning helps computers learn from data.",
    "Natural language processing enables machines to understand text.",
    "Deep learning models require large amounts of training data.",
    "The quick brown fox jumps over the lazy dog.",
    "Transformers have revolutionized the field of NLP.",
    "Fine-tuning pretrained models saves time and resources.",
    "Tokenization is the first step in any NLP pipeline.",
    "Attention mechanisms allow models to focus on relevant parts of the input.",
    "Open source libraries like Hugging Face make AI research accessible.",
]

# A short and a long sentence for padding/truncation demo
PADDING_SENTENCES = [
    "Hello world.",
    "This is a much longer sentence that contains many more words and will "
    "demonstrate what happens when truncation is applied with a fixed "
    "maximum sequence length during tokenization of input text for "
    "transformer models that have a limited context window size.",
]

MAX_LENGTH = 32
OUTPUT_PATH = os.path.join("results", "tokenization_examples.txt")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def separator(char="=", width=70):
    return char * width


def print_and_write(text, file_handle):
    print(text)
    file_handle.write(text + "\n")


def tokenize_and_display(tokenizer, sentence, model_name, fh, max_length=None,
                          padding=False, truncation=False):
    """Tokenize a sentence and display all details."""
    kwargs = {}
    if max_length is not None:
        kwargs["max_length"] = max_length
    if padding:
        kwargs["padding"] = "max_length"
    if truncation:
        kwargs["truncation"] = True

    encoding = tokenizer(sentence, **kwargs)

    tokens = tokenizer.convert_ids_to_tokens(encoding["input_ids"])
    token_ids = encoding["input_ids"]
    attention_mask = encoding.get("attention_mask", "N/A")
    token_count = len(token_ids)

    print_and_write(f"  Model       : {model_name}", fh)
    print_and_write(f"  Sentence    : {sentence}", fh)
    print_and_write(f"  Tokens      : {tokens}", fh)
    print_and_write(f"  Token IDs   : {token_ids}", fh)
    print_and_write(f"  Attn Mask   : {attention_mask}", fh)
    print_and_write(f"  Token Count : {token_count}", fh)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs("results", exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:

        # ---------------------------------------------------------------
        # Load tokenizers
        # ---------------------------------------------------------------
        print_and_write(separator(), fh)
        print_and_write("TASK 2 — HUGGING FACE TOKENIZER ANALYSIS", fh)
        print_and_write(separator(), fh)

        tokenizers = {}
        for model_name in MODELS:
            print_and_write(f"\nLoading tokenizer: {model_name} ...", fh)
            tokenizers[model_name] = AutoTokenizer.from_pretrained(model_name)
            vocab_size = tokenizers[model_name].vocab_size
            print_and_write(f"  Vocab size  : {vocab_size}", fh)
            print_and_write(
                f"  Special tokens: {tokenizers[model_name].all_special_tokens}", fh
            )

        # ---------------------------------------------------------------
        # Section 1: Token-by-token comparison across all 10 sentences
        # ---------------------------------------------------------------
        print_and_write("\n" + separator(), fh)
        print_and_write("SECTION 1 — TOKENIZING 10 SENTENCES (ALL TOKENIZERS)", fh)
        print_and_write(separator(), fh)

        for i, sentence in enumerate(SENTENCES, start=1):
            print_and_write(f"\n[Sentence {i}]", fh)
            for model_name, tokenizer in tokenizers.items():
                tokenize_and_display(tokenizer, sentence, model_name, fh)
            print_and_write(separator("-"), fh)

        # ---------------------------------------------------------------
        # Section 2: Side-by-side comparison on same sentences
        # ---------------------------------------------------------------
        print_and_write("\n" + separator(), fh)
        print_and_write("SECTION 2 — SIDE-BY-SIDE TOKEN COMPARISON", fh)
        print_and_write("(same sentence, different tokenizers)", fh)
        print_and_write(separator(), fh)

        comparison_sentences = SENTENCES[:5]
        for sentence in comparison_sentences:
            print_and_write(f"\nSentence: {sentence}", fh)
            for model_name, tokenizer in tokenizers.items():
                encoding = tokenizer(sentence)
                tokens = tokenizer.convert_ids_to_tokens(encoding["input_ids"])
                print_and_write(f"  [{model_name:30s}] {tokens}", fh)

        # ---------------------------------------------------------------
        # Section 3: Padding and truncation demonstration
        # ---------------------------------------------------------------
        print_and_write("\n" + separator(), fh)
        print_and_write(
            f"SECTION 3 — PADDING AND TRUNCATION (max_length={MAX_LENGTH})", fh
        )
        print_and_write(separator(), fh)

        for model_name, tokenizer in tokenizers.items():
            print_and_write(f"\nModel: {model_name}", fh)
            print_and_write(separator("-"), fh)

            for label, sentence in zip(["SHORT", "LONG"], PADDING_SENTENCES):
                print_and_write(f"\n  [{label} SENTENCE — no padding/truncation]", fh)
                tokenize_and_display(tokenizer, sentence, model_name, fh)

                print_and_write(
                    f"\n  [{label} SENTENCE — padding=True, truncation=True, "
                    f"max_length={MAX_LENGTH}]",
                    fh,
                )
                tokenize_and_display(
                    tokenizer, sentence, model_name, fh,
                    max_length=MAX_LENGTH, padding=True, truncation=True
                )

        # ---------------------------------------------------------------
        # Section 4: Token count summary table
        # ---------------------------------------------------------------
        print_and_write("\n" + separator(), fh)
        print_and_write("SECTION 4 — TOKEN COUNT SUMMARY TABLE", fh)
        print_and_write(separator(), fh)

        header = f"{'Sentence':60s} " + " ".join(
            f"{m.split('-')[0]:>12s}" for m in MODELS
        )
        print_and_write(header, fh)
        print_and_write(separator("-"), fh)

        for sentence in SENTENCES:
            counts = []
            for tokenizer in tokenizers.values():
                count = len(tokenizer(sentence)["input_ids"])
                counts.append(count)
            row = f"{sentence[:58]:60s} " + " ".join(f"{c:>12d}" for c in counts)
            print_and_write(row, fh)

        print_and_write("\n" + separator(), fh)
        print_and_write("Output complete.", fh)
        print_and_write(separator(), fh)

    print(f"\nAll output saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
