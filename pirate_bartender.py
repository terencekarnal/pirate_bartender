import random


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def question_func(a = False, b = False, c = False, d = False, e = False):
    """This asks questions and returns the ingredients mapped to a boolean"""
    #indented code block goes here
    answers = {}
    for question in questions:
       x = input(questions[question] + " (Y or N): ")
       if x == "Y" :
            answers[question] = True
       else :
             answers[question] = False
    
    return answers

'''
if __name__ == '__main__':
   question_func()
'''

def drink_constructor():
    """This randomly selects a drink items for the true pieces."""
    drink = question_func(a = False, b = False, c = False, d = False, e = False)
    for ingred in drink:
        if drink[ingred] == True:
            drink[ingred] = random.choice(ingredients[ingred])
        else :
            drink[ingred] = "n/a"
            
    print(drink)
    
if __name__ == '__main__':
   drink_constructor()    



