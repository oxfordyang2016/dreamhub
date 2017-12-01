import click
from config import url
import time
import requests
@click.command()
#@click.option('--count', default=1, help='Number of greetings.')
#this line is used to supply promt ask user to input
#@click.option('--name', prompt='Your name',help='The person to greet.')
#@click.option('--t', default="i am test")
@click.option('--inbox',help="u should write anything in ur mind")
@click.option('--tasktime',default="have not been deal with")
@click.option('--taskstatus',default="this status is not finised")
def task(inbox,tasktime,taskstatus):
    inboxthing = str(inbox)
    inputtime = str((time.ctime()))
    specifytasktime = str(tasktime) 
    status = str(taskstatus)
    print(str(tasktime))
    print(inbox)
    #upload-data = {'inbox':inboxthing,'input-time':inputtime,'task-status':status,'plantime':specifytasktime}
    uploaddata = {'inbox':inboxthing,'input-time':inputtime,'task-status':status,'plantime':specifytasktime}
    try:
        r = requests.post(str(url)+'/gtdcli', data =uploaddata )
        print('server return info==>',r.text)
    except BaseException as e:
        print("upload fail,please resend later")
        print("error info is ",str(e))
def test():
    print("i am test the setup.py")
