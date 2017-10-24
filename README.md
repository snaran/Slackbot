SlackBot - Python

Simple slackbot that handles some given commands and is capable of getting information from a data file, multiple data files is also supported by following the existent code. This also works as a template for a more complex bot as the basic capabilities are already
fully functional. This also contains a file to get your unique bot ID, from the given slack token.

Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

  Prerequisites:

  Things that you will need:

    -Either Python 2 or 3
    -pip and virtualenv to handle Python application dependencies
    -Free Slack account with a team on which you have API access or sign up for the Slack Developer Hangout team
    -Official Python slackclient code library built by the Slack team
    -Slack API testing token

Installing:

  First, we need to get a virtualnv to handle python application dependencies, this is done by opening up the temrinal/command line
  and moving into the directory of your chosing to store the files. Within that directory to deploy a new virtualenv by typing
  
    virtualenv slackbot
  
  then, to active type
  
    source slackbot/bin/activate
    
  next, you must install the slack API library so you can actually communicate with the slack client. 
  In terminal type:
  
    pip install slack client
  
  Next, we have to obtain our own BOT TOKEN, this is done by first, signing up to slack then going into the bot user page, after that, click on the
  "create a new bot user" link, then name it whatever you want, in this case I will be naming mine sherlock. After this is done, the page will give you a 
  unique BOT TOKEN. after you copy your TOKEN, go ahead and hit save integration. 
  
  Now, back at the command line we have to make the token an environment variable
  NOTE: everytime you exit out of the environment OR close your current terminal window, you must re open the virtual environemnt and RE-TYPE your enviromental variables.
   
  To export the token as a environment variable you must type on the terminal:
    
    export SLACK_BOT_TOKEN = 'your slack bot token from the website'
  
  To get the BOT_ID, just simply run the print_bot_id.py on the termial by typing:
    
    python print_bot_id.py
    
  This prints out the BOT_ID. Now, we have to save the BOT_ID into another environment variable, to do this type:
  
    export BOT_ID = 'your slack bot BOT ID'
  
  Now, this should be all set and you should be able to run your own bot with your own TOKEN.
  
Running the tests:
  
  There is a separated file called filereader.py thats in charge of testing if the file reading procejures are working properly,
  feel free to use this file to test out any filereading operations beyond the ones I've done.

Deployment:
  
  The only thing you must do is simply run the file on the terminal. MAKE SURE that your virtualenv is initialized and that your enviroment variables are stored.

Functionability:
  
  The bot is fairly simple, it has the following commands:
    
    hello: says hello and introduces himself
    commnads: shows the list of commands
    gettime: displays the current time and date
    getfirstrow: gets the first row of the specified file
    getfilesize: gets the file size of the specified file
    getfirstten: gets the first ten rows of the specified file
    getfilename: gets the file name of the specified file
    getfilelocation: gets the file location of the specified file

Built With
    
    Python 2.7.10

Author

  Samuel Naranjo - Towson University

Acknowledgments

  https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
  https://www.stackoverflow.com
  https://api.slack.com/tutorials/tags/python
  http://kazuar.github.io/building-slack-game-part1/
  
