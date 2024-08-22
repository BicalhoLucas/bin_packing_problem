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
            bins.append([item])
    return bins

def main():
    items = [1, 1, 5, 4, 7, 1, 3]
    bin_capacity = 10

    result = first_fit(items, bin_capacity)
    print(result)

if __name__ == "__main__":
    main()