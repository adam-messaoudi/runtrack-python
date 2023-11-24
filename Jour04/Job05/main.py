def modifier_liste(L):
    if len(L) >= 5:
        print(L)

        print(L[1])

        if len(L) > 4:
            L[3] = L[2] + L[4]
            print(L)
            
        print(L[-1])

L = [1, 2, 3, 4, 5]
modifier_liste(L)

