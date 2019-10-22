#Midterm Example #2
def infiniteSequence():
    num = 0
    while num<550:
        yield num
        num += 1
def printEvenNum():
    for i in infiniteSequence():
        if (i % 2 == 0)&(i<500):
            print(i, end = '\n')
printEvenNum()

def printOddNum():
    for i in infiniteSequence():
        # lets generate precisely the same amount of numbers
        if (i%2==1)&(i<499):
            print(i, end = '\n')
printOddNum()


