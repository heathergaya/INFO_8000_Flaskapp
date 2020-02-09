# INFO_8000_Flaskapp

A very basic app with poor security (but also useless data). 
Data comes from birdinfo.db, created in database_for_flask.ipynb.



Four routes are possible

Route '/':
Takes you to the home page. Nothing much here. 

  Example: http://34.69.66.156/ returns a page with some text
  

Route '/testy':
Used during testing (to see if app was broken).
    
    Example: http://34.69.66.156/testy?name=x returns "name":"x Hello" in JSON


Route '/viewtable':
Allows the user to query any SQlite table available in the birdinfo.db database using ?myquery=. 
Tables can be one of: observers, effort, birds, nets, sites

    Example: 34.69.66.156/viewtable?myquery=SELECT%20*%20FROM%20observers returns the observer table. 
    Example2: http://34.69.66.156/viewtable?myquery=SELECT%20*%20FROM%20birds returns all bird captures 

Route '/addstuff' requires permission, but allows user to add to database:
Requires --user admin:yaybirds be tacked on to end of command. Obviously in a real database of any importance we would make this slighly more secure and not tell everyone the password and username.

    Example: http://34.69.66.156/addstuff?info=INSERT%20INTO%20effort%20VALUES%20(%27Jan21%27,%202,%204) will throw an error 
    Example2: http://34.69.66.156/addstuff?info=INSERT%20INTO%20effort%20VALUES%20(%27Jan21%27,%202,%204) --user admin:yaybirds will return a statement showing success
    
