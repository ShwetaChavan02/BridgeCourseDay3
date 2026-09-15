# prints numbers from 0 to 9 except 5
i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1