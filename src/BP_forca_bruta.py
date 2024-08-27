from itertools import combinations
import os
import time

def is_valid_partition(partition, bin_capacity):
    for bin_items in partition:
        if sum(bin_items) > bin_capacity:
            return False
    return True

def generate_partitions(items):
    if not items:
        yield []
        return
    
    for i in range(1, len(items) + 1):
        for subset in combinations(items, i):
            remaining = list(items)
            for item in subset:
                remaining.remove(item)
            for rest_partition in generate_partitions(remaining):
                yield [list(subset)] + rest_partition

def brute_force_bin_packing(items, bin_capacity):
    best_solution = None
    min_bins = len(items) + 1

    for partition in generate_partitions(items):
        if is_valid_partition(partition, bin_capacity):
            if len(partition) < min_bins:
                best_solution = partition
                min_bins = len(partition)

    return best_solution, min_bins

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

    
    for index, (bin_capacity, items) in enumerate(entries):
        print(f"\nExecutando para a Entrada {index + 1}...")

        # Inicia a contagem de tempo de execução do código
        start_time = time.time()

        # Resolve o problema
        solution, num_bins = brute_force_bin_packing(items, bin_capacity)

        # Para a contagem antes de exibir a solução
        end_time = time.time()
        elapsed_time = end_time - start_time

        if solution:
            # Exibir a solução
            for i, bin_items in enumerate(solution, 1):
                print(f"Bin {i}: {bin_items}")
        else:
            print("Nenhuma solução válida encontrada para esta entrada.")

        # Exibir o tempo gasto
        print(f"Tempo gasto para encontrar a solução: {elapsed_time:.8f} segundos")
        

if __name__ == "__main__":
    main()
