print('Welcome to my minigame!!!')

playing = input('Do you want to play? ')
if playing.lower() != 'yes':
    quit()
print('Okay! Lets play :) ')
score = 0

question = input('who is the president of America? ')
if question.lower() == 'joe biden' :
    print('Correct!!!')
    score +=1
else:
    print('Incorrect!!!')

question = input('who is the president of Nigeria? ')
if question.lower() == 'muhammadu buhari':
    print('correct???')
    score +=1
else:
    print('INcorrect!!!')

question = input('What is the meaning of CPU? ')
if question.lower() == 'central processing unit':
    print('correct')
    score +=1
else:
    print('Incorrect')

question = input('Who is the son of God? ')
if question.lower() == 'jesus':
    print('correct!!!')
    score +=1
else:
    print("incorrect")

print("You got " + str(score) + " questions correctly!!!")
print("You got " + str((score /4) * 100) + "%")
