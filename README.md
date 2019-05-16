Log_Analysis
Udacity - Logs Analysis Project

Project Overview
This is a project assigned by Udacity as a part of the Udacity Full Stack Nanodegree program. In this project, our task is to create a reporting tool that prints out reports based on the data in the database. This reporting tool is a Python program using the PostgreSQL database and Vagrant file settings to run a VM server to run the database.

How to Run?
PreRequisites:
• Python3
• Vagrant
• VirtualBox
Setup Project:
1. Install Vagrant and VirtualBox
2. Download or Clone [fullstack-nanodegree-vm](http://https://github.com/udacity/fullstack-nanodegree-vm) repository.
3. Unzip and copy the content of this folder.
4. newsdata.sql file will provide the data.
Launching the Virtual Machine:
1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
   	   $ vagrant up

2. Then Log into this using command:
       $ vagrant ssh

3. Change directory to cd  /vagrant and look around with ls.
Setting up the database and Creating Views:
1. Load the data in local database using the command:
    psql -d news -f newsdata.sql

    The database includes three tables:	    
	○ The authors table includes information about the authors of articles.
	○ The articles table includes the articles themselves.
	○ The log table includes one entry for each time a user has accessed the site.		
2. Use psql -d news to connect to database.
3. Create view new_articles using:

	CREATE VIEW new_articles AS
		SELECT author,concat('/article/',slug)
		FROM articles;

4. Create view view2 using:
	CREATE VIEW view2 AS
		SELECT path, count(path)
		FROM log join new_articles
		on log.path = new_articles.concat
		GROUP BY path 
		ORDER BY count(path) DESC;

5. Create view num_errors using:
	CREATE VIEW num_errors AS
		SELECT TO_CHAR(time :: DATE,'Mon dd,yyyy') as date, count(status) as error
		FROM log 
		WHERE status not like '200%'
		GROUP BY date
		ORDER BY date;

6. Create view num_requests using:
	CREATE VIEW num_requests AS
		SELECT TO_CHAR(time :: DATE,'Mon dd,yyyy') as date, count(*) as total_requests 
		FROM log 
		GROUP BY date
		ORDER BY date;
	
Running the queries:
1. From the vagrant directory inside the virtual machine,run newsdb.py
    $ python newsdb.py
