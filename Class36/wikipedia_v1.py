from bs4 import BeautifulSoup
import requests


def main():
    
    wikipedia("https://en.wikipedia.org/wiki/Hamilton_College", 100)
    
    
def wikipedia(url, max_pages):
    """Repeatedly find and "click" the first link in a Wikipedia article
    until you make it to the Philosophy article."""
    
    for i in range(max_pages):
        ## Did we get to philosophy?
        if url == "https://en.wikipedia.org/wiki/Philosophy":
            print("Yay, we made it to Philosophy after", i, "steps")
            return
        
        
        source_code = requests.get(url).text
        html = BeautifulSoup(source_code, "html.parser")
        
        ## Find the first <p> tag
        first_paragraph = html.find("p")
#         print(first_paragraph.text)

        ## Find the first link in the paragraph
        first_link = first_paragraph.find("a")
        
        print()
        print(i)
        print("Current URL:", url)
        print(first_link.text)

        ## Get the href of the first link
        href = first_link.get("href")
#         print(href)

        ## Make the new URL
        url = "https://en.wikipedia.org" + href

        


    
if __name__ == "__main__":
    main()
