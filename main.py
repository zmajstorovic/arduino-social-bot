from turtle import st
from matplotlib.pyplot import pause
import serial
import time
import tweepy
import json

def getTemp():
    # make sure the 'COM#' is set according the Windows Device Manager
    ser = serial.Serial('COM4', 9800, timeout=1)
    time.sleep(4)
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        #print(string)
    # time.sleep(5)
    return string
    ser.close()

def TwitterAuth():

    with open('config.json') as json_file:
        data = json.load(json_file)
    
    #print(data['consumer_key'])
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
    api = tweepy.API(auth)
    return api

def main():

   
    #api = tweepy.api
    while(True):
    
        api = TwitterAuth()
        temp = getTemp()
        tweet = "Izmjerena temperatura u uredu je "+temp[3:]+"°C, a vlažnost zraka je "+temp[0:2]+"%."
        status = api.update_status(status=tweet)
        print(temp[0:2]+'   '+temp[3:])

        
        pause(3600)
    

if __name__ == "__main__":
    main()