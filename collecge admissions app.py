# here I am getting the user inputs for test score and class rank
testScoreString = input("Type your score here")
classRankString = input("type class rank here")

# then I am converting the string to integer with the int function
testScore = int(testScoreString)
classRank = int(classRankString)

# The rest of the code checks the admissions acceptance
# if the score is greater than or equal to 90, and the classrank is greater or equal to 25
if testScore >= 90:
    if classRank >= 25:
        # then print accept
        print("Accept")
    #     if not print reject
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