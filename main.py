from team import lotteryTeam, otherTeam, record, fullRecord, winningChance, top4, boardUpdate
import random
import time
from prettytable import PrettyTable

table = PrettyTable()
table2 = PrettyTable()
table3 = PrettyTable()
table4 = PrettyTable()

lotteryPick = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
otherPick = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


def numberCreate():
    numList = []
    for i in range(1, 1001):
        numList.append(i)

    return numList


def draftSimulation(numberList):
    teamOdds = {}
    pickOrder = []
    chanceList = [140, 140, 140, 125, 105, 90, 75, 60, 45, 30, 20, 15, 10, 5]

    for i in range(len(lotteryTeam)):
        teamOdds[lotteryTeam[i]] = []

    for i in range(len(chanceList)):
        for j in range(0, chanceList[i]):
            number = random.choice(numberList)
            numberList.remove(number)
            teamOdds[lotteryTeam[i]].append(number)

    numList = numberCreate()

    while len(pickOrder) != 4:
        number = random.choice(numList)
        numList.remove(number)
        for j in range(len(lotteryTeam)):
            if (number in teamOdds[lotteryTeam[j]]) and (lotteryTeam[j] not in pickOrder):
                pickOrder.append(lotteryTeam[j])

    otherTeam = []
    for i in range(len(lotteryTeam)):
        if lotteryTeam[i] not in pickOrder:
            otherTeam.append(lotteryTeam[i])

    pickOrder = pickOrder + otherTeam

    return pickOrder


def positionChange(teamOrder):
    #hi
    firstChangeList = []
    changeDict = {}
    changeList = []
    arrow = ["↑ ", "↓ ", "- "]
    for i in range(len(lotteryTeam)):
        for j in range(len(teamOrder)):
            if teamOrder[j] == lotteryTeam[i]:
                loc = i - j
                firstChangeList.append(loc)

    for i in range(len(firstChangeList)):
        if firstChangeList[i] < 0:
            num = -firstChangeList[i]
            combine = arrow[1] + str(num)
            changeDict[lotteryTeam[i]] = combine
        elif firstChangeList[i] == 0:
            combine = " "
            changeDict[lotteryTeam[i]] = combine
        elif firstChangeList[i] > 0:
            combine = arrow[0] + str(firstChangeList[i])
            changeDict[lotteryTeam[i]] = combine

    for i in range(len(teamOrder)):
        changeList.append(changeDict[teamOrder[i]])

    return changeList


def recordOrder(teamOrder):
    recordDict = {}
    recordList = []
    for i in range(len(lotteryTeam)):
        recordDict[lotteryTeam[i]] = record[i]

    for i in range(len(teamOrder)):
        recordList.append(recordDict[teamOrder[i]])

    return recordList


def lotterySim(teamOrder):
    print("\n|-------------------------------------------------------------|")
    print("FULL DRAFT RESULT:")
    print("\n|------------------------FIRST  ROUND-------------------------|")
    change = positionChange(teamOrder)
    recordList = recordOrder(teamOrder)
    fullList = lotteryTeam + otherTeam
    fullPick = lotteryPick + otherPick
    for i in range(len(fullPick)):
        fullPick[i] += 30
    totalRecord = record + fullRecord
    table.add_column("PICK", lotteryPick)
    table.add_column("               TEAM", teamOrder)
    table.add_column("RECORD", recordList)
    table.add_column("CHANGE", change)
    table.align = "l"
    table2.add_column("PICK", otherPick)
    table2.add_column("              TEAM", otherTeam)
    table2.add_column("RECORD", fullRecord)
    table2.align = "l"
    table3.add_column("PICK", fullPick)
    table3.add_column("              TEAM", fullList)
    table3.add_column("RECORD", totalRecord)
    table3.align = "l"
    print(table)
    print("|-----------------------END  OF  LOTTERY----------------------|\n")
    time.sleep(3)
    print(table2)
    time.sleep(3)
    print("\n|------------------SECOND  ROUND---------------------|")
    print(table3)
    print("\n|------------------END  OF  DRAFT--------------------|\n")
    time.sleep(2)
    print("The top four of this draft is:")
    print(f"\t1. {teamOrder[0]}")
    print(f"\t2. {teamOrder[1]}")
    print(f"\t3. {teamOrder[2]}")
    print(f"\t4. {teamOrder[3]}")
    time.sleep(2)
    print(f"\nCongratulations to the {teamOrder[0]} with the 1st overall pick!")
    time.sleep(2)
    print("\nThis concludes the 2022 NBA Draft Lottery.")
    print("\nThank you for using the NBA Draft Lottery Simulator!")


