def main():
    alunos=15
    matriz=[]
    nome=0;prc1=1;prc2=2;m=3;prc3=4;mf=5;resultado=6
    msg='Nome       PRC1   PRC2  MD   PRC3   MF    Resultado'
    for i in range(alunos):
        linha=[]
        linha.append(raw_input('Digite o nome do aluno: '))
        linha.append(float(input('Digite a nota do PRC1 ')))
        linha.append(float(input('Digite a nota do PRC2 ')))
        linha.append((linha[prc1]+linha[prc2])/2)
        if (linha[m] < 7):
            linha.append(float(input('Digite a nota do PRC3 ')))
            linha.append((linha[prc3]+linha[prc2])/2)
        else:
            linha.append('-')
            linha.append(linha[m])
        if (linha[mf] < 6):
            linha.append('Reprovado')
        else:
            linha.append('Aprovado')
        matriz.append(linha)
    print(msg)
    for i in range(alunos):
        print('')
        print(str(matriz[i][nome])+"    "+str(matriz[i][prc1])+"   "+str(matriz[i][prc2])+"   "+str(matriz[i][m])+"    "+str(matriz[i][prc3])+"   "+str(matriz[i][mf])+"   "+str(matriz[i][resultado]))

if __name__=="__main__":
    main()
