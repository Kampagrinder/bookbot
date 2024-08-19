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

   