with open ("text.txt", "r", encoding="utf-8")as file: #Открываем файл
    v = file.read() #Читаем его
    e = v.replace("о", "a") 
with open ("output.txt", "w", encoding="utf-8")as file:#Меняем о на а и переносим в другой файл
    file.write(e) #Выводим 
