from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt


def main():

    electoral_votes = electoral_college()
#     print(electoral_votes)

    population = get_population()
#     print(population)

    states = list(electoral_votes.keys())
    states.sort()
#     print(states)

    people_per_vote = []
    for state in states:
        votes = electoral_votes[state]
        pop_of_state = population[state]
        print(state, "has a population of", pop_of_state, "and", votes, "electoral college votes")
        
        pop_per_vote = pop_of_state / votes
        people_per_vote.append(pop_per_vote)
        
    
    ### Make a graph of people per vote
    plt.bar(states, people_per_vote)
    plt.xticks(rotation=90)
    plt.ylabel("People per electoral college vote")
    plt.show()
    
    
def remove_commas(string):
    """Takes a string and removes all commas."""
    
    new_string = ""
    
    for char in string:
        if char != ",":
            new_string += char
            
    return new_string
    

def get_population():
    """Parse Wikipedia's website of states to get the population of
    each state."""
    
    url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
    source_code = requests.get(url).text
    html = BeautifulSoup(source_code, "html.parser")

    ### Find all table rows
    ### Turns out, there are way too many tables
#     rows = html.find_all("tr")
#     print(len(rows))

    population_dictionary = {"District of Columbia": 705749}

    states_table = html.find("table")
    
    rows = states_table.find_all("tr")
    
    for row in rows:
        
        cells = row.find_all("td")
        
        if len(cells) > 0:
#             print(row)
            row_header = row.find("th")
            state = row_header.text.strip()
#             print(state)
#             print(cells)

            ### Check for commonwealths
            if state[-3:] == "[E]":
                state = state[:-3]

            ### Use negative indexing to get the state's population
            population_string = cells[-8].text
#             print(population_string)

            population = int(remove_commas(population_string))
#             print(population)

            population_dictionary[state] = population
            
    return population_dictionary



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
