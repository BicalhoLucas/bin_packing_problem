from itertools import combinations
from itertools import permutations

def is_valid_partition(partition, bin_capacity):
    for bin_items in partition:
        if sum(bin_items) > bin_capacity:
            return False
    return True

def generate_partitions_combinations(items):
    partitions = []
    def generate(current_items):
        if not current_items:
            yield []
            return

        for i in range(1, len(current_items) + 1):
            for subset in combinations(current_items, i):
                remaining = list(current_items)
                for item in subset:
                    remaining.remove(item)
                for rest_partition in generate(remaining):
                    yield [list(subset)] + rest_partition

    for partition in generate(items):
        partitions.append(partition)
    return partitions

def brute_force_bin_packing_combinations(items, bin_capacity):
    best_solution = None
    min_bins = len(items) + 1

    partitions = generate_partitions_combinations(items)
    
    print("\nTodas as partições geradas com combinations:")
    for partition in partitions:
        print(partition)
    
    for partition in partitions:
        if is_valid_partition(partition, bin_capacity):
            if len(partition) < min_bins:
                best_solution = partition
                min_bins = len(partition)

    return best_solution, min_bins

# Testar com a nova instância
bin_capacity = 5
items = [2, 3, 4]

print("Usando Combinations:")
solution_combinations, num_bins_combinations = brute_force_bin_packing_combinations(items, bin_capacity)
print(f"\nMelhor solução usando combinations: {solution_combinations} com {num_bins_combinations} bins")
