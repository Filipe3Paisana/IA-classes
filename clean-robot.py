import random
import time

# Definição do ambiente - grelha de 3x3 (pode ser expandida)
class Environment:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        # Cria uma grelha com células 'clean' ou 'dirty' aleatoriamente
        self.grid = [[random.choice(['clean', 'dirty']) for _ in range(cols)] for _ in range(rows)]

    def display_grid(self, agent_position=None):
        for i, row in enumerate(self.grid):
            row_str = ""
            for j, cell in enumerate(row):
                if agent_position and agent_position == [i, j]:
                    row_str += "A"  # Representa a posição do agente
                elif cell == 'clean':
                    row_str += "C"  # Célula limpa
                else:
                    row_str += "D"  # Célula suja
            print(row_str)
        print()

    def is_clean(self):
        # Verifica se todas as células estão limpas
        for row in self.grid:
            if 'dirty' in row:
                return False
        return True

# Definição do agente - o aspirador
class VacuumAgent:
    def __init__(self, env):
        self.env = env
        self.position = [0, 0]  # O agente começa no canto superior esquerdo

    def clean(self):
        # Se a célula atual estiver suja, o agente limpa
        row, col = self.position
        if self.env.grid[row][col] == 'dirty':
            self.env.grid[row][col] = 'clean'
            print(f"Limpando a célula em posição {self.position}")

    def move(self):
        # Move o agente para a próxima célula (linha por linha)
        row, col = self.position
        if col < self.env.cols - 1:
            self.position = [row, col + 1]  # Move para a direita
        elif row < self.env.rows - 1:
            self.position = [row + 1, 0]  # Move para a próxima linha, primeiro coluna
        else:
            print("Todas as células foram visitadas.")

# Inicializa o ambiente e o agente
env = Environment()
vacuum = VacuumAgent(env)

# Mostrar o estado inicial da grelha
print("Estado inicial da grelha:")
env.display_grid(agent_position=vacuum.position)

# Loop até a grelha estar completamente limpa
while not env.is_clean():
    vacuum.clean()  # O agente limpa a célula atual
    env.display_grid(agent_position=vacuum.position)  # Mostrar o estado atual da grelha com o agente
    vacuum.move()  # O agente move-se para a próxima célula
    time.sleep(1)

print("Todas as células estão limpas!")
