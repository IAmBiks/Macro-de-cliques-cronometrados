from time import sleep
from pyautogui import click
from os import system, name

vezes = 0          
contagem = 0

def clear():
    system('cls' if name == 'nt' else 'clear') or None

while(True):               #repetição do programa
    while(True):
        try:
            clear()                                      #redefinição de parametros
            vezes = int(input("Quantas vezes?\n"))
            contagem = 0
            escolhaTempo = int(input("Utliziar tempo prédefinido(30 segundos)? \n1-Sim \n2-Não\n"))   #escolha de cooldown
            if escolhaTempo == 1:
                tempo = cronometro = 30
            elif escolhaTempo == 2:
                tempo = cronometro = int(input("Quanto tem para delay?\n"))
            else:
                print("Valor desconhecido inserido \nreiniciando")
                sleep(5)
                break
            for x in range(vezes):                       #repetição de clicks(forma de menu)
                for y in range(tempo):                             #menu    
                    clear()
                    print("Tempo predefinido:", tempo)
                    print("aperte CTRL+C para reiniciar")
                    print("Click", vezes-contagem, "/", vezes)
                    print(cronometro)
                    sleep(1)
                    cronometro -= 1
                cronometro = tempo              
                click()
                contagem += 1
        except ValueError:           
            print("Valor incorreto inserido \reiniciando")
            sleep(2)
            break
        except KeyboardInterrupt:
            break

#ultima atualização: 20/09/24