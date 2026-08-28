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

def time_measure(language, correct, wrong):
    random_word = random.choice(language)

    print("Type the following word as fast as you can: \n")

    print(random_word)

    start_time = time.perf_counter()

    typed_word = input()

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    if typed_word == random_word:
        correct += 1
        print("\n Time elapsed:", execution_time, "seconds")
        print(correct, " Correct answers")
    else:
        wrong += 1
        print("Wrong spelling!")
        print("You typed ", typed_word, " instead of ", random_word)
        print(wrong, " Wrong answers")

    return correct, wrong

def main():

    correct = 0
    wrong = 0

    print("TypeSpeed \n\n")
    print("Available languages: English (1), Portuguese (2)")
    lan_choice = input("Select your language: \n")
    try:
        if lan_choice == '1':        
            print("Press enter to continue, CTRL + C to exit")
            input()
            while True:
                correct, wrong = time_measure(en, correct, wrong)
        elif lan_choice == '2':        
            print("Press enter to continue, CTRL + C to exit")
            input()
            while True:
                correct, wrong = time_measure(pt, correct, wrong)
        else:
            print("Option not available! \n")
    except KeyboardInterrupt:
        print("\nExiting...")

main()
