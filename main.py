def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path=book_path)
    words = count_words(text=text)
    letters = count_letters(text)
    display_report(path=book_path, words=words, letters=letters)



def read_book(book_path):
    with open(book_path, "r") as book_file:
            book = book_file.read()
    return book


def count_words(text):
    return len(text.split())


def count_letters(text):
    letters = {}
    for char in text:
        lowered = char.lower()
        if lowered not in letters:
            letters[lowered] = 0
        letters[lowered] += 1

    return letters


def display_report(path, words, letters):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document\n")
    sorted_letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_letters.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")

    print("--- End report ---")



if __name__  == "__main__":
    main()
