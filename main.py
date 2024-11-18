with open ("text.txt", "r", encoding="utf-8")as file:
    v = file.read()
    e = v.replace("о", "a")
with open ("output.txt", "w", encoding="utf-8")as file:
    file.write(e)
