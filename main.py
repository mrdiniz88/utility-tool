from time import sleep
import speedtest
import os
from random import randint
from sys import argv, executable

from logo import Logo

verde = '\033[1;32m'; amarelo = '\033[1;33m'; vermelho = '\033[1;31m'; azul = '\033[1;34m'
    
def clear():
    os.system('cls||clear')

def restart():
    os.execl(executable, executable, *argv)

def opcoes():
    menu = f'''
[ 1 ] SpeedTest   
[ 2 ] PortScan
[ 3 ] Gerador de senha forte
[ 4 ] BruteForce (Ainda em teste)
[ 5 ] PING
'''
    print(menu)

Logo();sleep(3)
opcoes()

num = int(input('Escreva o numero desejado: '))

if num == 1:

    def getNetSpeed():
        speedTestHelper = speedtest.Speedtest()
        speedTestHelper.get_best_server()
        #Check download speed 
        download = speedTestHelper.download()
        #Check upload speed
        upload = speedTestHelper.upload()
        #generate shareable image
        url = speedTestHelper.results.share()
        #fetch result
        result = f'download: {download}, upload: {upload}, url: {url}'
        return result

    quant = int(input(f'{amarelo}Quanto testes deseja fazer? {amarelo}'));sleep(1.5);clear()
        

    for i in range(quant):
        print(f'{vermelho}Isso pode demorar um pouco...{vermelho}')
        print(f'{verde}-={verde}'*20)
        print(getNetSpeed())
        print(' ')
        print(f'{vermelho}[!]{vermelho}{amarelo} A URL .png PODE AUXILIAR NA VIZUALIZÇÃO DO RESULTADO {amarelo}{vermelho}[!]{vermelho}')
        print(f'{verde}-={verde}'*20)

elif num == 2:
    print('Para ultilizar nosso Portscan, saia do script e execute\n(chmod +x porscan.py)\n(./portscan.py <IP>) ex de IP: 192.168.1.1')

elif num == 3:
    chave = input("digite a base da sua senha (ex: coxinha)\n>>>   ")
    senha = ""

    for letra in chave:
    	if letra in "Aa":	
     	   senha = senha + "10"
    	elif letra in "Bb":
    		senha = senha + "11"
    	elif letra in "Cc":
    		senha = senha + "12"
    	elif letra in "Dd":
    		senha = senha + "13"
    	elif letra in "Ee":
    		senha =  senha + "14"
    	elif letra in "Ff":
    		senha = senha + "15"
    	elif letra in "Gg":
    		senha = senha + "16"
    	elif letra in "Rr":
    		senha = senha + "#"
    	elif letra in "Ss":
    		senha = senha + "%"
    	elif letra in "Hh":
    		senha = senha + "24"
    	elif letra in "Tt":
    		senha = senha + "7"
    	elif letra in "Jj":
    		senha = senha + "|"
    	else: senha = senha + letra
    print(senha)

elif num == 4:
    
    print('Isso vai demorar...')
    result = ""
    password = input("Senha: ")
    characters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'h', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'ç']
    '''0', '1', '2','3', '4', '5', '6', '7', '8', '9'''
    
    while(result != password):
        result=""
        for character in password:
            resultcharacters = characters[randint(0, 26)]
            result=str(result) + str(resultcharacters)
        print(result)
    print(f"Senha encontrada foi: {result}")

elif num == 5:

    ping = " ping "
    site = input(" IP address:  ")
    print("para parar de um Control-C")
    sleep(2)
    une = ping+site
    os.system(une)

else: 
    restart()