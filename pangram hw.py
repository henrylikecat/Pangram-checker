def pangram(cat):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in cat.lower():
            return False
    return True
while True:

    string=input("ENTER YOUR STRING!!!: ")
    if(pangram(string)==True):
        print("YES!!!!!!!!!!!")
    else:
        print("NO!!!!!!!!!!!!")

