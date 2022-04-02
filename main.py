from turtle import st
from matplotlib.pyplot import pause
import serial
import time
import tweepy
import json
from datetime import datetime
import schedule
 
def getTime():
    vrijeme = datetime.now()
#    return (f'{vrijeme.hour}:{vrijeme.minute}')
    return vrijeme.hour, vrijeme.minute

def getTemp():
    # make sure the 'COM#' is set according the Windows Device Manager
    ser = serial.Serial('COM4', 9800, timeout=1)
    time.sleep(4)
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string

    return string
    ser.close()

def TwitterAuth():
    #get authentication credentials
    with open('config.json') as json_file:
        data = json.load(json_file)

    twitter_auth_keys = {
        "consumer_key"        : data['consumer_key'],
        "consumer_secret"     : data['consumer_secret'],
        "access_token"        : data['access_token'],
        "access_token_secret" : data['access_token_secret']
    }

    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token( 
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    #api = tweepy.API(auth)
    return tweepy.API(auth)

def main():

    #hour, minutes = getTime()
    temp = getTemp()
    api = TwitterAuth()
    
    tweet = "• Vrijeme: "+datetime.now().strftime("%H:%M")+"\n• Izmjerena temperatura: "+temp[3:]+"°C\n• Vlažnost zraka: "+temp[0:2]+"%."
    status = api.update_status(status=tweet)
    #print(temp[0:2]+'   '+temp[3:])


if __name__ == "__main__":

    schedule.every().hour.at(":00").do(main)
    while(True):
        schedule.run_pending()
    
    #print(datetime.now().strftime("%H:%M"))
    #main()