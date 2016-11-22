def main():
    matriz=[]
    somatorio=0
    for i in range(4):
        linha=[]
        for j in range(4):
            linha.append(int(input("Digite um numero da Linha "+str(i+1)+" Coluna "+str(j+1)+" ")))
        somatorio=somatorio+linha[i]
        matriz.append(linha)
    for i in range(4):
        print matriz[i]
    print somatorio
if __name__=="__main__":
    main()
