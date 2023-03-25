import itertools as it

x = "abcd"

y =  "ahjfdce"

all_letters = []

for i in x:
    all_letters.append(i) if i not in all_letters else next

for j in y:
    all_letters.append(j) if j not in all_letters else next

print(list(it.combinations(all_letters, len(all_letters))))

#Im confused on what this challenges is asking for