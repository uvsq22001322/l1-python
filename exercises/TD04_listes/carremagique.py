import copy

carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
print(carre_mag)



#carre_pas_mag = copy.deepcopy(carre_mag)
carre_pas_mag = [list(l) for l in carre_mag]
carre_pas_mag[3][2] = 7
print(carre_pas_mag)

def afficheCarre(carre):
    for l in carre:
        print(l)
    print()

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)

def testLignesEgales(carre):

    somme = sum(carre_mag[0])
    for l in carre:
        if somme != sum(l):
            return -1
    return somme

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

def sommeColonne(carre, i):
    somme = 0
    for l in carre:
        somme += l[i]
    return somme

def testColonnesEgales(carre):
    somme = sommeColonne(carre, 0)
    for i in range(len(carre)):
        if sommeColonne(carre, i) != somme:
            return -1
    return somme

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))

print(carre_mag[0][0], carre_mag[1][1], carre_mag[2][2], carre_mag[3][3])



def testDiagonalesEgales(carre):
    somme_diag1 = 0
    for i in range(len(carre)):
        somme_diag1 = carre [i][i]
    somme_diag2 = 0
    for i in range(len(carre)):
        somme_diag2 = carre [len(carre) - i - 1][i]
    if somme_diag1 = somme_diag2:
        return somme_diag1
    else:
        return -1

print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag)) 



carre[i][i]
carre[len(carre- i)][i]
