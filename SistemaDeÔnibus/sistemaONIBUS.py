#Sistema Intermunipal de Ônibus!

viagens = [[0, 0, 0, 0]for _ in range(3)]

valor = [[0, 0, 0, 0]for _ in range(3)]

origens = ["Vitória", "Serra", "Cariacica"]
destinos = ["Vitória", "Serra", "Cariacica", "Vila Velha"]

while True:
    print("\n=-=-= SISTEMA DE ÔNIBUS INTERMUNICIPAL =-=-=")      #menu 
    print("1 - Cadastrar dados")
    print("2 - Listar todos os dados")
    print("3 - Buscar um dado")
    print("4 - Atualizar dados")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":        #cadastrar dados
        while True:
            print("\nCidades de origem:")
            for i in range(3):
                print(f"{i} - {origens[i]}")
            try:
                origem = int(input("\nDigite o número da cidade de origem: "))
                if origem not in range(len(origens)):
                    raise ValueError                        
            
            except ValueError:
                print(f'\nERRO! Insira um número entre 0 e {len(origens) - 1}')
                continue

            print("\nCidades de destino:")
            for j in range(4):
                print(f"{j} - {destinos[j]}")
            try:
                destino = int(input("\nDigite o número da cidade de destino: "))
                if destino not in range(len(destinos)):
                    raise ValueError                         
            
            except ValueError:
                print(f'\nERRO! Insira um número entre 0 e {len(destinos) - 1}')
                continue

            viagens[origem][destino] = int(input("\nQuantidade de passageiros: "))
            valor[origem][destino] = float(input('Valor total obtido (R$): '))
            print("\n>>> DADOS CADASTRADOS COM SUCESSO! <<<")

            continuar = input("\nDeseja cadastrar outro? (s/n): ").strip().lower()
            if continuar != 's':
                break

    elif opcao == '2':           #Listar todos os dados
        print('\n=-=- Viagens -=-=')
        print('Origem ->', '\t'.join(destinos))
        for i in range(3):
            linha = '\t'.join(str(viagens[i][j]) for j in range(4))
            print(f'{origens[i]} -> \t{linha}')

        print('\n=-=- Valor -=-=')
        print('Origem ->', '\t'.join(destinos))
        for i in range(3):
            linha = '\t'.join(f'{valor[i][j]:.2f}' for j in range(4))
            print(f'{origens[i]} -> \t{linha}')
        
    elif opcao == '3':             #buscar um dado
        for i in range(3):
            print(f'{i} - {origens[i]}')
        try:
            origem = int(input('Insira o número da cidade de origem: '))
            if origem not in range(len(origens)):
                raise ValueError
            
        except ValueError:
            print(f'\nERRO! Insira um número entre 0 e {len(origens) - 1}')
            continue

        for j in range(4):
            print(f'{j} - {destinos[j]}')
        try:
            destino = int(input('Insira o número da cidade de destino: '))
            if destino not in range(len(destinos)):
                raise ValueError
            
        except ValueError:
            print(f'\nERRO! Insira um número entre 0 e {len(destinos) - 1}')
            continue 

        a = viagens[origem][destino]
        b = valor[origem][destino]
        print(f'Quantidade de Viagem(s): {a}')
        print(f'Valor obtido (R$): {b:.2f}')

    elif opcao == '4':                 #atualizar dados
        while True:
            for i in range(3):
                print(f'{i} - {origens[i]}')
            try:
                origem = int(input('\nInsira o número da cidade de origem: '))
                if origem not in range(len(origens)):
                    raise ValueError
                
            except ValueError:
                print(f'\nERRO! Insira um número entre 0 e {len(origens) - 1}')
                continue

            for j in range(4):
                print(f'{j} - {destinos[j]}')
            try:
                destino = int(input('\nInsira o número da cidade de destino: '))
                if destino not in range(len(destinos)):
                    raise ValueError
                
            except ValueError:
                print(f'\nERRO! Insira um número entre 0 e {len(destinos) - 1}')
                continue

            viagens[origem][destino] = int(input('\nNovo número de passageiros: '))
            valor[origem][destino] = float(input('Novo valor total {R$}: '))
            print('\n>>> Dados Atualizados! <<<')

            continuar = input('\nDeseja atualizar outro dado? (s/n): ').strip().lower()
            if continuar != 's':
                break

    elif opcao == '0':              # fim  :)  <3
        print('\nPrograma Encerrado.')
        print('Até logo!')
        print('\n--> Integrantes: Miguel, Paulo Roberto, Pedro Antônio. <--\n')
        break

    else:
        print('\nOpção Inválida! Tente novamente!')
        