import string
def minion_game(s):
    A = set(string.ascii_uppercase)
    B = {'A', 'E', 'I', 'O', 'U'}
    track = []
    Const = list(A - B)
    Vowel = list(B)
    Const.sort()
    Vowel.sort()
    print(Const, Vowel)
    Players = {'Stuart': 0, 'Kevin': 0}
    length = len(s)
    print(length)
    #for i
    for i in range(0, length+1):
        for j in range(i+1, length+1):
            letters = s[i:j]
            print(letters)
            if letters[0] in Vowel:
                if letters in track:
                    Players['Kevin'] = Players['Kevin'] + 1
                else:
                    track.append(letters)
                    Players['Kevin'] = Players['Kevin'] + 1
            else:
                if letters in track:
                    Players['Stuart'] = Players['Stuart'] + 1
                else:
                    track.append(letters)
                    Players['Stuart'] = Players['Stuart'] + 1
    print(Players)
    for k, v in Players.items():
        if Players['Stuart'] > Players['Kevin'] and k == 'Stuart':
            print(k, v)
            break
        elif Players['Stuart'] < Players['Kevin'] and k == 'Kevin':
            print(k, v)
            break
        else:
            print("Draw")
            break


s = input()
minion_game(s)