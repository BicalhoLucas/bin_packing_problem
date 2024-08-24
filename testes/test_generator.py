"""
  Gera um conjunto de entradas aleatórias para o problema do Bin Packing.

  Entradas:
    num_entradas: Número de entradas a serem geradas.
    num_itens: Número de itens em cada entrada.
    capacidade_bin: Capacidade máxima de cada bin.
    max_tamanho_item: Tamanho máximo de um item.
    ? Nome do arquivo

  Returnos:
    Uma lista de listas, onde cada lista interna representa uma entrada.
    ? Um arquivo contendo as entradas geradas

"""

import random
import os

def gerar_entradas(num_entradas, num_itens, capacidade_bin, max_tamanho_item):
    entradas = []
    for _ in range(num_entradas):
        entrada = [random.randint(1, max_tamanho_item) for _ in range(num_itens)]
        entradas.append(entrada)
    return entradas

def salvar_entradas_em_arquivo(entradas, nome_arquivo):
    pasta_saida = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../testes/testes_gerados')
    caminho = os.path.join(pasta_saida, nome_arquivo) 
    with open(caminho, 'w') as arquivo:
        for entrada in entradas:
            linha = ' '.join(map(str, entrada))
            arquivo.write(linha + '\n')
    print("Arquivo salvo com sucesso em: " + str(caminho) + ".txt")

def main():
    # entradas pre definidas
    num_entradas = 10
    num_itens = 20
    capacidade_bin = 20
    max_tamanho_item = capacidade_bin

    opcao = int(input("  0 - Usar valores pré-definidos \n  1 - Informar valores\n   => "))

    if (opcao == 1):
        num_entradas = int(input("Numero de entradas: "))
        num_itens = int(input("Numero de itens: "))
        capacidade_bin = int(input("Capacidade do bin: "))
        max_tamanho_item = capacidade_bin

    entradas = gerar_entradas(num_entradas, num_itens, capacidade_bin, max_tamanho_item)
    for entrada in entradas:
        print(entrada)
        print("\n")

    opcao = input(" Salvar os testes em arquivo? S (Sim) | N (Não) \n => ")
    if (opcao == "S"):
        nome_arquivo = str(input("Nome do arquivo (com .txt): "))
        nome_arquivo = nome_arquivo
        salvar_entradas_em_arquivo(entradas, nome_arquivo)


if __name__ == "__main__":
    main()