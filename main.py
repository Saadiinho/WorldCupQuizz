import random
import pandas as pd
import csv

def ajouter_ligne(file, ligne):
    with open(file, mode='a', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerow(ligne)




#Step 1: Recup data
data = pd.read_csv('WorldCups.csv')

#Step 2: Separate data to list
date = data['Year'].to_list()
country = data['Country'].to_list()
winner = data['Winner'].to_list()
runners_up = data['Runners-Up'].to_list()
third = data['Third'].to_list()
fourth = data['Fourth'].to_list()
goal_scored = data['GoalsScored'].to_list()
domains = [date, country, winner, runners_up, third, fourth, goal_scored]

#Step 3: Create answers
length_list = len(date)


def create_answer(domain, index):
    #Vérification de l'unicité des réponses affichées
    while True:
        #Création des index des trois autres réponses
        answer1 = random.randint(0, length_list - 1)
        answer2 = random.randint(0, length_list - 1)
        answer3 = random.randint(0, length_list - 1)
        #Vérification si tous les index sont différents
        if (answer1 != index and answer2 != index and answer3 != index):
            if (answer1 != answer2 and answer1 != answer3):
                if (answer2 != answer3):
                    #Vérifications de toutes les valeurs des index
                    if (domain[answer1] != domain[index] and domain[answer2] != domain[index] and domain[answer3] != domain[index]):
                        if (domain[answer1] != domain[answer2] and domain[answer1] != domain[answer3]):
                            if (domain[answer2] != domain[answer3]):
                                #Si tout est différent, on sort de la boucle
                                break
    answers = [domain[index], domain[answer1], domain[answer2], domain[answer3]]
    random.shuffle(answers)
    i = 1
    for answer in answers:
        print(i, '-', answer)
        i+=1
    return answers

#Step 4: Create Questions
def create_question(index, index_question):
    if index_question == 1:
        print("Où s'est déroulé la coupe du monde en ", date[index], ' ?')
    elif index_question == 2: 
        print("Qui a remporté la coupe du monde en ", date[index], " ?")
    elif index_question == 3: 
        print("Qui a été vice-champion lors de la coupe du monde ", date[index], " ?")
    elif index_question == 4: 
        print("Qui est arrivé à la troisième position lors de la coupe du monde ", date[index], " ?")
    elif index_question == 5: 
        print("Qui est arrivé à la quatrième position lors de la coupe du monde ", date[index], ' ?')
    else :
        print("Quel nombre de buts ont été marqués lors de la coupe du monde en ", date[index], ' ?')

def get_correct_answer(answers, correct_answer_index):
    return answers[correct_answer_index]

def get_correct_answer_index(answers, correct_answer):
    return answers.index(correct_answer) + 1

def choose_answer():
    index = random.randint(0, length_list -1)
    index_question = random.randint(1, len(domains) - 1)
    create_question(index, index_question)
    answers = create_answer(domains[index_question], index)
    user_input = int(input('Choisissez votre réponse : '))
    while (user_input < 1 or user_input > 4):
        user_input = int(input('Erreur, veuillez rentrer un numéro entre 1 et 4 : '))

    # Get the correct answer
    correct_answer = get_correct_answer(domains[index_question], index)

    # Check if the user's answer matches the correct answer
    if user_input == get_correct_answer_index(answers, correct_answer):
        print("Bravo, votre réponse est correcte !")
        return True
    else:
        print("Désolé, votre réponse est incorrecte. La réponse correcte était", correct_answer)
        return False



def start():
    pseudo = input("Entrez votre pseudo : ")
    print("La partie peut commencer !")
    score = 0
    question = 1
    while question <= 10:
        print("\nQuestion numéro ", question)
        correct = choose_answer()
        if correct:
            score += 1
            print("Votre score : ", score, '\n')
        question += 1
    print("Quizz terminé.\nVotre score :", score,'\n')
    # Utilisation de la fonction pour ajouter une ligne dans le fichier
    nouvelle_ligne = [pseudo, score]
    ajouter_ligne("scores.csv", nouvelle_ligne)

def afficher_score():
    score = pd.read_csv("scores.csv")
    print(score.sort_values('Score', ascending=False))

    
def menu():
    print('#'*46)
    print('#', ' '*42, '#')
    print("# Bonjour et bienvenue dans WorldCup Quizz ! #")
    print('#', ' '*42, '#')
    print('#'*46)
    print('\n')
    choice = -1
    while choice != 0:
        print("1- Commencer le quiz.")
        print("2- Afficher les scores des joueurs.")
        print("0- Quitter")
        choice = int(input("Votre choix :"))
        while choice != 1 and choice != 2 and choice != 0:
            choice = int(input("Je n'ai pas compris, veuillez réessayer :"))
        if choice == 1:
            start()
        elif choice == 2:
            afficher_score() 
            print('\n')
        
menu()

