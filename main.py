from time import sleep
import speedtest
import os
from random import randint

from logo import Logo

verde = '\033[1;32m'; amarelo = '\033[1;33m'; vermelho = '\033[1;31m'; azul = '\033[1;34m'
    
def clear():
    os.system('cls||clear')

def opcoes():
    menu = f'''
[ 1 ] SpeedTest   
[ 2 ] PortScan
[ 3 ] BruteForce
'''
    print(menu)

Logo()
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