def currentStanding():
    table4.add_column("PICK", lotteryPick)
    table4.add_column("               TEAM", lotteryTeam)
    table4.add_column("RECORD", record)
    table4.add_column("TOP 4", top4)
    table4.add_column("1ST OVR", winningChance)
    table4.align = "l"
    print(table4)


def randomTop4(teamOrder):
    top4List = []
    for i in range(0, 4):
        top4List.append(teamOrder[i])

    random.shuffle(top4List)
    return top4List


def currentBoard(teamOrder, x):
    table5 = PrettyTable()
    currentOrder = boardUpdate
    num = x - 1
    currentOrder[num] = teamOrder[num]
    table5.add_column("PICK", lotteryPick)
    table5.add_column("               TEAM", currentOrder)
    table5.align = "l"
    print(table5)
    del table5


def main():
    choiceList = ["a", "b"]
    x = 14
    numList = numberCreate()
    pickOrder = draftSimulation(numList)
    top4Random = randomTop4(pickOrder)
    print("\nWelcome to the 2022 NBA Draft Lottery Simulator!")
    print("(using projection record from FiveThirtyEight)\n")
    print("Current Lottery Team Standing:")
    currentStanding()
    print("\nPlease select your simulation method (a or b):")
    print("\ta) Simulate the whole draft")
    print("\tb) Simulate each team via order")
    choice = input("Your choice: ").lower()
    while choice not in choiceList:
        choice = input("Invalid input, please choose again: ").lower()
    if choice == "b":
        print("\nThe NBA Draft Lottery begins:")
    while choice != "a" and x != 0:
        if x > 3:
            print("\n---------------------------")
            print(f"The {x}th pick belongs to:")
            print("---------------------------")
            time.sleep(2)
            print(f"The {pickOrder[x - 1]}\n")
            time.sleep(2)
            currentBoard(pickOrder, x)
        if x == 5:
            print("\nThe top four teams remaining are: ")
            print("(orders to be revealed)")
            print(f"\t{top4Random[0]}")
            print(f"\t{top4Random[3]}")
            print(f"\t{top4Random[1]}")
            print(f"\t{top4Random[2]}")
        elif x == 3:
            print("\n---------------------------")
            print(f"The {x}rd pick belongs to:")
            print("---------------------------")
            time.sleep(2)
            print(f"The {pickOrder[x - 1]}\n")
            time.sleep(2)
            currentBoard(pickOrder, x)
        elif x == 2:
            print("\n---------------------------")
            print(f"The {x}nd pick belongs to:")
            print("---------------------------")
            time.sleep(2)
            print(f"The {pickOrder[x - 1]}\n")
            time.sleep(2)
            currentBoard(pickOrder, x)
        elif x == 1:
            print("\n---------------------------")
            print(f"The {x}st pick belongs to:")
            print("---------------------------")
            time.sleep(2)
            print(f"The {pickOrder[x-1]}\n")
            time.sleep(2)
            print(f"Congratulations to the {pickOrder[x-1]} with the 1st overall pick!")
            time.sleep(2)
            currentBoard(pickOrder, x)
            a = input("\nEnter any key to see the full result: ")
            break
        x -= 1
        choice = input("\nEnter any key to continue the draft, or enter 'a' to simulate to the end: ")
    lotterySim(pickOrder)


main()
