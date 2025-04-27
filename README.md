# Fundamentos de Inteligência Artificial - TP1

Este projeto implementa o clássico jogo **15-puzzle** utilizando algoritmos de busca como **BFS**, **DFS** e **A\***.

## 📁 Estrutura do Projeto

- `board.py`: Implementa a lógica do tabuleiro (estado do jogo, movimentos, etc.).
- `agent.py`: Implementa a lógica do agente de busca.
- `heuristics.py`: Contém funções de heurísticas para o algoritmo A\*.
- `main.py`: Arquivo principal para execução do programa.
- `tests/`: Conjunto de testes unitários para garantir o funcionamento dos módulos.

## 📦 Dependências

- `numpy`

> As dependências necessárias estão listadas no arquivo `requirements.txt`.

## 🚀 Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o programa:

```bash
python TP1/main.py
```

Para gerar um puzzle aleatório (Pode ocorrer uma trava na memória na solução desses puzzles gerados):

```bash
python TP1/main.py --r
```

Para gerar um puzzle aleatório e simples com 10 movimentos padrão:

```bash
python TP1/main.py --s
```
Para gerar um puzzle aleatório e simples com n movimentos padrão

```bash
python TP1/main.py --s n
```



