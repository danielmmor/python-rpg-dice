# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def rolagem(msgRawAll):
    try:
        indx = 0
        for character in msgRawAll:
            if character.isdigit():
                break
            indx = indx + 1

        #msgRaw = msgRawAll.split('/r')
        #msgA = msgRaw[1].split('d')
        msgRaw = msgRawAll[indx : len(msgRawAll)]

        print(msgRaw)

        if msgRaw.find('d') != -1:
            msgA = msgRaw.split('d')
        else:
            msgA = msgRaw.split('D')
        
        print(msgRaw)

        if msgA[1].find('+') != -1:
            msgB = msgA[1].split('+')
            dadoMax = int(msgB[0])
            dadoAdd = int(msgB[1])
        else:
            dadoAdd = 0
            dadoMax = int(msgA[1])

        dadoNum = int(msgA[0])


        if dadoMax < 4:
            final = "O número de lados deve ser no mínimo 4!"
        elif dadoNum < 1:
            final = "O número de dados deve ser no mínimo 1!"
        else:
            params = {'num': dadoNum, 'max': dadoMax}
            page = requests.get('https://www.random.org/integers/?num=2&min=1&max=3&col=1&base=10&format=html&rnd=new', params=params)

            resultado = BeautifulSoup(page.content, 'html.parser')

            tudo = resultado.find(id="invisible")

            dadosRaw = tudo.find(class_="data").get_text()
            dados = dadosRaw.split('\n')
            del dados[-1]

            dados = list(map(int, dados))

            if dadoAdd != 0:
                final = str(dados)+"%2B"+str(dadoAdd)+", total "+str(sum(dados)+dadoAdd)
            else:
                if dadoNum == 1:
                    final = str(dados)
                else:
                    final = str(dados)+", total "+str(sum(dados))
        return final
    except:
        return "Não entendi"
