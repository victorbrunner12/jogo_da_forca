import os
import random
from player import Player

digitadas = []

class JogoForca:
    def get_letra(self):
        try:
            # Input pedindo uma letra para o jogador.
            letra = input("Digite uma letra: ")

            return letra
        except Exception as ex:
            print(ex)

    def verifica_caracteres(self, letra):
        try:
            # Verificando se o tamanho da variavel "letra" é maior que 1. Caso sim é pedido ao usuario que digite uma letra apenas.
            if len(letra) > 1:
                print("Digite apenas UMA letra.")
                return True

            return False
        except Exception as ex:
            print(ex)

    def verifica_letra(self, digitadas, letra, palavra_secreta):
        try:
            # Verifica se a letra digitada pelo jogador está na palavra final.
            if letra in palavra_secreta:
                # Se sim é retornado False.
                print(f'\nUhul. A letra "{letra}" EXISTE na palavra.')
                return False
            else:
                # Se não é feita uma verificação adicional para ver se a letra ja foi digitada.
                if letra in digitadas:
                    # Se sim, é exibida a mensagem de letra ja digitada e retornado False
                    print(f'A letra "{letra.upper()}" já foi digitada.')
                    return False
                else:
                    # Se não, é retornado True para retirada de 1 ponto de vida.
                    print(f'\nAff. A letra "{letra}" NÃO EXISTE na palavra.')
                    return True
        except Exception as ex:
            print(ex)

    def implementa_palavra(self, palavra_secreta):
        try:
            # Definindo variavel secreto_temporario para '' para implementação de novas letras.
            secreto_temporario = ''

            # Laço do tipo for para percorrer cada caractere da palavra final.
            for letra_secreta in palavra_secreta:
                # Verificando se a letra da palavra está na lista de letras digitadas.
                if letra_secreta in digitadas:
                    # Se sim, a letra é adicionada no secreto_temporario no seu devido índice.
                    secreto_temporario += letra_secreta
                else:
                    # Se não, é adicionado um asterisco para esconder a palavra.
                    secreto_temporario += '*'

            return secreto_temporario
        except Exception as ex:
            print(ex)

    def clear_console(self):
        try:
            # Utilizando a biblioteca os para sistema operacional e fazendo uma verificação
            # Se os.name == 'nt' ele limpa o console com o comando 'cls' senão 'clear'.
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as ex:
            print(ex)

    def forca_main(self):
        try:
            #Chamando função para pegar uma lista com dois indices com os nomes dos P1 e P2.
            nomes = Player().nome_players()

            #Chamando função para um dos Players escolhidos randomicamentes digitarem uma palavra.
            palavra_secreta = Player().get_palavra(random.choice(nomes))

            #Chamando função para calcular a vida do Player que tem que descobrir a palavra
            vidas = Player().vidas_player(palavra_secreta)

            secreto_temporario = ''

            #Chamando função que limpa o console para que o
            self.clear_console()

            print(f"Tamanho da palavra: {len(palavra_secreta)}\nVidas: {vidas}")

            while True:
                # Verificando se ainda restam vidas para o jogador.
                if vidas < 1:
                    print("===============================================================================")
                    print(f"Você perdeu!\nA palavra era: {palavra_secreta}\nVocê parou em: '{secreto_temporario.upper()}'")
                    print("===============================================================================")
                    break

                # Pegando a letra do jogador.
                letra = self.get_letra()

                # Verificando se o jogador digitou mais de 1 caractere.
                if self.verifica_caracteres(letra):
                    continue

                # Verificando se a letra contém na palavra ou se já foi digitada. (Se True então não existe a palvra.)
                if self.verifica_letra(digitadas, letra, palavra_secreta):
                    vidas -= 1
                    print(f'Tentativas restantes: {vidas}')

                # Adicionando a letra digitada na lista de letras.
                digitadas.append(letra)

                # Implementando a variavel com Asterisco (Se a letra não contém na palavra) ou Letras (Se a letra contém na palavra)
                secreto_temporario = self.implementa_palavra(palavra_secreta)

                # Verificando se a variavel está completa e igual a palavra.
                if secreto_temporario == palavra_secreta:
                    print("===============================================================================")
                    print(f"Parabéns você conseguiu completar!\nA palavra era '{palavra_secreta.upper()}'.")
                    print("===============================================================================")
                    break

                print(f"\nPalavra: {secreto_temporario}")

        except Exception as ex:
            print(ex)