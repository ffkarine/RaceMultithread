import time
import random
import threading
import os

# Cria uma classe de carro com os atributos necessários para ele
class Carro:
    carroId = 0
    carroIdEscuderia = 0
    escuderia = 0
    isTraining = False
    ciclo = 0
    nVoltas = 0
    voltasFaltantes = 0
    pista = 0
    tempoEntrada = 0
    tempoVolta = 0
    tempoTotal = 0

    def __init__(self, carroId, carroIdEscuderia, escuderia, pista, textOutput):
        self.carroId = carroId
        self.carroIdEscuderia = carroIdEscuderia
        self.escuderia = escuderia
        self.pista = pista
        self.pista.carros.append(self)
        self.textOutput = textOutput

    # Método principal -> Gerencia o treino do carro, controlando entradas, saídas e voltas completadas
    def Treina(self):
        # Enquanto não completar seu treino ou enquanto ainda houver tempo, fica em loop
        while(self.ciclo < 2 and time.time() < timeLimit):
            mutex.acquire()
            try:
                # Se o carro consegue entrar na pista, entra e inicia o treino
                if (self.pista.carrosTreinando < self.pista.maxCarros and self.escuderia.carrosNaPista == 0 and self.isTraining == False):
                    self.EntraNaPista()
            finally:
                mutex.release()
            
            # Se o carro iniciou o treino, mas o tempo acabou, sai da pista
            if (self.isTraining == True):
                if(time.time() >= timeLimit):
                    mutex.acquire()
                    try:
                        return self.SaiDaPista()
                    finally:
                        mutex.release()

                # Calcula o a volta inicial
                self.tempoVolta = random.randrange(1000, 1401)
                self.tempoVolta = self.tempoVolta*0.001
                self.tempoTotal += self.tempoVolta
                tempo = self.tempoVolta
                i = self.nVoltas

                # Fica em loop enquanto não terminar o ciclo de voltas (ou o tempo acabar)
                while i > 0:
                    time.sleep(tempo)

                    mutex.acquire()
                    try:
                        txt = "VOLTA COMPLETADA\nId: E{0}C{1}\nTempo da Volta: {2}s\nCiclo: {3}\nVolta Atual: {4} \nVoltas Faltantes: {5}\nCarros na Pista: {6}\nMomento da Volta: {7} s\n".format(
                            self.escuderia.escuderiaId, self.carroIdEscuderia, tempo, self.ciclo, self.nVoltas - i + 1, i-1, self.pista.carrosTreinando, time.time() - timeStart)
                        if(isTxtOutput):
                            self.textOutput.append(txt)
                        print(txt)                
                    finally:
                        mutex.release()

                    # Calcula o tempo das voltas n+1, com base na primeira volta, no formato:
                    # TempoDaVoltaN = TempoDaVoltaInicial +- (0.1)*TempoDaVoltaInicial
                    mx = self.tempoVolta*(0.01)*random.randrange(0, 11)*(pow(-1, random.randrange(0,2)))
                    tempo = self.tempoVolta + mx
                    # Se o tempo da nova volta estiver fora do range permitido, corrige o tempo
                    if(tempo < 1.0):
                        tempo = 1
                    elif(tempo > 1.4):
                        tempo = 1.4
                    i -= 1
                    self.voltasFaltantes = i
                    self.tempoTotal += tempo

                    # Se o tempo acabar, sai da pista
                    if(time.time() >= timeLimit):
                        mutex.acquire()
                        try:
                            return self.SaiDaPista()
                        finally:
                            mutex.release()

            # Após o término do ciclo, sai da pista
            if (self.isTraining == True):
                mutex.acquire()
                try:
                    self.SaiDaPista()
                finally:
                    mutex.release()
    
    # Método de entrada na pista
    def EntraNaPista(self):
        # Se o tempo acabou, não entra na pista            
        if(time.time() >= timeLimit):
            return

        # "Avisa" para a pista e para a escuderia que entrou na pista e que iniciou um ciclo de treinamento
        self.pista.carrosTreinando += 1
        self.escuderia.carrosNaPista +=1
        self.isTraining = True
        self.ciclo += 1

        # Calcula a quantidade de voltas para este ciclo (entre 4 e 12), e calcula o tempo de entrada (entre 100ms e 500ms)
        random.seed()
        self.nVoltas = random.randrange(4, 13)
        self.voltasFaltantes = self.nVoltas
        self.tempoEntrada = random.randrange(100, 501)
        self.tempoEntrada = self.tempoEntrada*0.001
        self.tempoTotal += self.tempoEntrada

        txt = "ENTRADA\nId: E{0}C{1}\nTempo de Entrada: {2}s\nCiclo: {3}\nVoltas Faltantes: {4}\nCarros na Pista: {5}\nMomento da Entrada: {6} s\n".format(
            self.escuderia.escuderiaId, self.carroIdEscuderia, self.tempoEntrada, self.ciclo, self.nVoltas, self.pista.carrosTreinando, time.time() - timeStart)
        if(isTxtOutput):
            self.textOutput.append(txt)
        time.sleep(self.tempoEntrada) 
        print(txt)

    # Método de saída da pista
    def SaiDaPista(self):
        txt = "SAÍDA\nId: E{0}C{1}\nCiclo: {2}\nÚltima Volta: {3}\nVoltas Faltantes: {4}\nCarros na Pista: {5}\nMomento da Saída: {6} s\n".format(
            self.escuderia.escuderiaId, self.carroIdEscuderia, self.ciclo, self.nVoltas - self.voltasFaltantes, self.voltasFaltantes, self.pista.carrosTreinando - 1, time.time() - timeStart)
        if(isTxtOutput):
            self.textOutput.append(txt)
        print(txt)
        
        # "Avisa" para a pista e para a escuderia que saiu da pista e não está mais treinando
        self.isTraining = False
        self.pista.carrosTreinando -= 1
        self.escuderia.carrosNaPista -= 1

