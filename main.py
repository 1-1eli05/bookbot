def main():
    with open("books/frankenstein.txt") as f:
        file_contents=f.read()
    print(file_contents)
    print(wordcounter())
    counts=lettercounter()
    sort_report(counts)

def wordcounter():
    with open("books/frankenstein.txt") as f:
        file_contents=f.read()
        words= file_contents.split()
    return len(words)

def lettercounter():
        letter_count ={}
        with open("books/frankenstein.txt") as f:
            file_contents=f.read()
        for letter in file_contents:
            current_count = letter_count.get(letter.lower(),0)
            letter_count[letter.lower()]= current_count +1
        return letter_count

def sort_report(letter_count):
    letter_list= [{"letter":letter, "count":count} for letter, count in letter_count.items() if letter.isalpha()]
    letter_list.sort(key=lambda x: x['count'], reverse=True)
    for item in letter_list:
        print(f"The '{item['letter']}' character was found {item['count']} times")



main()