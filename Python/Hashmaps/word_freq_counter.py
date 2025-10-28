from hash_map import HashTable
import re
import sys


def analyze_text_file(filename):
    """Analyze word frequencies in a text file."""
    word_freq = HashTable(100)
    total_words = 0

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                # Convert to lowercase and extract words (letters and hyphens)
                words = re.findall(r"\b[a-z]+(?:-[a-z]+)*\b", line.lower())

                for word in words:
                    if len(word) > 0:  # Skip empty strings
                        total_words += 1
                        count = word_freq.get(word) or 0
                        word_freq.put(word, count + 1)

        return word_freq, total_words

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, 0


def analyze_text_string(text):
    """Analyze word frequencies in a string."""
    word_freq = HashTable(100)
    total_words = 0

    # Convert to lowercase and extract words
    words = re.findall(r"\b[a-z]+(?:-[a-z]+)*\b", text.lower())

    for word in words:
        if len(word) > 0:
            total_words += 1
            count = word_freq.get(word) or 0
            word_freq.put(word, count + 1)

    return word_freq, total_words


def get_top_words(word_freq, n=10):
    """Get top N most frequent words."""
    # Collect all word-frequency pairs
    word_list = []

    for bucket in word_freq.bucket_array:
        if bucket:
            current = bucket.head
            while current:
                word_list.append((current.key, current.value))
                current = current.next

    # Sort by frequency (descending)
    word_list.sort(key=lambda x: x[1], reverse=True)

    return word_list[:n]


def print_statistics(word_freq, total_words, top_n=20):
    """Print detailed statistics about word frequencies."""
    print("\n" + "=" * 60)
    print("WORD FREQUENCY ANALYSIS")
    print("=" * 60)

    print(f"\nTotal words: {total_words}")
    print(f"Unique words: {word_freq.size}")
    print(f"Vocabulary richness: {(word_freq.size/total_words)*100:.2f}%")

    # Get top words
    top_words = get_top_words(word_freq, top_n)

    print(f"\nTop {len(top_words)} Most Frequent Words:")
    print("-" * 60)
    print(f"{'Rank':<6} {'Word':<20} {'Count':<10} {'Percentage'}")
    print("-" * 60)

    for i, (word, count) in enumerate(top_words, 1):
        percentage = (count / total_words) * 100
        print(f"{i:<6} {word:<20} {count:<10} {percentage:.2f}%")

    print("\n" + "=" * 60)


def search_word(word_freq, word):
    """Search for a specific word's frequency."""
    count = word_freq.get(word.lower())
    if count:
        print(f"\nThe word '{word}' appears {count} time(s)")
    else:
        print(f"\nThe word '{word}' was not found in the text")


if __name__ == "__main__":
    print("Word Frequency Counter")
    print("=" * 60)

    # Check if filename provided as command line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        word_freq, total_words = analyze_text_file(filename)
    else:
        # Demo mode with sample text
        print("\nNo file specified. Running demo with sample text...\n")

        sample_text = """
        The quick brown fox jumps over the lazy dog. The dog was very lazy,
        but the fox was quick and brown. Foxes are known to be quick animals.
        The quick fox and the lazy dog became friends. They would play together
        every day. The brown fox loved to jump and run, while the lazy dog
        preferred to rest under the tree. Despite their differences, the fox
        and the dog were the best of friends in the forest.
        """

        word_freq, total_words = analyze_text_string(sample_text)

    if word_freq:
        print_statistics(word_freq, total_words, top_n=15)

        # Interactive search
        print("\nWould you like to search for specific words? (y/n): ", end="")
        try:
            response = input().strip().lower()

            while response == "y":
                print("Enter word to search (or 'quit' to exit): ", end="")
                search_term = input().strip()

                if search_term.lower() == "quit":
                    break

                search_word(word_freq, search_term)

                print("\nSearch another word? (y/n): ", end="")
                response = input().strip().lower()

        except (EOFError, KeyboardInterrupt):
            print("\n\nExiting...")

    print("\nAnalysis complete!")
