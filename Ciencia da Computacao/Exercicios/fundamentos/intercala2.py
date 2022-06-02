def intercala2(L, inicio, meio, fim):
    T = [None] * (fim - inicio + 1)
    i = inicio
    j = meio + 1
    k = 0
    while i <= meio and j <= fim:
        if L[i] < L[j]:
            T[k] = L[i]
            i += 1
            k += 1
        else:
            T[k] = L[j]
            j += 1
            k += 1

    while i <= meio:
        T[k] = L[i]
        i += 1
        k += 1

    while j <= fim:
        T[k] = L[j]
        j += 1
        k += 1

    return T