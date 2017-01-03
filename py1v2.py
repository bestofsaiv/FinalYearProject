import re
count = 0
llc = 0
lineList = []
t =[]


#       .+? for any type of string

pattern = re.compile("^([A-Z]+)\=([A-Z]+)+$") #A=B
pattern1 = re.compile("^([A-Z]+)\=([a-z]+)\-\>([A-Z]+)+$") #A=b->C
pattern2 = re.compile("^([A-Z]+)\=([a-z]+)\-\>([a-z]+)\-\>([A-Z]+)+$") #A=a->b->C ---> A=a->X,X=b->C
pattern3 = re.compile("^([A-Z]+)\=\{([a-z]+)\,([a-z]+)\}\-\>([A-Z]+)+$")#A={a,b}->C ---> A=a->C , A=b->C


with open("/home/sai/FYP/test","r") as f:
    for line in f:
        #print line
        countTrans = len(list(re.finditer('->',line)))
        countStates = countTrans - 1
        #print countStates , "is COuntstates"
        if(re.match(pattern,line) <> None or re.match(pattern1,line) <> None ):
            lineList.append(line)
            print line
        elif(re.match(pattern3,line) <> None ):
			#A={a,b}->C ---> A=a->C , A=b->C
			#First process is ******** a
			result2 = re.search("{(.+?),",line)
			tempLine4 = result2.group(1)

			#First part extraction *********** A=
			result3 = re.search("^(.+?){",line)
			tempLine3 =result3.group(1)

			#Second part extraction ******* C
			result4 = re.search("(?<=->).+$",line)
			#A=a->C
			tempLine5 = tempLine3 + tempLine4 + "->" + result4.group(0) #A=a->C
			lineList.append(tempLine5)
			#-------------------------------

			#Second process is ******** b
			result2 = re.search(",(.+?)}",line)
			tempLine4 = result2.group(1)

			#A=b->C
			tempLine5 = tempLine3 + tempLine4 + "->" + result4.group(0) #A=b->C

			lineList.append(tempLine5)
        elif(countTrans>1):
            intermediateStatesCount = 1
            print line
	           #elif(re.match(pattern2,line) <> None ):
			#print "Yes a match"
            list1 = [m.start() for m in list(re.finditer('->',line))]
            #print list1 , "\t"
            while (intermediateStatesCount<=countTrans):
                temp = chr(ord('A') + count)
                if(intermediateStatesCount == 1):
                    lineList.append(line[0:list1[0]+2] + temp)
                    intermediateStatesCount+=1
                    count = count + 1
                elif(intermediateStatesCount>1 and intermediateStatesCount<countTrans):
                    exLine= chr(ord(temp)-1) + "=" + line[list1[intermediateStatesCount-2]+2:list1[intermediateStatesCount-1]+2] + temp
                    lineList.append(exLine)
                    intermediateStatesCount+=1
                    count = count + 1
                elif(intermediateStatesCount == countTrans):
                    exLine = chr(ord(temp)-1) + "=" + line[list1[intermediateStatesCount-2]+2:len(line)]
                    lineList.append(exLine)
                    intermediateStatesCount+=1
                    count = count + 1

        else:
            print "  "

print "\n\n\n"
for i in lineList:
	print i
#for i in t:
#    print i
