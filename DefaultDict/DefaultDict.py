from collections import defaultdict
name = "Furqan is a boy"
d_dict = defaultdict(int)

for ch in name:
    d_dict[ch] += 1 

print(d_dict)
