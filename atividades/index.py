# nome1 = input("Digite o primeiro nome: ")
# nome2 = input("Digite o segundo nome: ")
# nome3 = input("Digite o terceiro nome: ")

# def ordenar_1(nome1,nome2):
#     if nome1 < nome2:
#         return nome1
#     else:
#         return nome2
    
# def ordenar_2(nome1,nome2,nome3):
   
#     return ordenar_1(nome3,ordenar_1(nome1,nome2))

# resultado = ordenar_2(nome1,nome2,nome3)
# print(f"O nome que vem primeiro é {resultado}")

     
# def nome_unico(lista):

#     nomes = []

#     for nome in lista:

#         if nome not in nomes:
#             nomes.append(nome)


#     return nomes

# for x in range(10):
#     nome = input("digite um nome: ")
#     nomes = []

#     for nome in lista:

#         if nome not in nomes:
#             nomes.append(nome)

        
# print (nomes)


class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos.\n")

    def dormir(self):
        print("Dormindo ...ZzZzZZzZZzzzZZZzzzzZZ....\n")

def opcao(opcao):
    match opcao:
        case 1:
           return pessoa1.apresentar()
            
        case 2:
           return pessoa1.dormir()
        
        case 3:
           return print("Saindo ...")



nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))
pessoa1 = Pessoa(nome,idade)
op = 0
while(op != 3):
    op = int(input(f"Oque o {nome} irá fazer: \n1- se apresentar \n2-dormir\n3-sair\n\n"))

    opcao(op)



