import json

ip = "172.20.17.23" #str(input("Digite seu ip: \n")) #Recebendo o IP
listIp = ip.split(".") # Convertendo a string em lista separando por pontos
mask = 25 #int(input("Digite a mascara de rede: \n")) # Recebendo mascara de rede

#função que converta em binario
def converteBinario(numeroBinarios):
    for i in range(len(numeroBinarios)): # Laço para percorrer os index da lista
        numeroBinarios[i] = int(numeroBinarios[i]) # Transforma o item corrente em inteiro
        numeroBinarios[i] = bin(numeroBinarios[i]) # Transforma o item em um binário
        numeroBinarios[i] = numeroBinarios[i][2:] # Pega apenas o caracteres a partir do segundo até o final
    
    return numeroBinarios # Retorna a lista em binario em string

def verificaZeros(binarios):
    for i in range(len(binarios)): # Laço para percorrer os index da lista
        if len(binarios[i]) < 8: # Verifica se o item corrente é maior que 8
            num = 8 - len(binarios[i]) # Verifica quantos zeros vai precisar adicionar
            num = "0" * num # Atribui os zeros a variavel
            binarios[i] = num + binarios[i] # Atribui os zeros ao numero binario
        
    return binarios # Retorna a lista com os zeros preenchidos

def calculaMascara(ipBinario): #Recebe um ip em string
    rede = list(ipBinario) #Converte ele para lista
    mascara = 32 - int(mask) #Calculo para descobrir quantos 0 substituir nos octetos
    num = "0" * mascara # Atribuindo os zeros a uma variável
    '''
    rede.reverse()
    for i in range(len(num)):
        rede[i] = "0"
    
    rede.reverse()
    '''
    for i in range(len(num)): #Faz laço com o número de zeros, removendo o último item da lista
        rede.pop(-1)
    
    rede = "".join(rede) #Transfoma a lista  com o itens removidos em string
    rede = rede + num #Concatera os zeros no final da string
    
    return rede #Retorna uma um ip em string

def transformaDecimal(numeroBinario): #Recebe uma sitring de 1 octeto do número binario
    numDecimal = [] #Cria uma lista vazia
    pot = len(numeroBinario) - 1 # Calcula o numero de elementos -1 para a exponenciação

    for i in list(numeroBinario): #Transfoma a string binario em lista, e faz um laço para  percorrer cada item
        num = int(i) # Transforma o item corrente em inteiro
        num = num *  (2 ** pot) #Faz o calculo do primeiro numero para decimal
        pot -= 1 # Reduz 1 na potencia
        numDecimal.append(num) #Atribui o primeiro valor em uma lista
    
    return str(sum(numDecimal)) #Soma toda a lista para retornar o número decimal



listIp = converteBinario(listIp)
listIp = verificaZeros(listIp)
listIp = "".join(listIp)

resultadoMascara = calculaMascara(listIp)

Adecimal = "".join(resultadoMascara[0:8])
Bdecimal = "".join(resultadoMascara[8:16])
Cdecimal = "".join(resultadoMascara[16:24])
Ddecimal = "".join(resultadoMascara[24:32])

octetos = {
    
    'octeto1': transformaDecimal(Adecimal),
    'octeto2': transformaDecimal(Bdecimal),
    'octeto3': transformaDecimal(Cdecimal),
    'octeto4': transformaDecimal(Ddecimal),
    'mascara': mask,
    'gateway': "",
}

dados = json.dumps(octetos)

print(dados)
'''
print("Esse e o id da rede: {}.{}.{}.{}/{}".format(Adecimal,Bdecimal,Cdecimal,Ddecimal,mask))
print("Esse e o Default gateway: {}.{}.{}.{}".format(Adecimal,Bdecimal,Cdecimal,Ddecimal + 1))
'''
