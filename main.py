import criacaoProjetos
import view


caminhoArquivo = input("Caminho do arquivo:  ")
nomeArquivo = input("Nome do arquivo:  ")
extencaoArquivo = input("Extenção do arquivo:  ")

arquivo = criacaoProjetos.manipulacaoArquivos.CriarArquivo(caminhoArquivo , nomeArquivo , extencaoArquivo)