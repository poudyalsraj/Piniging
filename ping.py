import datetime
import os
import time
hnameList=[]
maxLen=2
while len(hnameList)<maxLen:
	hostname = input("Enter hostname: ")
	hnameList.append(hostname)

#while True:
n=0
for i in hnameList:
	print ("\n"+i)
	response = os.system("ping -c 1 " + hnameList[n])
	file = open("logfile.log", "a")
	t=datetime.datetime.now()
	a=t.strftime("%Y-%M-%D %H:%M:%S")

	if response == 0:
		print( "Network Active")
		file.write(i+ "  Network Active "+a+"\n")
	else:
		print("Network Error")
		file.write(i+ "  Network Error "+ a +"\n")
	
	n=n+1
#time.sleep(5)

















	
