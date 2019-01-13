import csv

def main():
    csv_file=open('QUESTION_DATA.csv',encoding="ISO-8859-1")
    questionData = csv.reader(csv_file)
    #sorting into array of arrays
    masterArray=subArray=[]
    for line in questionData:
        if "QQ" in line[0]: #getting initial question
            subArray.append(line[1]) 
            break
    for line in questionData:
        if "QQ" in line[0]: #continuing starting with answers to initial question
            masterArray.append(subArray)
            subArray=[]
            subArray.append(line[1])
        elif "AA" in line[0]:
            subArray.append(line[2])
            
            
    f=open("quiz.html", "a")
    f.seek(41,0)
    ID=NAME=ANS=""
    for j in range(20):
        for i in range(11):
            ID=NAME=("a(%s)", str(i))
            if masterArray[j][i]==True:
                ANS=str(masterArray[j][i])
            outputString="<input type=\"checkbox\" id=\""+ID+"\" name=\""+NAME+"\">\n<label for=\"a1\">"+ANS+"</label>\n<br>"
            f.write(outputString)

    
    
main()