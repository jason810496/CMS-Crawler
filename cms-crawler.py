import argparse

import threading
import time

import requests
from bs4 import BeautifulSoup as bs

from dotenv import load_dotenv
load_dotenv()
import os

# load environment variable from .env
HOST = os.getenv('HOST')
CSVNAME = os.getenv('CSVNAME')
THREAD_AMOUNT = int(os.getenv('THREAD_AMOUNT'))

# argument status
VERBOSE=False


# crawler class for multi thread
class Crawler:
    def __init__(self,username,password,question,filename):
        self.username = username
        self.password = password
        self.question = question
        self.filename = filename
        self.session = requests.Session()

    def login(self):
        getLoginPage = self.session.get( HOST )
        parseLoginPage = bs( getLoginPage.content , 'html.parser')
        xsrf_token=parseLoginPage.find('input')['value']
        login_payload = {'username' : self.username  , 'password' : self.password , '_xsrf' : xsrf_token }
        loginResponce = self.session.post( HOST+"login" , data=login_payload )
        if VERBOSE:
            print(f"{self.username} login : {loginResponce}")

    def submit(self):
        getSubmitPage = self.session.get( HOST + "tasks/"+ self.question +"/submissions")
        parsegetSubmitPage = bs( getSubmitPage.content , 'html.parser')
        inputList=parsegetSubmitPage.find_all('input')
        submissionFile = { inputList[2]['name'] : open( self.filename , 'rb')}
        xsrf_payload = { '_xsrf' : inputList[0]['value'] }
        submitResponce = self.session.post( HOST + "tasks/"+  self.question +"/submit" , data=xsrf_payload , files=submissionFile )
        if VERBOSE:
            print(f"{self.username} submit : {submitResponce}")

    def all(self):
        self.login()
        self.submit()



crawlerList = []
threads = []

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument( "-v" , "--verbose" , action="store_true" , help="increase output verbosity" )
    parser.add_argument( "-f" , "--file" , type=str , help="csv file with user,password,question,filename ( defult: testing.csv )" )
    parser.add_argument( "-t" , "--thread-limit" , type=int , help="set thread limit ( defult 20 thread )" )
    parser.add_argument( "--host" , type=str , help="set host ( Host also can be set in .env file )" )
    args = parser.parse_args()

    # update variable status
    if args.verbose:
        VERBOSE=True
    if args.file:
        CSVNAME=args.file
    if args.thread_limit:
        THREAD_AMOUNT=args.thread_limit
    if args.host:
        HOST=args.host

    try:
        with open( CSVNAME ) as file:
            idx=0
            for row in file:
                row = row.split(",")
                usr = row[0].strip()
                pas = row[1].strip()
                qst = row[2].strip()
                fil = row[3].strip()

                # set multi thread limit 
                while threading.active_count() > THREAD_AMOUNT:
                    time.sleep(0.1)
                crawlerList.append( Crawler( username=usr , password=pas , question=qst , filename=fil ) )
                threads.append( threading.Thread( target = crawlerList[idx].all ) )
                threads[idx].start()
                idx=idx+1
            print(f"{idx} files submitted !")

            for i in range(idx):
                threads[i].join()

    except IOError:
        print("Could not read csv file:", CSVNAME )
