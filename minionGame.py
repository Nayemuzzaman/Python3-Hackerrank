def minion_game(string):
    # your code goes here
    vol = 'AEIOU'
    kevin = 0
    stuart = 0
    for i in range (len(s)):
        if s[i] in vol:
           kevin = kevin + (len(s) - i)
        else:
            stuart = stuart+(len(s) - i)
    if (kevin<stuart):
        print("Stuart", stuart)
    elif(stuart<kevin):
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)