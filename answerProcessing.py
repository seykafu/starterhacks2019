import csv
from heapq import nlargest
def main():
    categoryData={}
    for i in range(38):
        categoryData[i]=0
    with open('QUESTION_DATA.csv') as csv_file:
        questionData = csv.reader(csv_file, delimiter=',')
        keyString="AA"
        for line in questionData: #checking line validity
            if "QQ" in line[0]:
                print(line[1]) #prints question
                ans=input() #take input from user however, return to me as a string "1"
                keyString="AA"+ans #converts answer to answer ID
            elif "AA" in line[0]:
                if keyString in line[0]: #checks if this answer is the one the user selected
                    line[1]=line[1].split(';')
                    for i in range(len(line[1])): 
                        line[1][i]=int(line[1][i]) #converts category codes to int
                        categoryData[line[1][i]]+=1 #adds data to master dictionary
    #now have categoryData filled with question responses
    topThree = nlargest(3, categoryData, key=categoryData.get)
    print(topThree)
    return
main()