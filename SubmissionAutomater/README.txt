Open submissionautomater.py

1. Set your desired endtime. Currently, the endTime values can only be set by hour
2. Since code assumes you have an available database: 
a] In 'db' set your hostname, MySQL username and password.
3. This code makes the assumption that the servers response to the users submission will contain keywords identifying whether or not the submission was successful. 
    You may want to figure out what keywords grep should search for in the server's response html code. Once you've determined your success/fail keywords modify the grep parameter in 'process' 
	to search for the keyword which means that the submission was accepted. 