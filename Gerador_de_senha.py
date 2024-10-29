# GERADOR DE SENHA EM PYTHON
import random # importando ramdom para gerar a senha em forma aleatoria 
import string # importando string para a senha ter varias formas como numeros letras e pontuação

def gerar_senha(tamanho = 12): # criamos um método(função) para gerar a senha 
    caracteres = string.ascii_letters + string.digits #chamamos a biblioteca string; para a senha conter letras e numeros
    senha = ''.join(random.choice(caracteres) for i in range(tamanho)) # a variavel escolhe um caracter aleatorio repentindo 12 vezes e junta as letras com o join
    return senha

print("-"*30,"GERADOR DE SENHA","-"*30)
Numero_de_senhas = int(input("Digite quantas senhas voce deseja: ")) # Numero de senhas que o usuario deseja receber

for i in gerar_senha(tamanho = Numero_de_senhas): # Faz um loop em gerar senhas repetindo a função gerar senha 
    print("A SENHA GERADA FOI: ", gerar_senha()) # exibição da senha
