import re
count = 0
llc = 0
lineList = []

pattern = re.compile("^([A-Z]+)\=([A-Z]+)+$") #A=B
pattern1 = re.compile("^([A-Z]+)\=([a-z]+)\-\>([A-Z]+)+$") #A=b->C
pattern2 = re.compile("^([A-Z]+)\=([a-z]+)\-\>([a-z]+)\-\>([A-Z]+)+$") #A=a->b->C ---> A=a->X,X=b->C
pattern3 = re.compile("^([A-Z]+)\=\{([a-z]+)\,([a-z]+)\}\-\>([A-Z]+)+$")#A={a,b}->C ---> A=a->C , A=b->C


with open("/home/sai/FYP/test","r") as f:
    for line in f:
		print line

		if(re.match(pattern,line) <> None or re.match(pattern1,line) <> None ):
			lineList.append(line)

		elif(re.match(pattern2,line) <> None ):
			#print "Yes a match"
			temp = chr(ord('A') + count)
			#print temp
			count = count + 1


		#	line =
			result = re.search("(?<=->).+$",line)
			#print temp + "=" + result.group(0)
			tempLine = temp + "=" + result.group(0)

			result1 = re.search("^(.+?)->",line)
			#print result1.group(0) + temp
			tempLine2 =result1.group(0) + temp


			lineList.append(tempLine2)

			lineList.append(tempLine)

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


		else:
			print " "

print "\n\n\n"
for i in lineList:
	print i
