"""
Created on May 20,2019


This file contains main method which holds main logic of the game
"""
from stringDatabase import *
from game import *
import random
class guess:
    """

    this class represent the game including menu
    """

    def main(self):
        """
        The exwcution of the program will start from this main method which represent the game itself

        """
        stringDatabase.IOop(1)
        word=""
        Word=""
        guess=""
        letter=""
        status=""
        badGuess=0
        contr=0
        noOfTime=0
        missLetter=0
        score=0
        cont=0
        flag=0
        listTemp = []
        listTemp1 = []
        # frequency :  store frequency of all letters in dictionary data structure
        frequency={'a':8.17,'b':1.49,'c':2.78,'d':4.25,'e':12.70,'f':2.23,'g':2.02,'h':6.09,'i':6.97,'j' : 0.15,'k':0.77,'l':4.03,'m':2.41,'n':6.75,'o':7.51,'p':1.93,'q':0.10,'r':5.99,'s':6.33,'t':9.06,'u':2.76,'v':0.98,'w':2.36,'x':0.15,'y':1.97,'z':0.07}
        dictionary={}
        try:
            for i in range(100):
                print("\n** The great guessing game **")
                print("        Game : ",i+1)
                f2=random.randint(0,4029)
                Word=list[f2]
                word="----"
                listTemp.clear()
                listTemp1.clear()
                noOfTime=0
                badGuess=0
                missLetter=0
                cont=0;
                score=0
                contr=0
                status=""
                for j in Word:
                    if j not in listTemp1:
                        listTemp1.append(j)
                    if j in dictionary:
                        dictionary[j] += 1
                    else:
                        dictionary[j] = 1
                while word!=Word:
                    print("Current Guess: ",word)
                    print("g = guess, t = tell me, l for a letter, and q to quit")
                    choice=input()

                    if choice=="g":
                        contr=contr+1
                        print("Enter word:")
                        guess=input()
                        if guess==Word:
                            status="Success"
                            for h in listTemp1:
                                score+=dictionary[h]*frequency[h]
                            print("Correct Guess : ",Word)
                            print("\nLets guess another Word...\n\n")
                            word=Word
                        else:
                            badGuess=badGuess+1
                            score-=score/10
                            #print(score)
                            print("Incorrect Guess...Try Again\n ")
                    elif choice=="t":
                        contr=contr+1
                        status="Gave up"
                        for h in listTemp1:
                            score-=dictionary[h]*frequency[h]
                        print("You Gave up\nCorrect word is : ",Word)
                        print("Lets guess another Word...\n")
                        word=Word
                    elif choice=="q":
                        print("Your Current Guess Word is : ",Word)
                        print("Thank you for playing 'The great guessing game'")
                        print("\nYour game summary:-\n")
                        flag=1
                        status="Gave up"
                        word=Word
                    elif choice=="l":
                        contr=contr+1
                        print("Enter a letter:");
                        letter=input()
                        if letter in dictionary:
                            if letter in listTemp:
                                print("You already uncover this letter...Try with nother letter or word.\n")
                            else :
                                for j in range(0,len(word)):
                                    if Word[j]==letter:
                                       word=word[:j]+letter+word[j+1:]

                                listTemp1.remove(letter)
                            #print(word)

                                if word==Word:
                                    status="Success"
                                    score+=dictionary[letter]*frequency[letter]
                                    print("Correct Guess : " , Word)
                                    print("Lets guess another Word...\n")
                                    word = Word

                                else :
                                    score+= dictionary[letter]*frequency[letter]
                                    cont +=  dictionary[letter]
                                    print("You found " , cont , " letters\n")
                                    listTemp.append(letter)

                        else:
                            missLetter=missLetter+1
                            noOfTime=noOfTime+1
                            print("Incorrect letter Guess....Try Again\n")
                if(noOfTime!=0):
                    score-=score/noOfTime

                dictionary.clear()

                if(contr!=0):
                    game.report(i+1,Word,status,badGuess,missLetter,score)

                if flag==1:
                    break
        except:
            print()

        game.printReport(1)

if __name__== "__main__":
    guess.main(1)