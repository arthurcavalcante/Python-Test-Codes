memoria = [5, 3, 3, 4]
programas = {'W': 1, 'Y': 4, 'X': 2, 'Z': 2}
alocacao = []

# ^^^^ criação das listas

def alocar_programa(programa, tamanho):
    for i in range(len(memoria)):
        if memoria[i] >= tamanho:
            alocacao.append((programa, i, tamanho))
            memoria[i] -= tamanho
            break

def imprimir_memoria():
    estado_memoria = []
    for i in range(len(memoria)):
        estado_memoria.append(f"Área {i+1}: {memoria[i]}K livre")
    for prog, idx, tam in alocacao:
        estado_memoria.append(f"Programa {prog} na Área {idx+1}: {tam}K")
    print("\n".join(estado_memoria))
    print("-" * 30)

for prog, tam in programas.items():
    alocar_programa(prog, tam)
    imprimir_memoria()
