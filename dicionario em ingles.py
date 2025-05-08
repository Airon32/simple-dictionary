print("---DICIONARIO EM INGLES---")
from time import sleep
dicionario = []
while True:
    escolha = int(input(
        "[1] - adicionar palavra ao dicionario\n"
        "[2] - ver dicionario completo\n"
        "[3] - filtrar pela letra\n"
        "[4] - filtrar pelo tipo da palvrar (adjetivo, verbo, subjuntivo etc)\n"
        "[5] - retirar palavra do dicionario\n"
        "[6] - buscar palavra pela tradução da palavra\n"
        "[7] - pesquisar palavra no dicionario\n"
        "[8] - sair\nEscolha:"
    ))



    if escolha == 1:
        print("\n-=-=- DIGITE A CARACTERISTICAS DA PALAVRA: -=-=-\n")
        palavra =  input("digite a palavra que voce deseja adicionar: ")
        letraInicial = input("digite a primeira letra da palavra: ")
        tipo = input("digite o tipo da palavra(adjetivo, verbo, subjuntivo etc): " )
        traducao = input("digite a tradução da palavra: ")
        siginificado = input("digite o significado dessa palavra: ")

        InfoPalavras = {
            "palavra" : palavra,
            "letraInicial" : letraInicial,
            "tipo" : tipo,
            "tradução" : traducao,
            "significado" : siginificado
        }

        dicionario.append(InfoPalavras)
        print(f"-=-=- A palavra =-{palavra}-= foi adicionada com sucesso -=-=-")
        sleep(1.5)

    

    elif escolha == 2:
        print("\n-=-=- VER DICIONÁRIO COMPLETO -=-=-\n")
        for p in sorted(dicionario, key=lambda x: x['palavra'].lower()):
            print(f"- {p['InfoPalavras']}")
        sleep(2)

        

    elif escolha == 3:
        print("\n-=-=- FILTRO PELA LETRA -=-=-\n")
        filtro = input(
            "digite a primeira letra da palavra"
        ).lower()
        for p in dicionario:
            if p['letraInicial'].lower() == filtro:
                print(f"- {p['InfoPalavras']}")


    
    elif escolha == 4:
        print("\n-=-=- FILTRO PELO TIPO -=-=-\n")
        filtro = input(
            "digite o tipo da palavra da palavra"
        ).lower()
        for p in dicionario:
            if p['tipo'].lower() == filtro:
                print(f"- {p['InfoPalavras']}")


            
    elif escolha == 5:
        print("\n-=-=- RETIRADOR DE PALAVRAS -=-=-\n")
        remover = input(
            "digite a palavra que voce deseja remover: "
            ).lower()
        removida = False
        for p in dicionario:
            if p['InfoPalavras'].lower() == remover:
                dicionario.remove(p)
                print("\n-=-=-palavra removida-=-=-")
                sleep(1.5)
                removida = True 
                break
        if not removida:
            print("palavra nao encontrada")


     
    elif escolha == 6:
        print("\n-=-=- FILTRO PELA TRADUÇÃO -=-=-\n")
        filtro = input(
            "\n digite a tradução da palavra desejada:\n "
        ).lower()
        for p in dicionario:
            if p['tradução'].lower() == filtro:
                print(f"- {p['InfoPalavras']}")
            


    elif escolha == 7:
        print("\n-=-=- FILTRO PELA PALAVRA -=-=-\n")
        busca = input(
            "\n digite a palavra desejada:\n"
        ).lower()
        for p in dicionario:
            if busca in p['palavra'].lower():
                print(f"- {p['InfoPalavras']}")


    
    elif escolha == 8:
        print("saindo do dicionario...")
        sleep(2)
        break
