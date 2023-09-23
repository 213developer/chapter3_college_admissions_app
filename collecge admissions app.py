# here I am gettinG user inputs
testScoreString = input("Type your score here")
classRankString = input("type class rank here")

# then I am converting the string to integer with int
testScore = int(testScoreString)
classRank = int(classRankString)

# The rest of the code checks the admissions acceptance
if testScore >= 90:
    if classRank >= 25:
        print("Accept")
    else:
        print("Reject")
else:
    if testScore >= 80:
        if classRank >= 50:
            print("Accept")
        else:
            print("Reject")
    else:
        if testScore >= 70:
            if classRank >= 75:
                print("Accept")
            else:
                print("Reject")
        else:
            print("Reject")