
# # * Sistema Gerenciador de Escolas

# # * Este é o aruqivo principal do projeto, onde eu estou realizando algumas coisas que eu aprendi até agora.

# #  * Estou com um pouco de dificuldade para cadastrar novas escolas, mas estou focado em resolver esse problema.

# #  * Atualmente meu foco é corrigir a classe de cadastro para conseguir cadastrar novas escolas.


# class Cadastro_Escola:
#     def __init__(self, nome_escola=None, endereco_escola=None, cep_escola=None):
#         self.nome_escola = nome_escola
#         self.endereco_escola = endereco_escola
#         self.cep_escola = cep_escola

#     # ! Classe que cadastra as escolas
#     # Tenho que modificar o código para conseguir adicionar mais de uma escola no sistema.
#     def cadastrar_escola(self):

#         print("======== Cadastrar Escola no Sistema ========\n")
#         self.nome_escola = input("School name: ")
#         self.endereco_escola = input("School adress: ")
#         self.cep_escola = input("School cep: ")

#     # * Classe que vai exibir as escolas cadastradas.
#     #  Essa classe não foi tão modificada, porque eu ainda não acertei a classe de cadastro
#     #  acredito que depois que eu conseguir resolver a classe de cadastro, alguns erros vão surgir aqui nessa classe.
#     def exibir_escola(self):

#         if self.nome_escola and self.endereco_escola and self.cep_escola == None:
#             print("Error!\nNenhuma escola cadastrada.\nVolte ao menu e realize o cadastro de uma escola.")

#         print("======== Escolas Cadastradas no Sistema ========\n")
#         print("Name school: ", self.escola_cadastrada)
#         print("Adress school: ", self.escola_cadastrada)
#         print("cep school: ", self.escola_cadastrada)

#         return self.listar_opcoes()

#     # * Classe que vai exibir as opções do sistema
#     # Atualmente essa é a classe mais correta do projeto kkk
#     # Única que eu não fiquei quebrando a cabeça pra corrigir
#     # mas ainda tenho que adicionar algumas opções nessa classe.
#     def listar_opcoes(self):

#         print("\nSeja bem-vindo!")
#         print("O que você gostaria de fazer ?\n")
#         print("1 - Cadastrar escola")
#         print("2 - Listar escola(s)")
#         print("3 - Remover escola")
#         print("4 - Editar escola")
#         print("5 - Encerrar sessão\n")

#         resposta_usuario = int(input("Selecione uma opção: "))

#         if resposta_usuario == 1:
#             self.cadastrar_escola()
#             return self.listar_opcoes()
        
#         elif resposta_usuario == 2:
#              self.exibir_escola()

# # Armazenando a classe em uma variavel e chamando a função para testar
# teste = Cadastro_Escola()
# teste.listar_opcoes()

def minha_funcao(x):
    return x * 2

lista_resultados = []

# Chamando a função e guardando o valor
valor = minha_funcao(5)
lista_resultados.append(valor)

print(lista_resultados)  # Saída: [10]
