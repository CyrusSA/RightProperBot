import praw
import config
import time

def bot_login():  #Initializing login from config file
    r=praw.Reddit(username = config.username,
                  password = config.password,
                  client_id = config.client_id,
                  client_secret = config.client_secret,
                  user_agent = 'Right Proper Bot')
    print('Logged in')
    
    return r

def run_bot(r): 
    print('Retrieving Comments')
    for comment in r.subreddit('freefolk+asoiaf').stream.comments():
        flag=0 #flag to determine wether to write to don_reply
        with open('don_reply.txt', 'r') as f: #don_reply stores comment ids of comments already replied to
            list_comments = f.read().split('\n')
            if 'right proper lad' in comment.body.lower() and comment.author != r.user.me() and comment.id not in list_comments:
                print('Commenting')
                comment.reply('right proper')
                l=comment.id
                flag=1
                
        if flag ==1:
            with open('don_reply.txt', 'a') as f:
                f.write(l + '\n')
            print('Sleeping') #sleeping to avoide RateLimit Error
            time.sleep(5)
            print('Sleep Over')
            
#main program        
r = bot_login()
run_bot(r)
