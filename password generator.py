import random
#By:Balaji 13s
# password generator

# Questions
q1 = ["what is your name", "What is your favourite colour" , "how old are you", "Which year were you born in", "You favourite food", "What is you best subject","where do you live",]
q2 = ["What do you own","The colour of this object","Rate this object from a scale of 1 - 10", "How expensice is this object","What currency did you buy this object in",]
q3 = ["How does it look", "Rate it from a scale of 1-10", "How expensive is it", "Would you kill someone to get it", "Would you smuggle someone out of the country",]
q4 = ["Do you own a pet y or n", "Is your friend awesome y or n", "What is your dogs name", "How old is your dog", "How long have you known you friend", "Is he better than you is everything","What is your dogs favourite snack"]

# password function


def passcheck(x):
    q = ["what is your name", "What is your favourite colour" , "how old are you", "Which year were you born in", "You favourite food", "What is you best subject","where do you live",]
    q2 = ["What do you own","The colour of this object","Rate this object from a scale of 1 - 10", "How expensice is this object","What currency did you buy this object in",]
    q3 = ["what does it look like", "Rate it from a scale of 1-10", "How expensive is it", "Would you kill someone to get it", "Would you smuggle someone out of the country",]
    q4 = ["Do you own a pet y or n", "Is your friend awesome y or n", "What is you pets name", "How old is your pet", "How long have you known you friend", "What is your friends name ","What is your pets favourite snack"]
    check = True
    while check == True:
        if x == 1:
            a = input((q[0],":"))
            if a == "ethan":
                print("go away ethan oiiiiiii")
            else:
                b = input((q[1],":",))
                b = b.upper()
                c = input((q[2],":",))
                d = input((q[3],":",))
                e = input((q[4],":",))
                d = input((q[5],":",))
                f = input((q[6],":",))
                list1 = [a,b,c,d,e,f,]
                for i in range(10):
                    random.shuffle(list1)
                    password = ''.join(list1)
                    print(password)
            
            check = False
        elif x == 2:
            a = input((q2[0],":",))
            b = input((q2[1],":",))
            c = input((q2[2],":",))
            d = input((q2[3],":",))
            e = input((q2[4],":",))
            for i in range(10):
                    random.shuffle(list1)
                    password = ''.join(list1)
                    print(password)
            check = False
        elif x == 3:
            a = input((q3[0],":",))
            b = input((q3[1],":",))
            c = input((q3[2],":",))
            d = input((q3[3],":",))
            if d == "y":
                d = "I.am.a.murderrer."
            elif d == "n":
                d = ""
            e = input((q3[4],":",))
            if e == "y" :
                e = "I.am.also.a.smuggler."
            elif e == "n":
                e = ""

            list1 = [a,b,c,d,e,]
            for i in range(10):
                    random.shuffle(list1)
                    password = ''.join(list1)
                    print(password)
            check = False
        elif x == 4:
            a = input((q4[0],":",))
            if a == "y":
                c = input((q4[2],":",))
                d = input((q4[3],":",))
                g = input((q4[6],":",))
                g = 'likes'+ g
                list1 = [c,d,g]
                for i in range(10):
                    random.shuffle(list1)
                    password = ''.join(list1)
                    print(password)
            elif a == 'n':
                b = input((q4[1],":",))
                if b == "n" :
                    print("some friend")
                    b = "useless"
                elif b == "y":
                    b = "great"
                e = input((q4[4],":",))
                d = input((q4[5],":",))

                list1 = [b,e,d]
                for i in range(10):
                    random.shuffle(list1)
                    password = ''.join(list1)
                    print(password)
            
            check = False
        
        elif x == 5:
            print("so fussy just pick the other options")

        else:
            print("stop being a foo and type a number")
    
    return list1


print("""
This is a memmorable and unique password generator,
This may take a few minutes to sit down and be a good user.
Answer all the questions, if you do not want to answer the question enter n""")

xoption = int(input("""
What would you like your password to be based upon:
1) Yourself
2) Something you own
3) Something you would like to own
4) A friend or pet
5) Others
"""))

h = passcheck(xoption)




        


