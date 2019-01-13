from random import shuffle
#these lines only for sample data
name1=name2=email1=email2="foo"
groupName="fee"

namesAndEmails=isGivingGiftTo=[[name1,email1],[name2,email2]]
shuffle(isGivingGiftTo)
exportFile = open("%s.txt" %groupName, "w")
exportFile.write("Sender\t\t\t\tReciever\n")
for i in range(len(namesAndEmails)):
    exportFile.write(namesAndEmails[i][0]+" "+namesAndEmails[i][1]+" "+isGivingGiftTo[i][0]+" "+isGivingGiftTo[i][1]+"\n")
exportFile.close()
