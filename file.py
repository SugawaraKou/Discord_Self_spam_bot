terminal = "-m message gifs -g -q -t 10"
print(terminal)
ter = terminal.split()
print(ter)

"""
    -m + сообщение
    -g будут гифки
    -t + время до отправки
    -q количество
"""
stroka = ""
ti = 0
qu = 1
g = False

for i in ter:
    if i == "-m":
        m = True
        t = False
        q = False
        continue
    elif i == "-g":
        g = True
        continue
    elif i == "-t":
        t = True
        m = False
        q = False
        continue
    elif i == "-q":
        q = True
        t = False
        m = False
        continue

    if m:
        stroka += i + " "
    elif t:
        ti += int(i)
    elif q:
        qu += int(i)

print(stroka)
print(g)
print(ti)
print(qu)

# for i in range(0, int(text)):
#     test = ''.join(choice(ascii_uppercase) for i in range(10))  # рандомная гифка из файла
#     await ctx.send(embed=discord.Embed(description=test + " " + text))  # выделленный техт
#     lines = open('gifer').read().splitlines()
#     myline = random.choice(lines)
#     print(myline)
#     await ctx.send(embed=discord.Embed().set_image(url=myline))  # Скинуть gif по url
#     await ctx.send(file=discord.File('giphy.gif'))  # Локально скинуть gif
