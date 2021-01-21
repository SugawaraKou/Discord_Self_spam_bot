terminal = "-m message gifs -g 10"
print(terminal)
ter = terminal.split()
print(ter)

for i in ter:
    if i == "-m":
        m = True
        g = False
        s = False
        continue
    elif i == "-g":
        g = True
        m = False
        s = False
        continue
    elif i == "-s":
        s = True
        m = False
        g = False
        continue
    if m:
        print(i + " = -m")
    elif g:
        print(i + " = -g")
    elif s:
        print(i + " = -s")
