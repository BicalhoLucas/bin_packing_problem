# Caminhos das pastas
SRC_DIR = src
TEST_DIR = teste

# Arquivos Python
BRUTE_FORCE = $(SRC_DIR)/BP_forca_bruta.py
FIRST_FIT = $(SRC_DIR)/first_fit.py

# Alvo padrão
all: run_brute_force run_first_fit

# Executa o programa de força bruta
run_brute_force:
	@echo "Executando BP_força_bruta.py com o arquivo de teste..."
	python $(BRUTE_FORCE)

# Executa o programa heurístico
run_first_fit:
	@echo "Executando first_fit.py com o arquivo de teste..."
	python $(FIRST_FIT)

# Limpeza de arquivos compilados, se necessário
clean:
	@echo "Nada a limpar para projetos Python!"

# Alvo para rodar tudo
run_all: run_brute_force run_first_fit

.PHONY: all run_brute_force run_first_fit clean run_all