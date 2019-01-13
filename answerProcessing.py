import csv
from heapq import nlargest

def main():
    categoryData={}
    for i in range(38):
        categoryData[i]=0
    csv_file=open('QUESTION_DATA.csv',encoding="ISO-8859-1")
    questionData = csv.reader(csv_file)
    keyString="AA"
    for line in questionData: #iterates through lines
        if line[0]=='0': #marks end of general questions
            break;
        processLine(line,categoryData)
    #now have categoryData filled with general question responses
    

    topTwo = nlargest(2, categoryData, key=categoryData.get) #gets top two cats
    print(topTwo)
    for line in questionData: #continues iteration through lines, starting at QQ10
         #sports outdoors sub, access if toptwo is within 26-34,37
        if "QQ13" in line[0]: #forces end on QQ13
            break
        if (topTwo[0]>=26 and topTwo[0]<=34) or topTwo[0]==37 or (topTwo[1]>=26 and topTwo[1]<=34) or topTwo[0]==37: #checks if one of toptwo is within sub 1
            processLine(line, categoryData)
            
    for line in questionData: #continues iteration through lines, starting at QQ13
         #video game/elec sub, access if toptwo is within 0-11
        if "QQ16" in line[0]: #forces end on QQ16
            break
        if (topTwo[0]>=0 and topTwo[0]<=11) or (topTwo[1]>=0 and topTwo[1]<=11):
            processLine(line, categoryData)
            
    for line in questionData:
        #clothinghealth personalcare sub, access if topTwo is within 18-25,36
        if "QQ19" in line[0]:
            break
        if (topTwo[0]>=18 and topTwo[0]<=25) or topTwo[0]==36 or (topTwo[1]>=18 and topTwo[1]<=25) or topTwo[0]==36:
            processLine(line, categoryData)   
            
    for line in questionData:
        #household sub, access if topTwo is within 12-17,35
        if line[0]=='0':
            break
        if (topTwo[0]>=12 and topTwo[0]<=17) or topTwo[0]==35 or (topTwo[1]>=12 and topTwo[1]<=17) or topTwo[0]==35: 
            processLine(line, categoryData) 

    csv_file.close()
    topThreeFINAL = nlargest(3, categoryData, key=categoryData.get)
    return topThreeFINAL

def processLine(line,categoryData):
    global keyString
    if "QQ" in line[0]:
            print(line[1]) #prints question
            ans=input() #take input from user however, return to me as a string "1"
            keyString="AA"+ans #converts answer to answer ID
    elif "AA" in line[0]:
        if keyString in line[0]: #checks if this answer is the one the user selected
            line[1]=line[1].split(';')
            for i in range(len(line[1])):
                if line[1][i] != '':
                    line[1][i]=int(line[1][i]) #converts category codes to int
                    categoryData[line[1][i]]+=1 #adds data to master dictionary
    return
main()