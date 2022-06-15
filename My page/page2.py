# Hello World project 
# python3
# حدس زدن شماره انتخابی توسط کامپیوتر


from math import floor

def IsGuessTrue(Min, Max, Guess, NoGuess):
    if Min == Max :
        return
    else:
        OP = input ("Is your number (E)qual to ,(G)reater than or (L)ess than %i: " % Guess )
        if (OP == 'E' or OP == 'e'):
            print ("I found your number in %i Guess , it is %i"% (NoGuess, Guess))
            Max = Min
            IsGuessTrue(Min, Max, Guess, NoGuess)
        elif (OP == 'G' or OP == 'g'):
            Min = Guess
            Guess = floor ((Min + Max)/2)
            NoGuess += 1
            IsGuessTrue(Min, Max, Guess, NoGuess)
        elif (OP == 'L' or OP == 'l'):
            Max = Guess
            Guess = floor ((Min + Max)/2)
            NoGuess += 1
            IsGuessTrue(Min, Max, Guess, NoGuess)
        else: 
             print ("Error in data")
             

Numbers = [x for x in range (1001)]
Min = 1
Max = 1000
Guess = floor ((Min + Max)/2)
NoGuess = 1
IsGuessTrue(Min, Max, Guess, NoGuess)
