def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path=book_path)
    words = count_words(text=text)
    print(f"Text has {words} words.")


def read_book(book_path):
    with open(book_path, "r") as book_file:
            book = book_file.read()
    return book

def count_words(text):
    return len(text.split())

if __name__  == "__main__":
    main()
