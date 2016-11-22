def main():
    continua='s'
    vetor=[]
    vetor2x=[]
    i=0
    while not(continua=="N") :
        vetor.append(int(input('Digite um numero ')))
        vetor2x.append(vetor[i]*2)
        i=i+1
        continua=raw_input("Digite 'N' para sair ")
    print vetor
    print vetor2x

if __name__=="__main__":
    main()
