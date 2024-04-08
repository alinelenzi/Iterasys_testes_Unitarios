import csv


def read_csv(arquivo_csv):
    dados_csv = []
    try:
        
        with open(arquivo_csv, newline= '') as massa: #newline, caracter de final de linha
            tabela = csv.reader(massa, delimiter=',') #informando q o separador é a virgula 

            next(tabela) #para pular a uma linha, a primeira linha de cabeçalhho
            for linha in tabela:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Erro: Arquivo não encontrado: {arquivo_csv}\n')     #mensagem de erro de arquivo não encontrado
    except Exception as fail:                                       #qualquer erro não previsto     
        print(f'Falha imprevista: {fail}')                          #mensagem de erro q voltará do sistema
