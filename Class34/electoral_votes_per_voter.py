from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt


def main():

    electoral_votes = electoral_college()
    print(electoral_votes)


def electoral_college():
    """Parse a website to find the number of electoral college
    votes for each state and return that as a dictionary."""
    
    url = "https://www.britannica.com/topic/United-States-Electoral-College-Votes-by-State-1787124"
    source_code = requests.get(url).text
    
#     print(source_code[:200])

    html = BeautifulSoup(source_code, "html.parser")
    
    electoral_table = html.find("table")
    
#     print(electoral_table)

    ### Find the rows of the table:
    rows = electoral_table.find_all("tr")
#     print(rows)

    electoral_votes = {}

    for row in rows:
        cells = row.find_all("td")
        
#         for cell in cells:
#             print(cell)
#             print(cell.text)

#         print("length of cells", len(cells))        

        if len(cells) == 6:
            electoral_votes[cells[0].text] = int(cells[1].text)
            electoral_votes[cells[2].text] = int(cells[3].text)
            electoral_votes[cells[4].text] = int(cells[5].text)
        
    return electoral_votes

    
if __name__ == "__main__":
    main()
