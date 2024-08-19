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
     
print (word_count())

def character_count(text):
    lowered_string = text.lower()
    char_counts = {}
    for i in lowered_string:
        if i in char_counts:
            char_counts[i] += 1
        else: char_counts[i] = 1
    return char_counts

with open("books/frankenstein.txt", "r") as file:
    content = file.read()

result = character_count(content)
print(result)

    


   