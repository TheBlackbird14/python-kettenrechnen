import random 

def gen_rand_int(min, max):
    RandInt = random.randint(min, max)
    return RandInt

#generates random mathematical operator
def gen_rand_calc():
    PickNum = gen_rand_int(1, 4)
    if PickNum == 1:
        Calc = "+"
        return Calc
    elif PickNum == 2:
        Calc = "-"
        return Calc
    elif PickNum == 3:
        Calc = "*"
        return Calc
    else:
        Calc = "/"
        return Calc

Correct = bool(True)

Score = int(0)


while Correct == True:
# Defines parts of the calculation

    FirstNum = gen_rand_int(1, 100)
    Operator = gen_rand_calc()
    SecNum = gen_rand_int(2, 10)


#generate calculation partss
    OneNum = FirstNum
    Op = Operator
    TwoNum = SecNum


# funktion to stitch calculation parts
    def print_calc():
        Q = str(OneNum) + str(Op) + str(TwoNum)
        return Q


#calculate answer


    if Op == "+":
        CompCalc = OneNum + TwoNum
    elif Op == "-":
        CompCalc = OneNum - TwoNum
    elif Op == "*":
        CompCalc = OneNum * TwoNum
    else:
        CompCalc = OneNum / TwoNum

#checks if answer is valid
    valid = bool()

    if Op == "+":
        valid = True
    elif Op == "-" and CompCalc >= 0:
        valid = True
    elif Op == "*" and CompCalc <= 200:
        vali = True
    elif Op == "/" and OneNum % TwoNum == 0:
        valid

#print answer
    Question = print_calc()
    if valid == True:
        print(Question)
    else:
        continue

#take user answer
    UserCalc = int(input("="))

#check if answers match up
    
    if CompCalc == UserCalc:
        Correct = True
        print("Correct!")
        Score += 1
    else:
        Correct = False
        print("Nope - Game Over")
        break

print("Your Score: ", Score)

