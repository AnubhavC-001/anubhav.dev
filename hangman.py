from getpass import getpass
choose_word=getpass("Enter any word to your liking challenger !")
lives=len(choose_word)+2
guesses=[]
ft=False
while not ft:
    for letter in choose_word:
        if letter.lower() in guesses:
            print(letter,end=" ")
        else:
            print("_",end=" ")
    print("")

    guess =input(f"Lives left {lives}, Next guess :")
    guesses.append(guess.lower())
    if guess.lower() not in choose_word.lower():
        lives-=1
        if lives==0:
            break
    ft=True
    for letter in choose_word:
        if letter.lower() not in guesses:
            ft=False
if ft:
    print("GG")
else:
    print("sad")
