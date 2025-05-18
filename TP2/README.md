# Fundamentos de Inteligência Artificial - TP1 e TP2

## Descrição

### Tarefa 1
Este projeto implementa um Algoritmo Genético (AG) para resolver problemas de otimização contínua, especificamente para minimizar a função f(x1, ..., x10) = Σxᵢ² onde -5 ≤ xᵢ ≤ 5. O código inclui diferentes métodos de seleção, cruzamento e mutação adaptados para variáveis contínuas.

#### Funcionalidades Principais

**Métodos de Seleção Implementados**
- Seleção por Torneio: Seleciona o melhor indivíduo em um subconjunto aleatório.
- Seleção por Roleta: Seleção probabilística proporcional ao fitness.

**Operadores Genéticos**
- Cruzamento Aritmético: Combinação linear de pais para gerar filhos.
- Mutação Gaussiana: Perturbação com distribuição normal para explorar o espaço de busca.

---

### Tarefa 2
Este projeto implementa um Algoritmo Genético (AG) para resolver o problema da mochila (Knapsack Problem), que é um problema clássico de otimização combinatória. O objetivo é maximizar o valor total dos itens selecionados sem exceder a capacidade da mochila.

#### Funcionalidades Principais

**Algoritmo Genético**
- Inicialização de uma população de soluções aleatórias.
- Avaliação de fitness com penalização para soluções que excedem a capacidade da mochila.
- Seleção de pais utilizando o método de Torneio.
- Operadores de cruzamento e mutação para gerar novas soluções.

**Detalhes Técnicos**
- **Método de Seleção**: Seleção por Torneio, onde o melhor indivíduo de um subconjunto aleatório é escolhido como pai.
- **Penalização**: Caso a soma dos pesos dos itens selecionados exceda a capacidade da mochila, o fitness é reduzido proporcionalmente ao excesso de peso multiplicado por um fator de penalidade (`PENALIDADE`).
- **Cruzamento**: Cruzamento de ponto único, onde os genes dos pais são trocados a partir de um ponto de corte aleatório.
- **Mutação**: Inversão de genes (de 0 para 1 ou de 1 para 0) com uma probabilidade definida pela taxa de mutação.

**Saída Organizada**
- Exibição de uma tabela com a capacidade da mochila, o valor total da solução e o peso total.
- Exibição de um grid detalhado com os itens, indicando:
  - Se o item foi selecionado.
  - O peso e o valor de cada item.

---

### Requisitos
- Python 3.6+
- Bibliotecas: numpy, pandas, matplotlib, tabulate

### Como Executar

#### Tarefa 1
1. Instale as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o programa:
   ```bash
   python tarefa1.py
   ```

#### Tarefa 2
1. Instale as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o programa:
   ```bash
   python tarefa2.py
   ```

---

### Exemplo de Saída da Tarefa 2
**Tabela Principal**
```
+---------------------------+-------+
| Descrição                | Valor |
+===========================+=======+
| Capacidade da mochila    |    50 |
+---------------------------+-------+
| Valor total              |   210 |
+---------------------------+-------+
| Peso total               |    30 |
+---------------------------+-------+
```

**Grid de Itens**
```
Itens:
+--------+--------------+------+-------+
| Item   | Status       | Peso | Valor |
+========+==============+======+=======+
| Item 1 | Selecionado  |   10 |    60 |
+--------+--------------+------+-------+
| Item 2 | Não selecionado |   20 |   100 |
+--------+--------------+------+-------+
| Item 3 | Selecionado  |   15 |   120 |
+--------+--------------+------+-------+
| Item 4 | Selecionado  |    5 |    30 |
+--------+--------------+------+-------+
```