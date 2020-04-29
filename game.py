"""
    Created on May 20,2019
   

    this file will maintain information about a specific game
    """
dict={}
class game:
    """
    this class contains two methods.

    report(...) : maintain info. after all game ends.
    printReport()  : This method will print summary of game
    """

    def report(game,word,status,badguess,missletter,finalscore):
        """

        This method maintains information about all games

        :param game: for game number
        :param word: current guess word
        :param status: status of current game,  success or gave up
        :param badguess: number of wrong guess word
        :param missletter: number of wrong guess letters
        :param finalscore: final score after guessing word or after gave up
        """
        listTemp=[word,status,badguess,missletter,finalscore]
        dict[game]=listTemp

    def printReport(self):
        """
        This method will print Final report about all game and total score when player choose to quit
        """
        total=0
        print("Game     Word     Status     Bad Guesses     Missed Letters      Score")
        print("----     ----     ------     -----------     --------------      -----")
        for i in dict.keys():
            list2=dict[i]
            print(i,"      ",list2[0],"   ",list2[1],"  ",list2[2],"             ",list2[3],"                 ",round(list2[4],2))
            total=total+list2[4]

        print("\nFinal Score: ",round(total,2))