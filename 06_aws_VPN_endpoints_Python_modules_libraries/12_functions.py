# Kotini Sai Madhuhas
# 2024.02.17
# functions example

def debug(debugString):
    "Kotini Sai Madhuhas: debug function"
    print(myDebug)
    return
myDebug="Kotini Sai Madhuhas: first function"
debug(myDebug)

# define functions
def listUpdater(myList):
    "Kotini Sai Madhuhas: list updater"
    newList=[10,100,1000]
    myList.append(newList)
    return

orgiList=[1,3,5,7]
print(orgiList)
listUpdater(orgiList)
print(orgiList)

# define functions2
def listRefUpdater(myList):
    "Kotini Sai Madhuhas: list updater"
    newList=[10,100,1000]
    myList=newList # this assign a new reference to myList
    return

orgiList=[1,3,5,7]
print(orgiList)
listRefUpdater(orgiList)
print(orgiList)


def debug2(debugString, extraInfo):
    "Kotini Sai Madhuhas: debug function"
    print(debugString,'',extraInfo)
    return
myDebug="Kotini Sai Madhuhas: second function"
extraInfo=2
debug2(myDebug, extraInfo)


def printDetail(name, age):
    "Kotini  Sai Madhuhas: detail printer"
    print(name,'',age)
    return
name1="Kotini"
age1=25
printDetail(age=age1,name=name1)

