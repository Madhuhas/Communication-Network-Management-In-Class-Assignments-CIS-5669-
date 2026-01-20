# Kotini Sai Madhuhas
#2024.02.03
#numbers examples

import random

randomNumber =  random.choice([1,2,5,19,4,23])
print (randomNumber)

randomString = random.choice("Madhuhas")
print (randomString)

randomRangeNnumer = random.randrange(100,500,2)
print(randomRangeNnumer)

randomNum = random.random();
print(randomNum)

random.seed()
randomNum2 = random.random();
print (randomNum2)

list=[20,17,3,52,2,9]
random.shuffle(list)
print ("Shuffled list:",list)

uniformNum = random.uniform(10,20)
print(uniformNum)
