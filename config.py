import tweepy
import time
import json
import sys, os
import logging



authkey = os.environ['authkey']
authPass = os.environ['authPass']
Access_token = os.environ['Access_token']
Access_Token_Secret = os.environ['Access_Token_Secret']


logger = logging.getLogger()

def main_api():
    auth = tweepy.OAuthHandler(authkey, authPass)
    auth.set_access_token(Access_token, Access_Token_Secret)
    #accessing my profile after auth
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api


# main_api()