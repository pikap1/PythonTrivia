#OpenTDB by PixelTail Games LLC
#All data provided by the API and by this code is available under the Creative Commons Attribution-ShareAlike 4.0 International License
#The next code altered the original OpenTDB output for being used in python
#This code is free for Use for any purpose.
#The next lines of code are made only by Pikapi, Mail:Pikapi@homeplex.tk, Discord: pikapi...#5510,
from six.moves.urllib.request import urlopen# cota  simple:  '    toma todas las que quieras :D
import random
import re
import ast
restart="y"
while restart=="y":
    combo=0
    correct=0
    incorrect=0
    maxcombo=0
    loop=0
    while loop<=0:
        loop= int(input("how much questions do you want"))
    repopt=["y","n"]
    for i in range(1,loop+1,1):
        import html
        link ="https://opentdb.com/api.php?amount=1"
        response = urlopen(link)
        raw = response.read()
        content = html.unescape(str(raw))


        def category(response):#search function
         res = re.search(('"category":"(.+?)","type"'),str(response))#function
         if res:
            found = res.group(1)
            return found
        category = category(content)


        def typefunc(response):#search function
         res = re.search(('"type":"(.+?)","difficulty'),str(response))#function
         if res:
            found = res.group(1)
            return found
        tipe= typefunc(content)


        def difficultyfunc(response):#search function
         res = re.search(('"difficulty":"(.+?)","question":'),str(response))#function
         if res:
            found = res.group(1)
            return found
        difficulty= difficultyfunc(content)
        print("correct awnsers:",correct,"     incorrect awnsers:",incorrect)
        print("combo:",combo, "     Question number",i,"/",loop)
        print("type:",tipe,"   category:",category,"   Difficulty:" ,difficulty)


        def questionfunc(response):#search function
         res = re.search(('","question":"(.+?)","correct_answer"'),str(response))#function
         if res:
            found = res.group(1)
            return found
        question = questionfunc(content)
        print(question)


        def goodfunc(response):#search function
         res = re.search(('"correct_answer":"(.+?)","incorrect_a'),str(response))#function
         if res:
            found = res.group(1)
            return found
        good = goodfunc(content)


        def badfunc1(response):
         res = re.search(('"incorrect_answers":(.+?)}'),str(response))#function
         if res:
            found = res.group(1)
            return found
        bad1= badfunc1(content)


        options =ast.literal_eval(bad1)
        options.append(good)
        random.shuffle(options)
        random.shuffle(options)
        random.shuffle(options)
        random.shuffle(options)
        random.shuffle(options)
        random.shuffle(options)
        random.shuffle(options)



        a =options[0]
        b =options[1]
        if a==good:
         check = "a"
        elif b==good:
         check="b"
        if tipe==("multiple"):
         c =options[2]
         d =options[3]
         if c==good:
          check="c"
         elif d==good:
          check="d"
        print("a)",a)
        print("b)",b)
        if tipe==("multiple"):
         print("c)",c)
         print("d)",d)
        respond = "false"
        while respond == "false":
         res = input("Awnser:")
         res=res.lower()
         if tipe=="boolean":
          valids=["a","b"]
          if res in valids:
           if res==check:
            print("Correct awnser!")
            correct=correct+1
            combo=combo+1
           else:
            print ("wrong awnser")
            combo = 0
            incorrect = incorrect+1
           respond="true"
          else:
           res=print("incorrect awnser, please put the awnser in abc format:")
         elif tipe==("multiple"):
          valids=["a","b","c","d"]
          if res in valids:
           if res==check:
            print("Correct awnser!")
            correct=correct+1
            combo=combo+1
           else:
            print ("wrong awnser")
            combo = 0
            incorrect = incorrect+1
           respond="true"
          else:
           res=print("incorrect awnser, please put the awnser in abc format:")
        if maxcombo<combo:
           maxcombo = combo

    print("FINAL RESULTS---")
    print("correct awnsers:",correct,"     incorrect awnsers:",incorrect)
    print("combo:",combo, "     Question number",i,"/",loop)
    print("max combo:",maxcombo)
    reserror=1
    while reserror==1:
        restart=input("play again? (y/n)")
        if restart in repopt:
            reserror=0
            if restart ==repopt[0]:
             print("you decided to stay, now suffer")
        else:
         print("invalid awnser, please repeat uwu")
