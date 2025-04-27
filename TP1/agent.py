from collections import deque
import time
import numpy as np


class Agent:
    """
    Agente que resolve o problema do 15-puzzle usando BFS, DFS ou A*.
    """

    def __init__(self, board):
        """
        Inicializa o agente com um tabuleiro.
        """
        self.board = board

    def solve_with_bfs(self):
        """
        Resolve o problema usando o algoritmo BFS.
        """
        if not self.board.check_is_solvable():
            return {
                "solution": None,
                "nodes_expanded": 0,
                "moves": 0,
                "time": 0,
            }

        initial_state = self.board.board.flatten().tolist()
        goal_state = list(range(1, self.board.rows * self.board.cols)) + [0]

        queue = deque([(initial_state, [])])  # Fila para BFS: (estado, caminho)
        visited = set()
        nodes_expanded = 0

        start_time = time.time()

        while queue:
            current_state, path = queue.popleft()
            state_tuple = tuple(current_state)

            if state_tuple in visited:
                continue
            visited.add(state_tuple)
            nodes_expanded += 1

            if current_state == goal_state:
                end_time = time.time()
                return {
                    "solution": path + [current_state],
                    "nodes_expanded": nodes_expanded,
                    "moves": len(path),
                    "time": end_time - start_time,
                }

            for neighbors in self.board.get_neighbors(current_state):
                if tuple(neighbors) not in visited:
                    queue.append((neighbors, path + [current_state]))

        end_time = time.time()
        return {
            "solution": None,
            "nodes_expanded": nodes_expanded,
            "moves": 0,
            "time": end_time - start_time,
        }

    def solve_with_dfs(self, max_depth=20):
        """
        Resolve o problema usando o algoritmo DFS com limite de profundidade.
        """
        if not self.board.check_is_solvable():
            return {
                "solution": None,
                "nodes_expanded": 0,
                "moves": 0,
                "time": 0,
            }

        initial_state = self.board.board.flatten().tolist()
        goal_state = list(range(1, self.board.rows * self.board.cols)) + [0]

        stack = deque([(initial_state, [], 0)])  # Pilha para DFS: (estado, caminho, profundidade)
        visited = set()
        nodes_expanded = 0

        start_time = time.time()

        while stack:
            current_state, path, depth = stack.pop()
            state_tuple = tuple(current_state)

            if state_tuple in visited:
                continue
            visited.add(state_tuple)
            nodes_expanded += 1

            if current_state == goal_state:
                end_time = time.time()
                return {
                    "solution": path + [current_state],
                    "nodes_expanded": nodes_expanded,
                    "moves": len(path),
                    "time": end_time - start_time,
                }

            if depth >= max_depth:
                continue

            neighbors = self.board.get_neighbors(current_state)
            for neighbor in neighbors:
                if tuple(neighbor) not in visited:
                    stack.append((neighbor, path + [current_state], depth + 1))

        end_time = time.time()
        return {
            "solution": None,
            "nodes_expanded": nodes_expanded,
            "moves": 0,
            "time": end_time - start_time,
        }

    def solve_with_a_star(self, max_moves=50):
        """
        Resolve o problema usando o algoritmo A* com limite de movimentos.
        """
        if not self.board.check_is_solvable():
            return {
                "solution": None,
                "nodes_expanded": 0,
                "moves": 0,
                "time": 0,
                "limit_reached": False,
            }

        initial_state = self.board.board.flatten().tolist()
        goal_state = list(range(1, self.board.rows * self.board.cols)) + [0]

        priority_queue = deque([(0, 0, initial_state, [])])  # (f(n), g(n), estado, caminho)
        visited = set()
        nodes_expanded = 0

        start_time = time.time()

        while priority_queue:
            # Ordena a fila para simular uma fila de prioridade
            priority_queue = deque(sorted(priority_queue, key=lambda x: x[0]))
            _, g, current_state, path = priority_queue.popleft()
            state_tuple = tuple(current_state)

            if state_tuple in visited:
                continue
            visited.add(state_tuple)
            nodes_expanded += 1

            if len(path) > max_moves:
                end_time = time.time()
                return {
                    "solution": None,
                    "nodes_expanded": nodes_expanded,
                    "moves": len(path),
                    "time": end_time - start_time,
                    "limit_reached": True,
                }

            if current_state == goal_state:
                end_time = time.time()
                return {
                    "solution": path + [current_state],
                    "nodes_expanded": nodes_expanded,
                    "moves": len(path),
                    "time": end_time - start_time,
                    "limit_reached": False,
                }

            for neighbors in self.board.get_neighbors(current_state):
                if tuple(neighbors) not in visited:
                    h = self.board.misplaced_tiles(np.array(neighbors), np.array(goal_state))
                    g_new = self.board.cost(path + [current_state])
                    f = g_new + h
                    priority_queue.append((f, g_new, neighbors, path + [current_state]))

        end_time = time.time()
        return {
            "solution": None,
            "nodes_expanded": nodes_expanded,
            "moves": 0,
            "time": end_time - start_time,
            "limit_reached": False,
        }