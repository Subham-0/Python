from art import logo,vs
import random

print(logo)

A = {
    "ram":{
        "occupation":"farmer",
        "from": "gujurat",
        "Followers":2345543,
    },
    "hari":{
        "occupation":"dancer",
        "from": "odisha",
        "Followers":5345543,
    },
    "gita":{
        "occupation":"housewife",
        "from": "bihar",
        "Followers":53485543,
    },
    "Budhia":{
        "occupation":"Programmer",
        "from": "odisha",
        "Followers":995345543,
    },
    "lalit":{
        "occupation":"worker",
        "from": "odisha",
        "Followers":535543,
    }
}

B = {
    "kohil":{
        "occupation":"criketer",
        "from": "pune",
        "Followers":9992345543,
    },
    "jastin":{
        "occupation":"singer",
        "from": "usa",
        "Followers":7865345543,
    },
    "modiji":{
        "occupation":"primister",
        "from": "bihar",
        "Followers":6753485543,
    },
    "messi":{
        "occupation":"footbal player",
        "from": "Africa",
        "Followers":9895345543,
    },
    "beargrill":{
        "occupation":"Explorer",
        "from": "cenia",
        "Followers":565535543,
    }
}

# print(p1)
# print(p2)
# print(A[p1]["occupation"])
# print(B[p2]["occupation"])
# print(A[p1]["from"])
# print(B[p2]["from"])
A_list = list(A)
B_list = list(B)
score = 0
def play():
    global score

    num1 = random.randint(0,4)
    num2 = random.randint(0,4)
    p1 = A_list[num1]
    p2 = B_list[num2]
    print(f"Compare A:{p1},{A[p1]['occupation']},from {A[p1]['from']}")
    print(vs)
    print(f"Against B:{p2},{B[p2]['occupation']},from {B[p2]['from']}")
    dis = input("Who has more followers? type 'A' or 'B' ")
    if dis == 'A' :
        if A[p1]["Followers"] > B[p2]["Followers"]:
            score=score+1
            print(f"you are wright. current score {score}")
            play()
        else:
            print(f"Sorry that's wrong. score is {score}")
    if dis == 'B' :
        if A[p1]["Followers"] < B[p2]["Followers"]:
            score = score+1
            print(f"you are wright. current score {score}")
            play()
        else:
            print(f"Sorry that's wrong score is {score}")
            
play()
    
                



        

    