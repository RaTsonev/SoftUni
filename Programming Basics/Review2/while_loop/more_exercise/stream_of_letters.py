command = input()
ignored_symbols = ["!","@","`"," ","#","$","%","^","&","*","(",")","-","_","+","=","/","?","<",">","[","]","{","}"]
special = ["c","o","n"]
word = ""
whole_word = ""
while True:
    if command not in ignored_symbols:
        if command not in special:
            word = word + command
        else:
            special.remove(command)
        if len(special) == 0:
            special = ["c","o","n"]
            word = word + " "
            whole_word = whole_word + word
            word = ""
    command = input()
    if command == "End":
        print(whole_word)
        break




