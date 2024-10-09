import os

lista_de_compra = []

def AdicionarCompra():
    adicionar = input("\ndigite um item da sua compra para adicionar a lista: ")
    lista_de_compra.append(adicionar)
    print(f"\nfoi adicionado {adicionar} a lista")
    print(f"\nA lista atualizada é {lista_de_compra}")
    
    
def TirarDaLista():
    tirar = input("\ndigite o item que você deseja tirar da lista: ")
    lista_de_compra.remove(tirar)
    print(f"o item {tirar} foi removido da lista")
    print(f"\nA lista atualizada é {lista_de_compra}")
    
def VerLista():
    print("a lista de compra é: ", lista_de_compra)    
     
while True:
    print("-"*30, "LISTA DO EXTRA", "-"*30)
    print("1 - adicionar um item a lista")
    print("2 - tirar item da lista") 
    print("3 - ver lista atual")   
    print("4 - finalizar lista")
    escolha = (input("\ndigite a opção desejada: "))
    os.system('cls')


    if escolha == "1":
        AdicionarCompra()
        
    elif escolha == "2":
        TirarDaLista()
    
    elif escolha == "3":
        VerLista()
   
    elif escolha == "4":
        print("lista finalizada")
        VerLista()
        break