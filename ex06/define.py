import sys, requests
from bs4 import BeautifulSoup

def define(word: str):
    response = requests.get("https://www.dexonline.ro/definitie/" + word)
    if response.status_code == 200:
        html_doc = response.text
    else:
        print("Nu exista pagina pentru acest cuvant")
        exit(1)
    
    soup = BeautifulSoup(html_doc, "html.parser")
    try:
        return soup.find("span", "tree-def").get_text()
    except AttributeError:
        return "Nu exista pagina pentru acest cuvant"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Bad usage")

    word = sys.argv[1]

    print(define(word))