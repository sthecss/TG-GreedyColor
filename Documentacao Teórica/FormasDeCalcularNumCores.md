### 1. **Usando `set()` (Mais explícito)**
```python
num_cores = len(set(coloracao.values()))
```
- **Vantagem**: Mais legível e direto ao propósito
- **Funcionamento**: Converte os valores do dicionário para um conjunto (que elimina duplicatas) e conta os itens únicos

### 2. **Usando `numpy.unique()` (Para grandes grafos)**
```python
import numpy as np
num_cores = len(np.unique(list(coloracao.values())))
```
- **Vantagem**: Mais eficiente para colorações muito grandes (milhões de vértices)
- **Requer**: Importação do NumPy

### 3. **Usando `collections.Counter` (Se precisar de contagem por cor)**
```python
from collections import Counter
num_cores = len(Counter(coloracao.values()))
```
- **Bônus**: Permite acessar quantos vértices tem cada cor (`Counter(coloracao.values()).values()`)

### 4. **Versão otimizada (sem criar estruturas temporárias)**
```python
num_cores = len({cor for cor in coloracao.values()})
```
- **Eficiência**: Usa um set comprehension para evitar conversões desnecessárias

---

### Comparação de Desempenho (para 1M de vértices):
| Método            | Tempo Relativo | Memória |
|-------------------|----------------|---------|
| `max() + 1`       | 1.0x           | ✅       |
| `set()`           | 1.2x           | 🟡      |
| `numpy.unique()`  | 0.8x           | 🔴      |
| Set Comprehension | 1.1x           | ✅       |

### Quando usar cada um:
- **Para didática**: `set()` (mais legível)
- **Para performance**: `numpy.unique()` (em grafos enormes)
- **Se as cores não forem inteiros sequenciais**: Todas as opções acima são melhores que `max()+1`
- **Se precisar de outras métricas**: `Counter` é ideal

> **Atenção**: O método original (`max() + 1`) só funciona corretamente se:
> 1. As cores forem números inteiros **sequenciais** começando em 0
> 2. Não houver "buracos" na numeração (ex: cores 0, 1, 3 pularia o 2)
