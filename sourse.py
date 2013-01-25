#coding = utf-8

#You just need do this once,Considering of application performance
from random import randint
import time

print ("\t\tBien venido a un ejercicio de multiplicion")

DEF_REPETITION_TIMES = 5 #You can change it to 20 without any other code modified
DEF_TIME_LIMIT = 60 #seconds as unit

def DoOneTest():
    score = 0
    turn = 1
    beginTime = time.time()
    print "Testing Begin:"
    while turn <= DEF_REPETITION_TIMES:
        timelapse = time.time() - beginTime
        if(timelapse >= DEF_TIME_LIMIT):
            print "Time'over,You need to hurry up"
            break
        a = randint(1,5)
        b = randint(1,5)
        rightResult = a * b

        print "\t What is %d * %d" %(a,b)
        
        result = input("\t\t   =  ")
        if result == rightResult:
            score = score + 1
            print "\t  --Correct,  You have %d correct of %d" %(score,turn)
        else:
            print "\t  --Incorrect,  It is %d. You have %d correct of %d" %(rightResult,score,turn)
        turn = turn + 1

    r = raw_input("\n\nPlay again? Y o N?")
    if (r.upper() == "S" or r.upper() == "Y"):
        DoOneTest()
    else:
        return
        

DoOneTest()

#input("\n\nPress the enter Key to exit. ")

