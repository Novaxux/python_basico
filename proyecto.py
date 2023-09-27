import random

User=input("Ingresa piedra, papel o tijera ")

User=User.strip()
User=User.capitalize
Options=('Piedra','Papel','Tijeras')
computer_Option = random.choice (Options)
if User!=Options:
    print('Ingresa una opción correcta')
else:
    if computer_Option==User:   
        print('Empate')
    elif computer_Option=='Piedra' and User=='Tijera':
        print('Computador gana')
    elif computer_Option=='Tijera' and User=='Piedra':
        print('User gana')

    elif computer_Option=='Papel' and User=='Tijera':
        print('Usuario gana')
    elif computer_Option=='Tijera' and User=='Piedra':
        print('User gana')

    elif computer_Option=='Papel' and User=='Piedra':
        print('Computador gana')
    elif computer_Option=='Piedra' and User=='Papel':
        print('User gana')
        