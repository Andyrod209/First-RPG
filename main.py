import random
# story line... still trying to decide how to go about this.
print('''
A cold summer night... At a kingdom called Tiryns. Evil was aproaching... 

guard
''')

hercules = {
    'name':'Hercules',
    'health': 100, 
    'Attack Power': 75,
    'attack 1': 20,
    'attack 2': 40,
    'attack 3': 15
}


enemy1 = {
    'name': 'Robert The Traditor',
    'health': 65,
    'Attack Power': 50,
    'attack 1': 15,
    'attack 2': 15,
    'attack 3': 20
}
# Battle/ gameplay
def attack(hero, enemy):
    # using random number to select who goes first
    turn = random.randint(1,2)

    
    if turn == 1:
        loop = True
        while loop is True:
            attack = int(input('To attack pick a number from 1, 2, 3'))
            if attack == 1:
                enemy['health'] - hero['attack 1']
                print(f'Attack on {enemy["name"]} with attack 1 for {hero["attack 1"]}')
                loop = False
            elif attack == 2:
                enemy['health'] - hero['attack 2']
                print(f'Attack on {enemy["name"]} with attack 2 for {hero["attack 2"]}')
                loop = False
            elif attack == 3:
                enemy['health'] - hero['attack 3'] 
                print(f'Attack on {enemy["name"]} with attack 3 for {hero["attack 3"]}')
                loop = False      
            else:
                print('INVAID CHOICE!')
            # add enemy turn here so it'll be one attack and then the next 
            # do the same on turn 2 so enemy attacks first and hero next
            attack = random.randint(1, 3)
        if attack == 1:
            hero['health'] - enemy['attack 1']
            print(f'Attack on {hero["name"]} with attack 1 for {enemy["attack 1"]}')
             
        elif attack == 2:
            hero['health'] - enemy['attack 2']
            print(f'Attack on {hero["name"]} with attack 2 for {enemy["attack 2"]}')
        elif attack == 3:
            hero['health'] - enemy['attack 3'] 
            print(f'Attack on {hero["name"]} with attack 3 for {enemy["attack 3"]}')

    elif turn == 2:
        attack = random.randint(1, 3)
        if attack == 1:
            hero['health'] - enemy['attack 1']
            print(f'Attack on {hero["name"]} with attack 1 for {enemy["attack 1"]}')
             
        elif attack == 2:
            hero['health'] - enemy['attack 2']
            print(f'Attack on {hero["name"]} with attack 2 for {enemy["attack 2"]}')
        elif attack == 3:
            hero['health'] - enemy['attack 3'] 
            print(f'Attack on {hero["name"]} with attack 3 for {enemy["attack 3"]}')

        loop = True
        while loop is True:
            attack = int(input('To attack pick a number from 1, 2, 3'))
            if attack == 1:
                enemy['health'] - hero['attack 1']
                print(f'Attack on {enemy["name"]} with attack 1 for {hero["attack 1"]}')
                loop = False
            elif attack == 2:
                enemy['health'] - hero['attack 2']
                print(f'Attack on {enemy["name"]} with attack 2 for {hero["attack 2"]}')
                loop = False
            elif attack == 3:
                enemy['health'] - hero['attack 3'] 
                print(f'Attack on {enemy["name"]} with attack 3 for {hero["attack 3"]}')
                loop = False      
            else:
                print('INVAID CHOICE!')
           
# fix so when there is no more health to hero or enemy
def no_health():
    if hero ["health"] <= 0:
        print(f'{hero["name"]} is at {hero["health"]}')
    elif enemy["health"] <= 0:
        print(f'{enemy["name"]} is at {enemy["health"]}')
    

attack(hercules, enemy1)
