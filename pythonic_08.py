def lipat_ganda(x) :
    return x * 2

listku = [1,2,3,4,5]
listmu = []

for i in listku :
    listmu.append(lipat_ganda(i))

print(listku)
print(listmu)

listnya = list(map(lipat_ganda, listku))
print(listnya)