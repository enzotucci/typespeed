import time
import random

def time_measure():
    wordlist = [
    "japan", "cow", "green", "yellow", "cat", "bitcoin", "price", "random",
    
    "fox", "code", "jump", "blue", "data", "quiz", "web", "zoom", "wolf", "star",
    
    "rocket", "python", "matrix", "coffee", "galaxy", "wizard", "player", "shadow", 
    "crypto", "guitar", "jungle", "oxygen", "pixels", "safari", "vector", "liquid",
    
    "keyboard", "database", "algorithm", "astronaut", "dinosaur", "universe", 
    "scandals", "fraction", "velocity", "terminal", "software", "graphics",
    
    "PyThOn", "Ctrl+C", "lambda", "quadrilateral", "juxtaposition", "synchronize", 
    "cybersecurity", "javascript", "quantum", "infinity", "algorithm", "phenomenon"
]

    random_word = random.choice(wordlist)

    print("Type the following word as fast as you can: \n")

    print(random_word)

    start_time = time.perf_counter()

    input()

    endtime = time.perf_counter()

    execution_time = endtime - start_time
    print("\n Time elapsed:", execution_time, "seconds")


print("TypeSpeed \n\n")
print("Press enter to continue")
input()
while True:
    time_measure()
