b=dict()
print("do you want to run the program?")
x=input()
while x=="yes":
    print("enter your word:")
    x=input()
    if x in b :
        print(b[x])
    elif x not in b:
        print("threr is not antonym of this word, add one")
        c=input()
        b[x]=c
    print("continue?")
    x=input()

