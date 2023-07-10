listok = [2, 3, 4, 5, 'dad']
for i in range(len(listok) -1, -1, -1):
    if not isinstance(listok, str):
        del listok[i]