# Cria uma classe de escuderia com os atributos necessários para ela      
class Escuderia:
    escuderiaId = 0
    carrosNaPista = 0

    def __init__(self, escuderiaId):
        self.escuderiaId = escuderiaId

# Cria uma classe de pista com os atributos necessários para ela
class Pista:
    maxCarros = 0
    carrosTreinando = 0
    maxEscuderias = 0
    maxCarrosPorEscuderia = 0
    carros = []

    def __init__(self, maxCarros, maxEscuderias, maxCarrosPorEscuderia):
        self.maxCarros = maxCarros
        self.maxEscuderias = maxEscuderias
        self.maxCarrosPorEscuderia = maxCarrosPorEscuderia

# main
if __name__ == "__main__":
    # Define os valores apresentados no problema e inicia variáveis necessárias
    maxCarros = 5
    maxEscuderias = 7
    maxCarrosPorEscuderia = 2
    carros = []
    escuderias  = []
    carroThreads = []

    # Cria o mutex
    mutex = threading.Lock()

    # Define se é para imprimir a saída em um arquivo de texto ou não
    isTxtOutput = True
    textOutput = []
    
    # Inicia a pista
    pista = Pista(maxCarros, maxEscuderias, maxCarrosPorEscuderia)

    # Inicia as X escuderias
    for c in range(maxEscuderias):
        escuderias.append(Escuderia(c))

    # Inicia os Y carros e cria as threads vinculadas aos seus respectivos carros
    for c in range(maxEscuderias * maxCarrosPorEscuderia):
        carros.append(Carro(c, c%2, escuderias[c%(maxEscuderias)], pista, textOutput))
        carroThreads.append(threading.Thread(target=carros[c].Treina, args=()))

    # Inicia a contagem de tempo conforme apresentado pelo problema
    timeStart = time.time()
    timeLimit = timeStart + 60

    # Inicia as Y threads
    for c in range(maxEscuderias * maxCarrosPorEscuderia):
        carroThreads[c].start()

    # Aguarda a conclusão das Y threads
    for c in range(maxEscuderias * maxCarrosPorEscuderia):
        carroThreads[c].join()

    # Se a opção de saída em arquivo de texto estiver ativa, gera o arquivo e escreve a saída nele
    if(isTxtOutput):
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        output = open("race.txt","w")
        
        # Trecho de informacoes opcionais:
        #######################################
        carrosIniciados = []
        carrosFinalizados = []
        carrosNaoIniciados = []

        for carro in carros:
            if (carro.ciclo == 2 and carro.voltasFaltantes == 0):
                carrosFinalizados.append(carro.carroId)
            if (carro.ciclo != 0):
                carrosIniciados.append(carro.carroId)
            if (carro.ciclo == 0):
                carrosNaoIniciados.append(carro.carroId)

        output.write("=============================================================================================================================\n")
        output.write("Os seguintes carros INICIARAM pelo menos UM ciclo de treinamento durante o período de treino:\n")
        if(len(carrosIniciados) == 0):
            output.write("#")
        else:
            for ini in carrosIniciados:
                output.write("E{0}C{1}\t".format(carros[ini].escuderia.escuderiaId, carros[ini].carroIdEscuderia))

        output.write("\n\nOs seguintes carros FINALIZARAM os DOIS ciclos de treinamento durante o período de treino:\n")
        if(len(carrosFinalizados) == 0):
            output.write("#")
        else:
            for fin in carrosFinalizados:
                output.write("E{0}C{1}\t".format(carros[fin].escuderia.escuderiaId, carros[fin].carroIdEscuderia))

        output.write("\n\nOs seguintes carros NÃO iniciaram NENHUM ciclo de treinamento durante o período de treino:\n")
        if(len(carrosNaoIniciados) == 0):
            output.write("#")
        else:
            for nin in carrosNaoIniciados:
                output.write("E{0}C{1}\t".format(carros[nin].escuderia.escuderiaId, carros[nin].carroIdEscuderia))

        output.write("\n=============================================================================================================================\n\n")
        #######################################

        for content in textOutput:
            output.write(content + "\n")
        output.close()
