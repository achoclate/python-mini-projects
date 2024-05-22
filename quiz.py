print('Welcome to my quiz gameish')

playing = input('Do you wanna play? ')

if playing.capitalize() != 'Yes':
    quit()
print('okay! Let us roll')  
score = 0

answer = input('what is the tallest mountain in the world? ') 
if answer.capitalize() == 'Everest':
    print('Correct!')
    score += 1
else: 
    print('Wrong!') 
    print('Try again!')   
    
answer = input('what is the longest river in the world? ') 
if answer.capitalize() == 'Nile':
    print('Correct!')
    score += 1
else: 
    print('Wrong!') 
    print('Try again!')   
    
answer = input('what is the deepest river in the world? ') 
if answer.capitalize() == 'Congo':
    print('Correct!')
    score += 1
else: 
    print('Wrong!') 
    print('Try again!')   
    
answer = input('what is the largest country in the world? ') 
if answer.capitalize() == 'Russia':
    print('Correct!')
    score += 1
else: 
    print('Wrong!') 
    print('Try again!')   
    
answer = input('what is the largest continent in the world? ') 
if answer.capitalize() == 'Asia':
    print('Correct!')
    score += 1
else: 
    print('Wrong!') 
    print('Try again!')  
    
print('you got ' + str(score) + 'questions correct!')  
print('you got ' + str((score/4) * 100 ) + '%')                   