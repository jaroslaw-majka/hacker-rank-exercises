# Link: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = "AEIOU"
    kevin_score, stuart_score = 0, 0
    for i in range(len(string)):
        score = len(string) - i
        if string[i] in vowels:
            kevin_score += score
        else:
            stuart_score += score
    if kevin_score > stuart_score:
        print("Kevin {}".format(kevin_score))
    elif kevin_score < stuart_score:
        print("Stuart {}".format(stuart_score))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)