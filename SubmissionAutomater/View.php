<html>
 <head> 
  <title>Contest Automater</title>
 </head>
 <body>
 <?php  

#View.php: To allow the user to track the success of submissions to the sweepstakes, View.php provides the user with a easy way to view the success of each automated submission in the browser by polling the MySQL database that contains the submission data. 


#Connect to MySQL on host machine and select databse to use
  $con = mysql_connect('localhost', 'user', 'password') or die (mysql_error());
  $db = mysql_select_db("trackerDB", $con);
 

#Perform a query to select all rows for each of the columns in the submissions table of trackerDB database
#The submissions tables has 5 columns:
#ID: Primary Key, identifies the entry
#Date: Date the submission was made
#Time: Time the submission was made
#Time until next submission: Number of seconds that will pass before another submission attempt is made
#Status: Was the submission accepted or rejected by the website's server?

$result = mysql_query("SELECT * FROM submissions");
if (false === $result) {
    echo mysql_error();
}

$numRows  = mysql_num_rows($result);

#Setup the table header in HTML
echo "<table border='1'>
<tr>
<th>ID</th>
<th>Date</th>
<th>Time</th>
<th>Time until next submission</th>
<th>Status</th>
</tr>";

#Output each row
for($i=0; $i<$numRows; $i++) {
  $row = mysql_fetch_array($result);	
  echo "<tr>";
  echo "<td>" . $row[0] . "</td>";
  echo "<td>" . $row[1] . "</td>";
  echo "<td>" . $row[2] . "</td>";
  echo "<td>" . $row[3] . "</td>";
  echo "<td>" . $row[4] . "</td>";
  echo "</tr>";
}

echo "</table>";

mysql_free_result($result);


 ?>
 </body>
</html>
