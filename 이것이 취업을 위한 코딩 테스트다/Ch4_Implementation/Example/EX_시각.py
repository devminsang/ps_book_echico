n = int(input())

c = 0

for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if '3' in f'{h} + {m} + {s}':
                c += 1
                
print(c)