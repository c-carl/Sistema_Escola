
# * Sistema Gerenciador de Escolas
# * Este é o arquivo principal do projeto, onde eu estou praticando algumas coisas que eu aprendi até agora em Python.

# ? Última atualização no código - 28/04/2026

# ! Correções:
    # * Finalizar a parte de editar a escola cadastrada. 
    # * Verificar se as outra funções estão corretas.  
    # * Atribuir a opção de encerrar o código no menu de interação. 

# ! Problemas que eu ainda tenho que resolver: 
    # * Depois de algum tempo consegui resolver o problema de cadastrar mais de uma escola.
    # * Atualmente meu foco é corrigir a classe de editar escola e de remover escola.

# ! O que eu estava errando.
    # * Depois de alguns dias tentando resolver o problema de cadastro de mais de uma escola, percebi que o que
    # * estava impedindo esse cadastro era o fato de a lista que eu havia criado estar sendo atualizada toda vez que
    # * a função de cadastro era chamada no código. Ou seja, dessa forma, o código até criava a lista e armazenava
    # * os valores, mas, a cada vez que essa função era chamada, ele recriava a lista vazia.

# ? Correção:
    # * Criei a lista dentro da classe, mas fora das funções. Dessa forma, ela podia ser acessada por todos os objetos e,
    # * mesmo ao chamar a função de cadastro, continuava com as informações, pois não era mais atualizada toda vez.

import time

class Cadastro_Escola:
    def __init__(self, nome_escola=None, endereco_escola=None, cep_escola=None):
        self.nome_escola = nome_escola
        self.endereco_escola = endereco_escola
        self.cep_escola = cep_escola

    lista_escola = []

    # ? Classe que cadastra as escolas.

    def cadastrar_escola(self):

        print("=" * 7," Cadastrar Escola no Sistema ", "=" * 7,"\n")
        self.nome_escola = input("School name: ")
        self.endereco_escola = input("School adress: ")
        self.cep_escola = input("School cep: ")
        print("=" * 45)

        escolas_cadastradas = [self.nome_escola, self.endereco_escola, self.cep_escola]
        self.lista_escola.append(escolas_cadastradas)

        if self.cadastro_vazio():
            print("\nNão foi possível cadastrar.\nAlguma informação foi preenchida errada, tente novamente.\n")
            return self.cadastrar_escola()
        
    # ? Classe que verifica se as linhas de cadastro foram preenchidas corretamente.

    def cadastro_vazio(self):
        return not self.nome_escola or not self.endereco_escola or not self.cep_escola


    # ! Essa classe vai ser o meu foco agora que consegui resolver o problema da função de cadastro
    def exibir_escola(self):

        if self.nome_escola is None and self.endereco_escola is None and self.cep_escola is None:
            print("Error!\nNenhuma escola cadastrada.\nVolte ao menu e realize o cadastro de uma escola.")
        
        print(f"======== Escolas Cadastradas no Sistema ========\n")
        for i in self.lista_escola:
            print("======== INFORMAÇÕES DA ESCOLA",[] ,"========")
            print("Name school: ", i[0])
            print("Adress school: ", i[1])
            print("cep school: ", i[2])

    
    def remover_escola(self):

        if self.nome_escola is None and self.endereco_escola is None and self.cep_escola is None:
            print("\nError!\nNenhuma escola cadastrada.\nVolte ao menu e realize o cadastro de uma escola.\nVoltando ao menu...")
            time.sleep(3)

        else:
            del self.nome_escola
            del self.endereco_escola
            del self.cep_escola

            print("Escola removida do sistema.\nRetornando ao menu... ")
            time.sleep(3)

    def editar_escola(self):

        if self.nome_escola is None and self.endereco_escola is None and self.cep_escola is None:
            print("\nError!\nNenhuma escola cadastrada.\nVolte ao menu e realize o cadastro de uma escola.\nVoltando ao menu...")
            time.sleep(3)
        else:
            print("=" * 7," Editar Escola do Sistema ", "=" * 7,"\n")
            


    # * Classe que vai exibir as opções do sistema
    # Atualmente essa é a classe mais correta do projeto kkk
    # Única que eu não fiquei quebrando a cabeça pra corrigir
    # mas ainda tenho que adicionar algumas opções nessa classe.
    def listar_opcoes(self):

        print("\nSeja bem-vindo!")
        print("O que você gostaria de fazer ?\n")
        print("1 - Cadastrar escola")
        print("2 - Listar escola(s)")
        print("3 - Remover escola")
        print("4 - Editar escola")
        print("5 - Encerrar sessão\n")

        resposta_usuario = int(input("Selecione uma opção: "))

        if resposta_usuario == 1:
            self.cadastrar_escola()
            return self.listar_opcoes()
        
        elif resposta_usuario == 2:
            self.exibir_escola()
            return self.listar_opcoes()

        elif resposta_usuario == 3:
            self.remover_escola()
            return self.listar_opcoes()

# Ainda não sei muito bem pra que serve isso, mas sei que é algo necessário
if __name__ == "__main__":

    teste = Cadastro_Escola()
    teste.listar_opcoes()