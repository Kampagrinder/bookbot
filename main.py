def main():
    with open("books/frankenstein.txt") as f:
     file_contents = f.read()
if __name__ == "__main__":
    main()
def word_count():
     with open("books/frankenstein.txt") as f:
         words = f.read()
         word = words.split()
         return len(word)
     

def character_count(text):
    lowered_string = text.lower()
    char_counts = {}
    for i in lowered_string:
        if i.isalpha():
             if i in char_counts:
                 char_counts[i] += 1
             else:
                char_counts[i] = 1
    return char_counts

with open("books/frankenstein.txt", "r") as file:
    content = file.read()

result = character_count(content)
resultlist = list(result.items())

def sort_on(resultlist):
    return resultlist[1]
resultlist.sort(key=sort_on, reverse=True)


print("--- Begin report of books/frankenstein.txt ---")
print (word_count(), "words found in the document")
print ()


def row_print(resultlist):
    for char, count in resultlist:
        print(f"The '{char}' character was found {count} times")

row_print(resultlist)











    


   