import manipulacaoArquivos

while True:
    print("Opções:")
    print("1 - Criar arquivo")
    print("2 - Exibir conteudo do arquivo")
    print("3 - Deletar arquivo")
    print("4 - Sair")
    opcao = int(input("Escolha a opção desejada:  "))
    
    if (opcao == 1):
        caminhoArquivo = input("Caminho do arquivo:  ")
        nomeArquivo = input("Nome do arquivo:  ")
        manipulacaoArquivos.CriarArquivo(caminhoArquivo , nomeArquivo)

    elif (opcao == 2):
        caminhoArquivo = input("Caminho do arquivo:  ")
        nomeArquivo = input("Nome do arquivo:  ")        
        manipulacaoArquivos.ExibirConteudoArquivo(caminhoArquivo , nomeArquivo)
    elif (opcao == 3):
        caminhoArquivo = input("Caminho do arquivo:  ")
        nomeArquivo = input("Nome do arquivo:  ")        
        manipulacaoArquivos.DeletarArquivo(caminhoArquivo , nomeArquivo)

    elif (opcao == 4):
        break

    print("\n"*130)
