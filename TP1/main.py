from board import Board
from agent import Agent
from tabulate import tabulate  # Biblioteca para formatar a saída como tabela


def initialize_board(use_random):
    """
    Inicializa o tabuleiro.
    - Se `use_random` for True, gera um tabuleiro aleatório.
    - Caso contrário, usa um tabuleiro fixo para testes.
    """
    board = Board()
    if use_random:
        board.init_board()  # Gera um tabuleiro aleatório
    else:
        # Define um tabuleiro fixo para testes
        initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12]
        board.init_board(initial_state=initial_state)
    # Verifica se o tabuleiro é solucionável
    if not board.check_is_solvable():
        print("Tabuleiro não solucionável. Gerando um novo tabuleiro.")
        board.init_board()  # Gera um novo tabuleiro se o atual não for solucionável
    else:
        print("Tabuleiro inicial gerado com sucesso.")
    return board


def display_results(results):
    """
    Exibe os resultados em formato de tabela.
    """
    headers = ["Método", "Nós Expandidos", "Movimentos", "Tempo"]
    print("\nRelatório Final:")
    print(tabulate(results, headers=headers, tablefmt="grid"))


def solve_and_collect_results(agent, max_moves=50):
    """
    Resolve o problema usando diferentes algoritmos e coleta os resultados.
    """
    results = []

    # Resolver com A*
    print("\nSolução usando A* encontrada")
    a_star_report = agent.solve_with_a_star(max_moves=max_moves)
    if a_star_report["solution"]:
        # print("Caminho da solução encontrado com A*:")
        # for step in a_star_report["solution"]:
        #     print(step)
        results.append([
            "A*", a_star_report["nodes_expanded"], a_star_report["moves"], f"{a_star_report['time']:.4f} segundos"
        ])
    else:
        if a_star_report["limit_reached"]:
            print("O limite de movimentos foi atingido antes de encontrar a solução.")
        else:
            print("Nenhuma solução encontrada.")
        results.append(["A*", "N/A", "N/A", "N/A"])

    # Resolver com BFS
    print("\nSolução usando BFS encontrada")
    bfs_report = agent.solve_with_bfs()
    if bfs_report["solution"]:
        # print("Caminho da solução encontrado com BFS:")
        # for step in bfs_report["solution"]:
        #     print(step)
        results.append([
            "BFS", bfs_report["nodes_expanded"], bfs_report["moves"], f"{bfs_report['time']:.4f} segundos"
        ])
    else:
        print("Nenhuma solução encontrada com BFS.")
        results.append(["BFS", "N/A", "N/A", "N/A"])

    # Resolver com DFS
    print("\nSolução usando DFS encontrada")
    dfs_report = agent.solve_with_dfs()
    if dfs_report["solution"]:
        # print("Caminho da solução encontrado com DFS:")
        # for step in dfs_report["solution"]:
        #     print(step)
        results.append([
            "DFS", dfs_report["nodes_expanded"], dfs_report["moves"], f"{dfs_report['time']:.4f} segundos"
        ])
    else:
        print("Nenhuma solução encontrada com DFS.")
        results.append(["DFS", "N/A", "N/A", "N/A"])

    return results


if __name__ == "__main__":
    import argparse

    # Configuração de argumentos
    parser = argparse.ArgumentParser(description="15-Puzzle Solver")
    parser.add_argument("--r", action="store_true", help="Usar tabuleiro aleatório")
    parser.add_argument("--s", type=int, nargs="?", const=10, help="Gerar um tabuleiro simples com um número de movimentos (padrão: 10)")
    args = parser.parse_args()

    # Lista para armazenar os resultados de execução
    all_results = []

    # Gera e resolve 5 tabuleiros
    generated_boards = set()  # Para garantir que os tabuleiros sejam únicos
    for i in range(5):
        print(f"\n=== Tabuleiro {i + 1} ===")
        
        # Inicializa o tabuleiro
        board = Board()
        while True:
            if args.simple is not None:
                board.init_board(simple=True, num_moves=args.simple)
            elif args.random:
                board.init_board()  # Gera um tabuleiro aleatório
            else:
                # Define um tabuleiro fixo para testes
                initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 12]
                board.init_board(initial_state=initial_state)

            # Garante que o tabuleiro seja único
            board_tuple = tuple(board.board.flatten())
            if board_tuple not in generated_boards:
                generated_boards.add(board_tuple)
                break

        # Exibe a configuração inicial do tabuleiro
        print("Configuração inicial do tabuleiro:")
        print(board.board)

        # Inicializa o agente
        agent = Agent(board)

        # Resolve o problema e coleta os resultados
        results = solve_and_collect_results(agent, max_moves=100)
        all_results.append(results)

    # Exibe o relatório consolidado
    print("\n=== Relatório Consolidado ===")
    for i, results in enumerate(all_results):
        print(f"\nTabuleiro {i + 1}:")
        display_results(results)