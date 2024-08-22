from collections import Counter

S = input().upper()
counter = Counter(S)
max_freq = max(counter.values())

most_common = [char for char, freq in counter.items() if freq == max_freq]

if len(most_common) == 1:
    print(most_common[0])
else:
    print('?')