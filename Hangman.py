from tkinter import *

abc = "abcdefghijklmnopqrstuvwxyz"
encoded = []
tries = []
solution = input("Choose a word?")

error = 0

def compare (solution, encoded):
    for i in range (len(solution)):
        if solution[i]!=encoded[i]:
            return False
    return True

for i in range (len(solution)):
    encoded += "_"


while True:
    if compare(solution,encoded):
        print(solution)
        print("Congrats! You won!")
        break
    for j in encoded:
        print(j, end=" ")

    text = input("\nTell me a letter")

    j=0
    for index in range(len(solution)):
        if text in tries:
            print("You have already entered that letter")
            j-=1
            break
        if solution[index] == text:
            pos = index
            encoded[pos] = solution[pos]
            j+=1
    else:
        if j == 0:
            error += 1
    if error > 4 :
        print('Loser!')
        break
    tries.append(text)

