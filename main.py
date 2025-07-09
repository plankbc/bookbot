from stats import gen_report, get_num_chars, get_num_words
import sys


def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit[1]
    print("=" * 12, " BOOKBOT ", "=" *12)
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("-" * 12, " Word Count ", "-" * 12)
    word_count = get_num_words()
    print(f"Found {word_count[1]} total words")
    print("-" *8, " Character Count ", "-" * 8)
    letters = get_num_chars(word_count[0])
    gen_report(letters)
    print("=" * 12, " End ", "=" * 12)
    

   

if __name__ == "__main__":
    main()