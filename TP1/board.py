import numpy as np
from collections import deque
import copy

ROWS = 4
COLS = 4


class Board:
    """
    Cria o tabuleiro para o jogo.
    """

    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.board = np.zeros(shape=(self.rows, self.cols), dtype=int)

    def init_board(self, initial_state=None, simple=False, num_moves=10):
        """
        Inicializa o tabuleiro.
        - Se `initial_state` for fornecido, usa-o como estado inicial.
        - Se `simple` for True, gera um tabuleiro simples com poucos movimentos.
        - Caso contrário, gera um tabuleiro aleatório.
        """
        goal_state = list(range(1, self.rows * self.cols)) + [0]

        if initial_state:
            # Usa o estado inicial fornecido
            self.board = np.array(initial_state).reshape(self.rows, self.cols)
            if not self.check_is_solvable():
                raise ValueError("O tabuleiro inicial não é solucionável.")
        elif simple:
            # Gera um tabuleiro simples
            while True:
                self.generate_simple_board(num_moves=num_moves)
                if not np.array_equal(self.board.flatten(), goal_state):
                    break
        else:
            # Gera um tabuleiro aleatório
            while True:
                numbers = list(range(0, self.rows * self.cols))
                np.random.shuffle(numbers)
                self.board = np.array(numbers).reshape(self.rows, self.cols)
                if not np.array_equal(self.board.flatten(), goal_state) and self.check_is_solvable():
                    break

    def check_is_solvable(self):
        """
        Checa se a configuração atual do tabuleiro possui solução.
        """
        inversions = 0
        flat_board = self.board.flatten()

        for i in range(len(flat_board)):
            for j in range(i + 1, len(flat_board)):
                if (
                    flat_board[i] != 0
                    and flat_board[j] != 0
                    and flat_board[i] > flat_board[j]
                ):
                    inversions += 1

        blank_tile_row, _ = np.where(self.board == 0)

        blank_tile_row_from_bottom = self.rows - blank_tile_row[0]
        # print("Index do número 0:", blank_tile_row_from_bottom)
        # print("Paridade:", inversions)

        if blank_tile_row_from_bottom % 2 != 0:
            return inversions % 2 == 0

        else:
            return inversions % 2 != 0

    def get_neighbors(self, state):
        """
        Gera todos os estados vizinhos possíveis ao mover o 0.
        """
        neighbors = []
        rows, cols = self.rows, self.cols
        state = np.array(state).reshape((rows, cols))
        row, col = np.where(state == 0)
        row, col = row[0], col[0]

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita

        for dr, dc in moves:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                new_state = copy.deepcopy(state)
                new_state[row, col], new_state[r, c] = (
                    new_state[r, c],
                    new_state[row, col],
                )
                neighbors.append(new_state.flatten().tolist())

        return neighbors
    
    def cost(self, path):
        """
        Calcula o custo acumulado (g(n)) com base no número de movimentos realizados.
        """
        return len(path)

    def generate_simple_board(self, num_moves=10):
        """
        Gera um tabuleiro solucionável aplicando um número limitado de movimentos
        a partir do estado objetivo.
        - `num_moves`: Número de movimentos aleatórios para embaralhar o tabuleiro.
        """
        # Começa com o estado objetivo
        goal_state = list(range(1, self.rows * self.cols)) + [0]
        self.board = np.array(goal_state).reshape(self.rows, self.cols)

        # Aplica movimentos aleatórios
        for _ in range(num_moves):
            neighbors = self.get_neighbors(self.board.flatten().tolist())
            self.board = np.array(neighbors[np.random.choice(len(neighbors))]).reshape(self.rows, self.cols)

        # Verifica se o tabuleiro gerado é solucionável
        if not self.check_is_solvable():
            print("Tabuleiro gerado não é solucionável. Gerando novamente.")
            self.generate_simple_board(num_moves=num_moves)
