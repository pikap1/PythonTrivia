# OpenTDB by PixelTail Games LLC
# All data provided by the API and by this code is available under the Creative Commons Attribution-ShareAlike 4.0 International License
# The next code altered the original OpenTDB output for being used in python
# This code is free for Use for any purpose.
# The next lines of code were made only by Pikapi, Mail:Pikapi@homeplex.tk, Discord: pikapi...#5510,
# cota  simple:  '    toma todas las que quieras :D
from six.moves.urllib.request import urlopen
import random
import re
import ast


## FUNCTIONS HERE

# search for the question's category
def Category(response):
    res = re.search(('"category":"(.+?)","type"'),str(response))
    if res:
        found = res.group(1)
        return found

# search for the question's type (multiple choice/true or false)
def typefunc(response):
    res = re.search(('"type":"(.+?)","difficulty'),str(response))
    if res:
        found = res.group(1)
        return found

# search for the question's difficulty
def difficultyfunc(response):
    res = re.search(('"difficulty":"(.+?)","question":'),str(response))
    if res:
        found = res.group(1)
        return found

# search for the question
def questionfunc(response):
    res = re.search(('","question":"(.+?)","correct_answer"'),str(response))
    if res:
        found = res.group(1)
        return found

# search function
def goodfunc(response):
    res = re.search(('"correct_answer":"(.+?)","incorrect_a'),str(response))
    if res:
        found = res.group(1)
        return found

# search function
def badfunc1(response):
    res = re.search(('"incorrect_answers":(.+?)}'),str(response))
    if res:
        found = res.group(1)
        return found


## MAINLOOP HERE

restart="y"
while restart=="y":
    combo=0
    correct=0
    incorrect=0
    maxcombo=0
    loop=0

    while loop<=0:
        loop = int(input("How many questions do you want? "))

    repopt=["y","n"]


    for i in range(1,loop+1,1):
        import html
        link = "https://opentdb.com/api.php?amount=1"
        response = urlopen(link)
        raw = response.read()
        content = html.unescape(str(raw))
        
        category = Category(content)
        tipe = typefunc(content)
        difficulty = difficultyfunc(content)
        

        # print additional question/game info
        print("\n================================================================================\n")
        print("Correct Answers:",correct,"     Incorrect Answers:",incorrect)
        print("Current Streak:",combo,"     Question",i,"/",loop)
        print("Type:",tipe.title(),"    Category:",category.title(),"   Difficulty:" ,difficulty.title())


        question = questionfunc(content)
        print(question)
        good = goodfunc(content)
        bad1 = badfunc1(content)


        options = ast.literal_eval(bad1)
        options.append(good)
        for n in range(6):
            random.shuffle(options)

        a = options[0]
        b = options[1]
        if a==good:
         check = "a"
        elif b==good:
         check = "b"
        if tipe==("multiple"):
         c = options[2]
         d = options[3]
         if c==good:
          check = "c"
         elif d==good:
          check = "d"
        print("  a)",a)
        print("  b)",b)
        if tipe==("multiple"):
         print("  c)",c)
         print("  d)",d)
        respond = "false"
        while respond == "false":
         res = input("\nYour answer: ")
         res=res.lower()
         if tipe=="boolean":
          valids=["a","b"]
          if res in valids:
           if res==check:
            print("Correct answer!")
            correct=correct+1
            combo=combo+1
           else:
            print ("Wrong answer! The correct answer was", check.upper())
            combo = 0
            incorrect = incorrect+1
           respond="true"
          else:
           res=print("Invalid input, please type a valid answer (a, b): ")
         elif tipe==("multiple"):
          valids=["a","b","c","d"]
          if res in valids:
           if res==check:
            print("Correct answer!")
            correct=correct+1
            combo=combo+1
           else:
            print ("Wrong answer! The correct answer was", check.upper())
            combo = 0
            incorrect = incorrect+1
           respond="true"
          else:
           res=print("Invalid input, please type a valid answer (a, b, c, d):")
        if maxcombo<combo:
           maxcombo = combo

    print("\n================================================================================\n")
    print("FINAL RESULTS")
    print("Total Correct Answers:",correct,"     Total Incorrect Answers:",incorrect)
    print("Current Streak:",combo, "     Question ",i,"/",loop)
    print("Longest Streak:",maxcombo)
    reserror=1
    while reserror==1:
        restart=input("Play again? (y/n) ")
        if restart in repopt:
            reserror=0
            if restart ==repopt[0]:
             print("You decided to stay, now suffer.")
        else:
         print("Invalid answer, please repeat uwu")
