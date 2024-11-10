# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

l_name1 = name1.lower()
l_name2 = name2.lower()
counter_true = l_name1.count(
    "t" and "r" and "u" and "e") + l_name2.count("t" and "r" and "u" and "e")
counter_love = l_name1.count(
    "l" and "o" and "v" and "e") + l_name2.count("l" and "o" and "v" and "e")

score_true = counter_true
score_love = counter_love

x = f"{score_true}{score_love}"
y = f"{score_true}{score_love}"
z = f"{score_true}{score_love}"

if 10 > score_true and score_love > 90:
    print(f'"Your score is {x}, yo go together like coke and mentos."')
elif 40 > score_true and score_love < 50:
    print(f'"Your score is {y}, you are alright together."')
else:
    print(f'"Your score is {z}."')

    print(score_true, score_love)
