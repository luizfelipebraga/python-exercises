def intercala(L, M, tam1, tam2):
    T = [None] * (tam1 + tam2)
    i = 0
    j = 0
    k = 0
    while i < tam1 and j < tam2:
        if L[i] < M[j]:
            T[k] = L[i]
            i += 1
            k += 1
        else:
            T[k] = M[j]
            j += 1
            k += 1

    while i < tam1:
        T[k] = L[i]
        i += 1
        k += 1

    while j < tam2:
        T[k] = M[j]
        j += 1
        k += 1

    return T