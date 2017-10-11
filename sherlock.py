import os
import time
import csv
from datetime import datetime
from slackclient import SlackClient

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + BOT_ID + ">"

# LIST OF COMMANDS
#-----------------------------------------------------------------------
HELLO_COMMAND = "hello", "hi", "hey", "Hello", "Hi", ":)", "Hey"
SHOWCOMMANDS_COMMAND = "commands"
TIME_COMMAND = "gettime"
ROWCOMMAND_NUMBERONE = "getfirstrow"
GETFILESIZE_COMMAND = "getfilesize"
GETFIRST10_COMMAND = "getfirstten"
GETFILENAME_COMMAND = "getfilename"
GETFILELOCATION_COMMAND = "getfilelocation"
#-----------------------------------------------------------------------

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

#Calls on the top-1m.csv file
filenameAlexa = "top-1m.csv"
class getAlexaInfo():
    def __init__(self,filenameAlexa):
        with open(filenameAlexa, "r") as f_input:
            csv_input = csv.reader(f_input)
            self.details = list(csv_input)
    def get_row(self,row):
        return self.details[row-1]

#getting file size --> converts bytes into the appropiate category
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_sizenum(filenameAlexa):
    if os.path.isfile(filenameAlexa):
        file_info = os.stat(filenameAlexa)
        return convert_bytes(file_info.st_size)
totalfilesize = file_sizenum(filenameAlexa)

#getting the first 10 elements
rows =[]
itemslist = []
with open(filenameAlexa, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        #extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        #printing the first 5 rows
        for row in rows[:10]:
            itemslist.append(row)
            #parsing each column of a row

#---------------------------------------------------------------

#this part handles all the commands
def handle_command(command, channel):

    if command.startswith(SHOWCOMMANDS_COMMAND):
        responseCommand = "The general commands are: hello, gettime and commnads. And the useful commands for file management are: getfirstrow, getfirstten, getfilesize, getfilename, getfilelocation"
        slack_client.api_call("chat.postMessage", channel=channel,
        text=responseCommand, as_user=True)

    if command.startswith(GETFILENAME_COMMAND):
        responseName = "The name of the file is: "
        slack_client.api_call("chat.postMessage", channel=channel,
        text=responseName + str(filenameAlexa), as_user=True)

    if command.startswith(GETFILESIZE_COMMAND):
        slack_client.api_call("chat.postMessage", channel=channel,
        text="The file size is: " + totalfilesize, as_user = True)

    if command.startswith(ROWCOMMAND_NUMBERONE):
        data = getAlexaInfo(filenameAlexa)
        number = data.get_row(1)
        slack_client.api_call("chat.postMessage", channel=channel,
        text="The most visited website by alexa is: " + str(number), as_user=True)

    if command.startswith(GETFIRST10_COMMAND):
        data = getAlexaInfo(filenameAlexa)
        number = data.get_row

        slack_client.api_call("chat.postMessage", channel=channel,
        text="The top 10 websites visited by alexa are: " + str(itemslist), as_user=True)

    if command.startswith(HELLO_COMMAND):
        responseHello = "Hey! I am Sherlock, I will be assisting you today, type *"+SHOWCOMMANDS_COMMAND+"* to see everything I can do for you!"
        slack_client.api_call("chat.postMessage", channel=channel,
        text=responseHello, as_user=True)

    if command.startswith(TIME_COMMAND):
        responseTime = "The exact time is: " + str(datetime.now())
        slack_client.api_call("chat.postMessage", channel=channel,
        text=responseTime, as_user=True)

    if command.startswith(GETFILELOCATION_COMMAND):
        filelocation = os.path.dirname(os.path.abspath(filenameAlexa))
        slack_client.api_call("chat.postMessage", channel=channel,
        text="The file is located at: " + filelocation, as_user=True)
"""
    elif:
        elseresponse = "I didn't get that, please type *"+SHOWCOMMANDS_COMMAND+"* to see what I can do"
        slack_client.api_call("chat.postMessage", channel=channel,
        text=elseresponse, as_user=True)
"""

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
