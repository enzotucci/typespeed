import time
import random

en = [
    "japan", "cow", "green", "yellow", "cat", "bitcoin", "price", "random",
    
    "fox", "code", "jump", "blue", "data", "quiz", "web", "zoom", "wolf", "star",
    
    "rocket", "python", "matrix", "coffee", "galaxy", "wizard", "player", "shadow", 
    "crypto", "guitar", "jungle", "oxygen", "pixels", "safari", "vector", "liquid",
    
    "keyboard", "database", "algorithm", "astronaut", "dinosaur", "universe", 
    "scandals", "fraction", "velocity", "terminal", "software", "graphics",
    
    "PyThOn", "Ctrl+C", "lambda", "quadrilateral", "juxtaposition", "synchronize", 
    "cybersecurity", "javascript", "quantum", "infinity", "algorithm", "phenomenon"
]

pt = [
    "sol", "mar", "casa", "bola", "gato", "azul", "café", "vida", "fogo", "água",
    "ouro", "alvo", "jogo", "paz", "luz", "rocha", "fácil", "útil",
    
    "brasil", "computador", "janela", "música", "coração", "caneta", "frango", "floresta",
    "projeto", "código", "sombra", "viagem", "Espelho", "Planeta", "Xícara", "Açúcar",
    "Goiaba", "Foguete", "Trovão", "Gelo",
    
    "algoritmo", "astronauta", "dinossauro", "universo", "velocidade", "terminal", 
    "teclado", "biblioteca", "arquitetura", "borboleta", "chocolate", "dicionário",
    
    "paralelepípedo", "seqüência", "exceção", "antiguidade", "cabeçalho", "quilômetro",
    "bênção", "órgão", "paciência", "consciência", "substância", "frequência"
]

def time_measure(language):

    random_word = random.choice(language)

    print("Type the following word as fast as you can: \n")

    print(random_word)

    start_time = time.perf_counter()

    input()

    endtime = time.perf_counter()

    execution_time = endtime - start_time
    print("\n Time elapsed:", execution_time, "seconds")


print("TypeSpeed \n\n")
print("Avaible languages: English (1), Portuguese (2)")
lan_choice = input("Select your language: \n")
if lan_choice == '1':        
    print("Press enter to continue, CTRL + C to exit")
    input()
    while True:
        time_measure(en)
if lan_choice == '2':        
    print("Press enter to continue, CTRL + C to exit")
    input()
    while True:
        time_measure(pt)
else:
    print("Option not avaible! \n")
