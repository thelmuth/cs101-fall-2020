import random

NOUNS = ["dog", "person", "octopus", "platypus", "monkey", "computer", "chair",
         "cat", "juice", "book", "TV", "bacon", "egg", "Abraham Lincoln", "bagel"]

ARTICLES = ["a", "the"]

VERBS = ["jumps", "reads", "guffaws", "sleeps", "sits", "laughs", "swims", "eats",
         "fights", "loves", "destroys", "is", "discombobulates", "flies", "skips"]

PREPOSITIONS = ["under", "in", "above", "on", "through", "with", "between", "over"]

PUNCTUATION = ".!?"

ADJECTIVES = ["lovely", "gooey", "violent", "French", "sloppy", "purple", "salty",
              "moist", "small", "icky", "delicious", "thick", "smelly", "little",
              "tall", "tough", "fragile", "hairy"]

def main():
    """Generate and print a random sentence.
       THIS DOCSTRING HAS MULTIPLE LINES."""
    
    generated_sentence = sentence()
    fancy_sentence = capitalize_and_punctuate(generated_sentence)
    print(fancy_sentence)

def capitalize_and_punctuate(sent):
    """Capitalizes the first word of sent and adds punctuation at the end."""
    first = sent[0]
    capital_first = first.upper()
    capitalized = capital_first + sent[1:]
    return capitalized + random.choice(PUNCTUATION)
    
def sentence():
    """Builds and returns a random sentence."""
    return noun_phrase() + " " + verb_phrase()
    
def noun_phrase():
    """Build and return a noun phrase."""
    
    num_adjs = random.randint(0, 4)
    adjs = adjectives(num_adjs)
    
    article = random.choice(ARTICLES)
    noun = random.choice(NOUNS)
    
    adjs_and_noun = adjs + noun
    
    if adjs_and_noun[0] in "aeiouAEIOU" and article == "a":
        article = "an"
    
    return article + " " + adjs_and_noun
    
def verb_phrase():
    """Makes a verb phrase and returns it"""
    verb = random.choice(VERBS)
    np = noun_phrase()
    pp = prepositional_phrase()
    return verb + " " + np + " " + pp

def prepositional_phrase():
    """Builds and returns a prepositional phrase."""
    preposition = random.choice(PREPOSITIONS)
    np = noun_phrase()
    return preposition + " " + np

def adjectives(number_of_adjectives):
    """Returns a string containing zero or more adjectives based on the parameter."""
    
    adjs = ""
    for _ in range(number_of_adjectives):
        adj = random.choice(ADJECTIVES)
        adjs += adj + " "
        
    return adjs
    
    
    
    
if __name__ == "__main__":
    main()
