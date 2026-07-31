definitions = int(input())

months=[
    "Ox",
    "Tiger",
    "Rabbit",
    "Dragon",
    "Snake",
    "Horse",
    "Goat",
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
    "Rat"
]

ages = { # based on bessie, negatives mean younger cuz bessie - x = elsie for example
    "Bessie":0
}
for i in range(definitions):
    sentence = input().split()
    cow = sentence[0]
    guideline = sentence[-1]
    dire = sentence[3]
    nextStop = sentence[4]

    increment = 1 if dire == "next" else -1
    curMonth = (ages[guideline] + increment) % 12
    stepCnt = 1
    while months[curMonth] != nextStop:
        curMonth += increment
        stepCnt += 1
        if curMonth == -1:
            curMonth = 11
        elif curMonth == 12:
            curMonth = 0
    ages[cow] = ages[guideline] + stepCnt*increment

print(abs(ages["Elsie"]))

