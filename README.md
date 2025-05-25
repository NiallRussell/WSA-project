# Queens of RuPaul's Drag Race

##### This application allows the use to view the queens of RuPaul's Drag Race. It links to an SQL database which the user can interact with. The user can update details of any queen and add new queens to the database.

##### The user can interact with the database at https://niallrussell93.pythonanywhere.com/queenviewer.html

##### Five buttons are included to allow the user to create a new queen, update an existing queen's details, view the average age of first place queens, and compare the success of queens from different cities. The user can also view a list of all Drag Race franchises across the globe. The franchises are listed in a separate table in the database and are not linked to the queen table as this only lists queens who competed on the main US franchise. 

##### The database is incomplete, allowing the user to input details of any missing queens to achieve the total of 228 queens who have competed on the show. 

##### The button 'Compare Queen Counts by Season' allows the user to view how many queens should be included in each season, and how many are actually included in the database. This informs the user how many queens are missing from each season so they can narrow their focus when inputting new data. There is a seasons table in the database which links to the queen table through the season number as a foreign key. 