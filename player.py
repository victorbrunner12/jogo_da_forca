import getpass

class Player:
    def nome_players(self):
        try:
            #Pegando uma lista com dois índices [0] => Player 1 | [1] => Player 2
            lista_nome = []

            lista_nome.append(input("Digite o nick do Player 1: "))
            lista_nome.append(input("Digite o nick do Player 2: "))

            return lista_nome
        except Exception as ex:
            print(ex)

    def get_palavra(self, nome_player):
        try:
            #Pegando uma palavra e utilizando a biblioteca 'getpass' para a palavra não ser mostrada no console do prompt de comando.
            palavra = getpass.getpass(prompt=f"\n{nome_player.upper()} digite uma palavra: ")

            return palavra
        except Exception as ex:
            print(ex)

    def vidas_player(self, palavra):
        try:
            # Calculando a vida do jogador de acordo com o tamanho da palavra mais 3 tentativas extras.
            vida = len(palavra) + 3

            return vida
        except Exception as ex:
            print(ex)