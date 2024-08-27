"""
    Implementação do algoritmo First Fit para o problema do Bin Packing (BP).

    Funcionamento:
        1º - Cria uma lista de pacotes vazios.
        2º Iteração item a item:
            * Percorre a lista de bins, começando do primeiro até último
            * Coloca o item no primeiro bin que tiver espaço que para o mesmo.
            * Se nenhum bin tiver espaço, então é criado um novo bin e o item é adicionado nele.
    
    Entradas:
        * items: Uma lista com os tamanhos dos itens a serem embalados.
        * bin_capacity: A capacidade máxima de cada pacote.

    Saida:
        * Uma lista de listas, onde cada lista interna representa
          um pacote tendo como valores o tamanho de cada item.

"""
from itertools import permutations
import os
import time

def first_fit(items, bin_capacity):
    bins = []
    for item in items:
        found_bin = False
        for bin in bins:
            if sum(bin) + item <= bin_capacity:
                bin.append(item)
                found_bin = True
                break
        if not found_bin:
            if item > bin_capacity:
                return []
            else:
                bins.append([item])

    return bins

def read_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Processar cada linha como uma entrada única
    entries = []
    for line in lines:
        data = list(map(float, line.strip().split()))
        bin_capacity = data[0]
        items = data[1:]
        entries.append((bin_capacity, items))

    return entries


def main():

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../testes/testes_gerados/teste.txt')
    entries = read_from_file(file_path)   

    # Criar um DataFrame para armazenar os resultados

    for index, (bin_capacity, items) in enumerate(entries):
        print(f"\nExecutando para a Entrada {index + 1}...")

        # Inicia a contagem de tempo de execução do código
        start_time = time.time()

        result = first_fit(items, bin_capacity)

        # Para a contagem antes de exibir a solução
        end_time = time.time()
        elapsed_time = end_time - start_time

        
        result = first_fit(items, bin_capacity)
        if result == []:
            print("Nenhuma solução válida encontrada para esta entrada.")
        else:
            for i, bin_items in enumerate(result, 1):
                print(f"Bin {i}: {bin_items}")

        print(f"Tempo gasto para encontrar a solução: {elapsed_time:.8f} segundos")
    
if __name__ == "__main__":
    main()