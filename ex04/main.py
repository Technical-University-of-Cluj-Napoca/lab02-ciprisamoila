from search_engine import search_loop
from BST import BST

if __name__ == "__main__":
    print("Type ro for romanian, en for english: ")
    s = input()
    bst = None
    if s == "ro":
        # from file
        bst = BST("wordlist.txt", file=True, url=False)
    else:
        # from url
        bst = BST("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt", file=False, url=True)
    search_loop(bst)