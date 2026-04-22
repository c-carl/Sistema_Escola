
# * Sistema Gerenciador de Escolas
# * Este é o arquivo principal do projeto, onde eu estou praticando algumas coisas que eu aprendi até agora em Python.

# ? Última atualização no código - 21/04/2026
# ! Correções:
    # * Modificar o código pra armazenar mais de uma escola.
    # * Finalizar a parte de editar a escola cadastrada.
    # * Verificar se as outra funções estão corretas.

# ? Melhorias:
    # * Finalizar a parte de editar a escola cadastrada.
    # * Atribuir a opção de encerrar o código no menu de interação.

# ! Problemas que eu ainda tenho que resolver: 
    # * Estou com um pouco de dificuldade para cadastrar novas escolas, mas estou focado em resolver esse problema.
    # * Atualmente meu foco é corrigir a classe de cadastro para conseguir cadastrar novas escolas.

import time

class Cadastro_Escola:
    def __init__(self, nome_escola=None, endereco_escola=None, cep_escola=None):
        self.nome_escola = nome_escola
        self.endereco_escola = endereco_escola
        self.cep_escola = cep_escola

    # ! Estou tentando armazenar as informações do cadastro em uma lista
    # ! essa lista criada abaixo foi pra tentar armazenar...
    lista_escola = []

    # ! Classe que cadastra as escolas
    # Tenho que modificar o código para conseguir adicionar mais de uma escola no sistema.
    def cadastrar_escola(self):

        print("=" * 7," Cadastrar Escola no Sistema ", "=" * 7,"\n")
        self.nome_escola = input("School name: ")
        self.endereco_escola = input("School adress: ")
        self.cep_escola = input("School cep: ")
        print("=" * 45)

        if self.cadastro_vazio():
            print("\nNão foi possível cadastrar.\nAlguma informação foi preenchida errada, tente novamente.\n")
            return self.cadastrar_escola()

        # Ainda não sei como fazer pra adicionar várias escolas, mas uma hora eu consigo.
        # estou realizando alguns testes.

        # ! Aqui estou tentando realizar o cadastro de mais de uma escola
        # Cadastro_Escola.lista_escola.append(self.nome_escola)
        # Cadastro_Escola.lista_escola.append(self.endereco_escola)
        # Cadastro_Escola.lista_escola.append(self.cep_escola)
    
    def cadastro_vazio(self):
        return not self.nome_escola or not self.endereco_escola or not self.cep_escola

      #  Essa classe não foi tão modificada, porque eu ainda não acertei a classe de cadastro
    #  acredito que depois que eu conseguir resolver a classe de cadastro, alguns erros vão surgir aqui nessa classe.
    def exibir_escola(self):

        if self.nome_escola is None and self.endereco_escola is None and self.cep_escola is None:
            print("Error!\nNenhuma escola cadastrada.\nVolte ao menu e realize o cadastro de uma escola.")

        print("======== Escolas Cadastradas no Sistema ========\n")
        print("Name school: ", self.nome_escola)
        print("Adress school: ", self.endereco_escola)
        print("cep school: ", self.cep_escola)
    
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

# Armazenando a classe em uma variavel e chamando a função para testar
if __name__ == "__main__":

    teste = Cadastro_Escola()
    teste.listar_opcoes()