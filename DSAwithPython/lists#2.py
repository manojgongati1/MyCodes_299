heros=['spider man','thor','hulk','iron man','captain america']
#1
print('Length of the list',len(heros))

#2
heros.append("black panther")
print(heros)

#3
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)
#4
heros[1:3]=["doctor strange"]
print(heros)

#5
heros.sort()
print(heros)
