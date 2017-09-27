# Logs Analysis Project
This is the third project with **Udacity Full Stack Web Developer Nanodegree Program**. A python program is wrote to analyze the data "news". 

## Prepare the software and data
First, install the Linux-based virtual machine to get the PostgreSQL database and psycopg2 (postgreSQL database adapter for Python) needed for the project. 

Next, download the data file provided by Udacity, put the file into the vagrant directory (which is shared with your virtual machine) and load the data into your local database. 

## How to run the program
1. Download the python file reporting_tool.py and put it into the vagrant directory, where your data is.
2. In the Terminal, cd into the vagrant directory, and use the command `python3 reporting_tool.py` to run the python code. 
3. A text file report.txt will be created in the same directory. The analysis result is in this text file.

## Functionality
The python program connects to the database with **psycopg2**, runs three sql queries to obtain the answers to three questions, and presents the results in clearly formatted text. 
The three questions to answer: 
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## _Note: you need to bring the virtual machine online and log into it before loading the data and running the python program._ 


