import subprocess
import time
import random
import MySQLdb
from datetime import date, datetime, timedelta

#Determine current time and set the end time. 
#Once executed, SubmissionAutomater.py will continue to run until the deadline date/time set in 'endTime'.
currentTime = datetime.now()
endTime  = currentTime + timedelta(hours=48)

#Connect to the MySQL database
db = MySQLdb.connect("localhost", "user","password","trackerDB")
cursor =  db.cursor()

       
while (currentTime < endTime):
	#Command-line argument
	#cURL : "command line tool for transferring data with URL syntax". For this purpose cURL was used to transfer HTTP POST data 
	#To submit an entry to the contest, the site required the user to fill in the following:
	# First name, Last name, Email address, Postal Code and Country
	#A hidden value also had to be submitted with the POST request
	#The servers response is piped to 'grep'         
	process = subprocess.Popen(['curl -d "contestId=ec--magic-sogn--&Ecom_ShipTo_Postal_Name_First=Triesha&Ecom_ShipTo_Postal_Name_Last=Fagan&Ecom_ShipTo_Online_Email=fagan%40gatech.edu&confirm=fagan%40gatech.edu&Ecom_ShipTo_Postal_PostalCode=30318&Ecom_ShipTo_Postal_Country=United%2bStates&submit=Submit%2bEntry" blog.woodworkingtooltips.com/contest/index.php | grep "accepted" -c &'], shell=True, stdout=subprocess.PIPE)
        output= process.communicate()
	#The cURL command outputs the contents of the sites servers response to the POST command. 
	#If the submisison was accepted html text in the site says "Congratualtions, your submission was accepted. You have submitted XXX entries.
	#If the submission was rejected html text in the site says "Sorry, your submission was rejected. You must wait 3 mintues before submitting again."
	#The value returned by grep is either a 1 or 0. The data piped to grep is checked for the keyword "accepted". 
	#If the submission was accepted, I am assuming the keyword "accepted" will always be present, else the keyword "rejected" will be present
        if any('0' in op for op in output[0]):
            sub_status= "Rejected"
        else: sub_status = "Accepted"   

	#Submisisons are randomized betoween 160 seconds and 300 seconds
        sub_next=random.randint(160,300);
	#Insert the data for this submission into the local MySQL database. The Status field is filled based on the value returned by grep. 
        sub_datetime = datetime.now()
        cursor.execute('INSERT INTO submissions(sub_DATE,sub_TIME,sub_WAITTIME,sub_STATUS) VALUES (%s,%s,%s,%s)',(sub_datetime.date(),sub_datetime.time(),sub_next,sub_status));
	#Sleep betwen 160 and 300 seconds each time. 
        time.sleep(sub_next);

        db.commit()
             

db.close()


#curl -d "contestId=ec--magic-sogn--&Ecom_ShipTo_Postal_Name_First=Triesha&Ecom_ShipTo_Postal_Name_Last=Fagan&Ecom_ShipTo_Online_Email=fagan%40gatech.edu&confirm=fagan%40gatech.edu&Ecom_ShipTo_Postal_PostalCode=30318&Ecom_ShipTo_Postal_Country=United%2bStates&submit=Submit%2bEntry" blog.woodworkingtooltips.com/contest/index.php > curl_o_test.html
