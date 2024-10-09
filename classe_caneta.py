class Caneta:
    def __init__(self, marca, cor, tamanho, tampada):
        self.marca = marca
        self.cor = cor
        self.tamanho = tamanho
        self.tampada = tampada    
    
    def rabiscar(self):
        if self.tampada is True:
            print("ta tampada irmão, não rabisca")
        else:
            print("<<<<Rabiscou>>>>")
            
    def tampar(self):
        self.tampada = True
        
    def destampada(self):
        self.tampada = False
        
    def exibir_valores(self):
        print(f"CANETA, marca: {self.marca}, cor da caneta: {self.cor}, tamanho da caneta: {self.tamanho}cm")
        

c1 = Caneta("bic", "preta", 5 ,False)
c1.exibir_valores()
c1.rabiscar()

c2 = Caneta("papermet", "azul", 3, True)
c2.exibir_valores()
c2.rabiscar()