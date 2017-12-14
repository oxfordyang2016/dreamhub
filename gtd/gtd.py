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
@click.option('--taskstatus',default="this status is not finised")
@click.option('--today',default="noinfo")
@click.option('--tasktime',default="have not been deal with")
@click.option('--update',default="noupdate")
@click.option('--id',default="noselect")
@click.option('--project',default="inbox")
@click.option('--plantime',default="--not--clarified",help="it is used to specify the task plan time")
def task(inbox,tasktime,plantime,taskstatus,today,update,id,project):
    if str(today)!="noinfo":
        r= requests.get(str(url)+'/today')
        #print(r.text)
        for k,v in r.json().iteritems():
            print "id is "+str(k)+" task is "+str(v)

        return "allok"
    if str(update)!="noupdate":
        id = str(id)
        project = str(project)
        taskstatus=str(taskstatus)
        r=requests.post(str(url)+'/update',data={"id":id,"project":project,"plantime":plantime,"taskstatus":taskstatus})   
        print(r.text)
        return "allok"

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
