from os import read, remove


def CriarArquivo(caminhoArquivo, nomeArquivo):
    arquivo = open("{}\{}".format(caminhoArquivo,nomeArquivo), 'w')    
    arquivo.close()
    
    

def DeletarArquivo(caminhoArquivo, nomeArquivo):
    try:
        remove("{}\{}".format(caminhoArquivo, nomeArquivo))
    except:
        print("Arquivo {} inexistente!".format(nomeArquivo))
        print("Caso queira pode cria-lo usando a opção 1")
    
def ExibirConteudoArquivo(caminhoArquivo, nomeArquivo):
    try:
        arquivo = open("{}\{}".format(caminhoArquivo,nomeArquivo), 'r')    
        linhas = arquivo.readlines()
        print("*** Conteudo do arquivo {} ****".format(nomeArquivo))
        for linha in linhas:        
            print(linha)

        arquivo.close()

    except:
        print("Arquivo {} inexistente!".format(nomeArquivo))
        print("Caso queira pode cria-lo usando a opção 1")  