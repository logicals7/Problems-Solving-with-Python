input_ = input()
counts = dict()
for word in input_.lower().split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
for key, value in counts.items():
    print(key, value)