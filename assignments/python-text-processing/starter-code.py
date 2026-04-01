import string
from collections import Counter


def clean_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    words = [w.strip(string.punctuation).lower() for w in text.split()]
    return [w for w in words if w]


def word_counts(words):
    return Counter(words)


def save_report(output_path, filename, counts):
    total_words = sum(counts.values())
    unique_words = len(counts)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Analysis for {filename}\n")
        f.write(f"Total words: {total_words}, Unique words: {unique_words}\n\n")
        for word, count in counts.most_common(10):
            f.write(f"{word}: {count}\n")


if __name__ == "__main__":
    print("Starter code loaded. Fill in the CLI logic in main().")
