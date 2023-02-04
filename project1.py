q1="""which planet has the most moons?
a)jupiter
b)saturn
c)mars
d)venus"""
q2="""what is the only contient with land in all four hemispheres?
a)asia
b)austrilia
c)afeica
d)antarctica"""
q3="""whats the national flower of japan?
a)lotus
b)lilly
c)cherry blossom
d)tulips"""
q4="""How many keys does a classic panio have?
a)100
b)46
c)20
d)88"""
q5="""what was the most watched series in netflix in 2019?
a)stranger things
b)wednesday
c)ginny&georgia
d0lucifer"""

questions={q1:"b",q2:"c",q3:"c",q4:"d",q5:"a"}


name=input("Hi what ur name")
print("Hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this ques (yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter your answer")
    if ans==questions[i]:
        print("Wow!you got one point")
        score=score+1
        print("your current score is :",score)
    else:
        print("Wrong answer, u lost 1 mark")
        score=-1
        print("ur currentscore:",score)
    flag2=input("do u want to quit?(yes\no)")
    if flag2=="yes":
        break
    print("ur total score:",score)
