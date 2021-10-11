class manipulacaoArquivos:
    def CriarArquivo(caminhoArquivo, nomeArquivo, extencaoArquivo):
        arquivo = open("{}\{}.{}".format(caminhoArquivo,nomeArquivo, extencaoArquivo), 'w')
        return arquivo