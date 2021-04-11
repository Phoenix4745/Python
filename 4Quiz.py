import time
print('What is your name ?')
name= input().title()
print('Hello !, ' + name + ' Welcome to the quiz \nYou will be asked 10 questions. \nBest of Luck!')
print()

score=0

ans = input("1. Who was the first women from India to climb Mount Everest ?")
if ans.lower() == 'bachendri pal':
    print("That 's right")
    score = score+1
else:
    print('Incorrect')
    print("The correct answer is ", end= "")
    time.sleep(1)
    print('Bachendri Pal')
print()
time.sleep(1)
ans = input("2. Where is Amazon forest located (Continent) ?")
if ans.lower() == 'south america':
    print("That 's right")
    score = score+1
else:
    print('Incorrect')
    print("The correct answer is ", end= "")
    time.sleep(1)
    print("South America")
print()
time.sleep(1)
ans = input("3. Where is Nile river situated (Continent) ?")
if ans.lower() == 'africa':
    print("That 's right")
    score = score+1
else:
    print('Incorrect')
    print("The correct answer is ", end= "")
    time.sleep(1)
    print('Africa')
print()
time.sleep(1)
ans = input("4. Tipu Sultan was the ruler of which city ?")
if ans.lower() == 'mysore':
    print("That 's right")
    score = score+1
else:
    print('Incorrect')
    print("The correct answer is ", end= "")
    time.sleep(1)
    print('Mysore')
print()
time.sleep(1)
ans = input("5. What is the capital city of Netherlands ?")
if ans.lower() == 'amsterdam':
    print("That 's right")
    score = score+1
else:
    print('Incorrect')
    print("The correct answer is ", end= "")
    time.sleep(1)
    print('Amsterdam')
print()
time.sleep(1)
ans = input("6. Which is the smallest country in the world ?")
if ans.lower() == 'vatican city':
    print("That 's right")
    score = score+1
else:
    print('Incorrect')
    print("The correct answer is ", end= "")
    time.sleep(1)
    print('Vatican City')
print()
time.sleep(1)
ans = input("7. Which is the 3rd largest country of the world ?")
if ans.lower() == 'america':
    print("That 's right")
    score = score+1
elif ans.lower() == 'usa':
    print("That 's right")
    score = score+1
elif ans.lower() == 'u.s.a.':
    print("That 's right")
    score = score+1
else:
    print('Incorrect')
    print("The correct answer is ", end= "")
    time.sleep(1)
    print('U.S.A.')
print()
time.sleep(1)
ans = input("8. Current Governor of Reserve Bank ?")
if ans.lower() == 'shaktikanta das':
    print("That 's right")
    score = score+1
elif ans.lower().startswith('sh'):
   print('Your answer is not perfect. You will receive half mark.')
   score = score + 0.5
   print("The correct answer is ", end= "")
   time.sleep(1)
   print('Shaktikanta Das')
else:
    print('Incorrect')
    print("The correct answer is ", end= "")
    time.sleep(1)
    print('Shaktikanta Das')
print()
time.sleep(1)
ans = input("9. Who is the current DGP of Punjab police ?")
if ans.lower() == 'dinkar gupta':
    print("That 's right")
    score = score+1
else:
    print('Incorrect')
    print("The correct answer is ", end= "")
    time.sleep(1)
    print('Dinkar Gupta')
print()
time.sleep(1)
ans = input("10. Who is the First Woman President of India?")
if ans.lower() == 'pratibha patil':
    print("That 's right")
    score = score+1
else:
    print('Incorrect')
    print("The correct answer is ", end= "")
    time.sleep(1)
    print('Pratibha Patil')
print()
print('The test is finished. Let \'s see the result')
time.sleep(2)
print('Your result is ....')
time.sleep(2)
print('You have scored ' + str(score)+ ' marks out of 10')
print()
if score == 10:
    print('Outstanding, You have studied well in your previous classes')
if 8<=score<=9:
    print('Excellent, Your G.K. is good')
if score == 7:
    print('You need a little more practice. Good luck next time.')
if score< 7:
    print("You are not good at G.K. Practice more and try again")
if score<4:
    print("Your G.K. is very weak. You need a lot of hardwork")
