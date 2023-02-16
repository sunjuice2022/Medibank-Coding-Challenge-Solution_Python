import os
from collections import Counter

# replace the path to the directory you want to search
directory = './' 
strings = []

for root, dir, files in os.walk(directory):
    for file in files:
        if not file.endswith('.txt'):
            continue
        filepath = os.path.join(root, file)
        with open(filepath, 'r') as f:
            contents = f.read()
            words = contents.lower().split()
            strings.extend(words)

counts = Counter(strings)

unique_strings = []
for s in set(strings):
    if counts[s] > 2:
       unique_strings.append(s)

unique_strings = sorted(unique_strings, key=lambda s: counts[s], reverse=True)

for s in unique_strings:
    print(s, counts[s])
