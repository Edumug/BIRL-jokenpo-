import sys
import os

if len(sys.argv) < 2:
    print("Uso: python birl.py seu_arquivo.birl")
    sys.exit(1)

birl_file = sys.argv[1]
c_file = birl_file.replace('.birl', '.c')

with open(birl_file, 'r', encoding='utf-8') as f:
    codigo = f.read()

# Substituições de Entrada e Saída
codigo = codigo.replace('CE QUER VER ESSA PORRA?', 'printf')
codigo = codigo.replace('QUE QUE CE QUER MONSTRAO?', 'scanf')

# Ordem de tipos de dados (O maior precisa vir primeiro para não bugar o nome)
codigo = codigo.replace('TRAPEZIO DESCENDENTE', 'double')
codigo = codigo.replace('TRAPEZIO', 'float')
codigo = codigo.replace('BICEPS FRANGO', 'unsigned')
codigo = codigo.replace('FRANGO', 'char')
codigo = codigo.replace('MONSTRAO', 'long')
codigo = codigo.replace('MONSTRINHO', 'short')
codigo = codigo.replace('MONSTRO', 'int')

# Estruturas de controle e funções
codigo = codigo.replace('HORA DO SHOW', 'int main() { srand(time(NULL));')
codigo = codigo.replace('BORA CUMPADE', 'return')
codigo = codigo.replace('SAI FILHO DA PUTA;', 'break;')
codigo = codigo.replace('VAMO MONSTRO;', 'continue;')

codigo = codigo.replace('ELE QUE A GENTE QUER?', 'if')
codigo = codigo.replace('QUE NAO VAI DAR O QUE?', '} else if')
codigo = codigo.replace('NAO VAI DAR NAO', '} else')
codigo = codigo.replace('NEGATIVA BAMBAM', 'while')
codigo = codigo.replace('MAIS QUERO MAIS', 'for')
codigo = codigo.replace('BIRL', '}')

# Ajusta as aberturas de chaves automaticamente
lines = codigo.split('\n')
for i, line in enumerate(lines):
    if line.strip().startswith('if') or line.strip().startswith('} else if') or line.strip().startswith('while') or line.strip().startswith('for'):
        lines[i] = line + ' {'
    elif line.strip().startswith('} else'):
        lines[i] = line + ' {'

codigo = '\n'.join(lines)

with open(c_file, 'w', encoding='utf-8') as f:
    f.write('#include <stdio.h>\n#include <stdlib.h>\n#include <time.h>\n' + codigo)

# Compila e roda
os.system(f"gcc {c_file} -o programa.exe && .\\programa.exe")
