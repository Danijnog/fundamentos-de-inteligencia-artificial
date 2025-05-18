# Fundamentos de Inteligência Artificial - TP1

## Descrição
### Tarefa 1
Este projeto implementa um Algoritmo Genético (AG) para resolver problemas de otimização contínua, especificamente para minimizar a função f(x1, ..., x10) = Σxᵢ² onde -5 ≤ xᵢ ≤ 5. O código inclui diferentes métodos de seleção, cruzamento e mutação adaptados para variáveis contínuas.
Funcionalidades Principais
Métodos de Seleção Implementados

    Seleção por Torneio: Seleciona o melhor indivíduo em um subconjunto aleatório

    Seleção por Roleta: Seleção probabilística proporcional ao fitness

Operadores Genéticos

    Cruzamento Aritmético: Combinação linear de pais para gerar filhos

    Mutação Gaussiana: Perturbação com distribuição normal para explorar o espaço de busca

### Requisitos
    Python 3.6+
    Bibliotecas: numpy, pandas, matplotlib

### Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o programa:

```bash
python tarefa1.py
```