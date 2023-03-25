
x = 250

components = {
    "£1":None,
    "50p":None,
    "20p":None,
    "5p":None,
    "2p":None,
    "1p":None
}

combos = []

for i in range(3):
    components["£1"] = i
    for j in range(6):
        components["50p"] = j
        for k in range(13):
            components["20p"] = k
            for l in range(26):
                components["5p"] = l
                for m in range(51):
                    components["2p"] = m
                    for n in range(126):
                        components["1p"] = n
                        total = components["£1"] * 100 + components["50p"]*50 + components["20p"]*20 + components["5p"]*5 + components["2p"]*2 + components["1p"]
                        if total == x: combos.append("Combo Found")
print(len(combos))