def main():
    linhas=(int(input("Digite o numero de linhas ")))
    colunas=(int(input("Digite o numero de colunas ")))
    somatorio=0
    matriz=[]
    for i in range(linhas):
        coluna=[]
        for j in range(colunas):
            coluna.append(int(input('Digite o numero da L'+str(i+1)+' C'+str(j+1)+' ')))
            somatorio=somatorio+coluna[j]
        matriz.append(coluna)
    for i in range(linhas):
        print matriz[i]
    print somatorio


if __name__=="__main__":
    main()
