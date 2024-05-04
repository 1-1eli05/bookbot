def main():
   book_path = "books/frankenstein.txt"
   book_text=bookopener(book_path)
   num_of_words=wordcounter(book_text)
   counts=lettercounter(book_text)
   print(f"===Beginning {book_path} report===")
   print()
   print(bookopener(book_path))
   print()
   print(f"{num_of_words} words found in book")
   print()
   sort_report(counts)

#function to open and read the entire book
def bookopener(path):
     with open(path) as f:
        file_contents=f.read()
        return file_contents

#function to count the amount of words in the book
def wordcounter(book_text):
    words= book_text.split()
    return len(words)

#function to count the amount of each letter
def lettercounter(book_text):
        letter_count ={}
        for letter in book_text:
            current_count = letter_count.get(letter.lower(),0)
            letter_count[letter.lower()]= current_count +1
        return letter_count

#function to give a report on how many times each letter shows up
def sort_report(letter_count):
    letter_list= [{"letter":letter, "count":count} for letter, count in letter_count.items() if letter.isalpha()]
    letter_list.sort(key=lambda x: x['count'], reverse=True)
    for item in letter_list:
        print(f"The '{item['letter']}' character was found {item['count']} times")



main()