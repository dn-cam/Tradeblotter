File descriptions:  

1. main.py: the main application. It contains two rest apis, one to place orders, and other to get the current position of the user. To start the api server, run "python3 main.py". 

2. Blotter.py: The rest apis in main.py call methods form this class to read or persist data in SQLite3 db. Please read the comments in the file for more information about what the functions do.

3. Database.py: This script contains method to start the database server and establish a connection. This connection is used for the remainder of the service to read and persist data from the SQLite3 database.

4. createDB.py: run this script once in the beginning to create the tables in the database.


Instructions to run the code:

1. run createDB.py to set up the tables in local SQLite3 database. 
2. run main.py to set up api server
3. open ui.html with a browser (preferably chrome) to get the ui up
4. use the ui to place order and get current position.