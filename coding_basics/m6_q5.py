""" Question 5: Hangman """
"""
Input: string
Output: interactive hangman game 
"""
def play_hangman(word):
    current_word = "_"*len(word)
    parts_left = 6
    guessed_letters = []
    turns = 0
    while (parts_left != 0 and "_" in current_word):
        print("Current word: ",current_word)
        print("Incorrect guesses left: ",parts_left)
        print("Letters guessed: ",",".join(guessed_letters))
        get = guess_letter(guessed_letters)
        if get in word:
            print("Good guess!")
            current_word = update_current_word(get,word,current_word)
        else:
            print("Wrong guess!")
            parts_left-=1
        turns+=1
        guessed_letters.append(get)
        print("-------------------------")
        
    print("Final word: ",current_word)
    if parts_left != 0:
        print("You win in ",turns," turns")
    else:
        print("You lose in ",turns," turns")

def guess_letter(guessed_letters):
    while(True):
        user_input = input("Which letter do you want to guess: ")
        if len(user_input) == 1:
            if user_input not in guessed_letters:
                return user_input
            else:
                print("You already guessed that letter! Pick a different letter.")
        else:
            print("Enter only one letter")

def update_current_word(get,word,current_word):
    for i in range(len(word)):
        if get == word[i]:
            current_word = current_word[:i] + get + current_word[i+1:]
    return current_word
  

if __name__ == '__main__':
    play_hangman("programming")


""" Sample Hangman game in Python terminal:

Current word: _ _ _ _ _ _ _ _ _ _ _ 
Incorrect guesses left: 6
Letters guessed: 
Which letter do you want to guess: e
Not quite...
-----
Current word: _ _ _ _ _ _ _ _ _ _ _ 
Incorrect guesses left: 5
Letters guessed: e
Which letter do you want to guess: o
Good guess!
-----
Current word: _ _ o _ _ _ _ _ _ _ _ 
Incorrect guesses left: 5
Letters guessed: e, o
Which letter do you want to guess: i
Good guess!
-----
Current word: _ _ o _ _ _ _ _ i _ _ 
Incorrect guesses left: 5
Letters guessed: e, o, i
Which letter do you want to guess: n
Good guess!
-----
Current word: _ _ o _ _ _ _ _ i n _ 
Incorrect guesses left: 5
Letters guessed: e, o, i, n
Which letter do you want to guess: g
Good guess!
-----
Current word: _ _ o g _ _ _ _ i n g 
Incorrect guesses left: 5
Letters guessed: e, o, i, n, g
Which letter do you want to guess: y
Not quite...
-----
Current word: _ _ o g _ _ _ _ i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y
Which letter do you want to guess: as
Please enter only one letter.
Which letter do you want to guess: a
Good guess!
-----
Current word: _ _ o g _ a _ _ i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y, a
Which letter do you want to guess: m
Good guess!
-----
Current word: _ _ o g _ a m m i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y, a, m
Which letter do you want to guess: i
You already guessed that letter! Pick a different letter.
Which letter do you want to guess: t
Not quite...
-----
Current word: _ _ o g _ a m m i n g 
Incorrect guesses left: 3
Letters guessed: e, o, i, n, g, y, a, m, t
Which letter do you want to guess: r
Good guess!
-----
Current word: _ r o g r a m m i n g 
Incorrect guesses left: 3
Letters guessed: e, o, i, n, g, y, a, m, t, r
Which letter do you want to guess: p
Good guess!
-----
Final word: p r o g r a m m i n g 
You won in 11 turns.
"""