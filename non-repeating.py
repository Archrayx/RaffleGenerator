import random as rd

raffle = open("raffle.txt", "r+")
name = ""
EMail = ""
RUSURE = False

def ays():
    global RUSURE
    global name
    global EMail
    while RUSURE == False:
        name = input("Name: ")
        answer = input("is that the right name? (y/n): ")
        while answer == 'y':
            EMail = input("EMail: ")
            answer2 = input("is that the right EMail? (y/n): ")
            if answer2 == "y":
                RUSURE = True
                break
while True:
    r = rd.randint(1000,9999)
    ays()
    if (str(r)) not in ('raffle.txt'):
        raffle.write(name + " ************* " +"R" + str(r) + " ************* " + EMail + '\n')
        print (r)
        break
raffle.close()
