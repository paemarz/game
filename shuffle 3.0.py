import random 

print("WELCOME TO SHUFFLE ME 3.0! ")
print("i have  word, can you guess it?")
print("enter quit to quit game")


def pick_words():
    with open("words.txt") as word_box:
        correct_words = set(word_box.read().split())
    return correct_words
    
    
#points sequence
point = 0

english_words = pick_words()
          

print(english_words)


while True:
    word_pick = input("enter an english word").lower()
    english_word = random.choice(english_words)
    if word_pick == english_word.lower():
        point += 6
        print("awesome! {} is correct. you have 6 points.")
#this means that the word the user writes and the word the computer chose are the same

    if word_pick in english_words:
        points += 3
        print("you gained more points." + "t\t\t" "points: " + points)
#this means that the word the user writes and the word the computer chose are not the same, but the word the user writes is in the list of words the computer chooses from
   
    elif word_pick == 'quit':
          print("total points:" + points)
          print("give one more shot?")
          break
#this outputs the total points and ends the game.
          
    else:
        print("oops! {} is wrong. you miss a point.")
        points -= 1
#the user loses a point, so his total points is reduced by one.
    
