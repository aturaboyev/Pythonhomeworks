txt = input("Enter a text: ")
ltxt = list(txt)
invalid = ["a","e","u","i","o","A","E","U","I","O"]
signal = 1
count = 0
for e in txt:
    if signal < 3:
        pass
    elif e in invalid:
        pass
    elif e == txt[-1]:
        pass
    else:
        ltxt.insert(count + 1, "_")
        count += 1
        invalid.append(e)
        signal=0
    signal += 1
    count += 1
    

print("".join(ltxt))

    


