def minion_game(string):
    length = len(s)
    vow = 0
    con = 0
    for i in range(length):
        if string[i] in 'AEIOU':
            vow = vow + (length - i)

        else:
            con = con + (length- i)
    if vow < con:
        print("Stuart",con)
    elif con < vow:
        print("Kevin",vow)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)