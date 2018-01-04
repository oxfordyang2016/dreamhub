import click,ast,os
from config import url
import time
import requests
@click.command()
#@click.option('--count', default=1, help='Number of greetings.example:gtd --inbox "try to test gtd server" --plantime 171218 --project "gtd"  ')
#this line is used to supply promt ask user to input
#@click.option('--name', prompt='Your name',help='The person to greet.')
#@click.option('--t', default="i am test")
@click.option('--inbox',help='u should write anything in ur mind use the format:example:gtd --inbox "try to test gtd server" --plantime 171218 --project "gtd" ')
@click.option('--taskstatus',default="unfinished")
@click.option('--today',default="noinfo")
@click.option('--tasktime',default="have not been deal with")
@click.option('--update',default="noupdate",help='gtd --update "yes" --id 16 --plantime 20171212 --project "inbox" --taskstatus "finish"')
@click.option('--id',default="noselect")
@click.option('--project',default="inbox")
@click.option('--login',default="nologin",help='gtd --login "yes" --email "exampleemail" --password "example"')
@click.option('--email',default="noemail")
@click.option('--password',default="nopassword")
@click.option('--plantime',default="unspecified",help="it is used to specify the task plan time")
def task(inbox,tasktime,plantime,taskstatus,today,update,id,project,login,email,password):
    #about cookie http://docs.python-requests.org/en/master/user/quickstart/
    #check absoulute path is very important there,when u not check the absoulute
    #file path.when u use the gtd service in other directory,the gtd cookie book wiil not be updated
    currentdir = os.path.dirname(os.path.abspath(__file__))
    cookiepath= str(currentdir)+'/cookiebook.txt'
    if str(login)!="nologin":
        r=requests.post(str(url)+'/login',data={'email':email,'password':password,'client':'commandline'})
        print(str(r.cookies['email']))
        with open(cookiepath,"w") as f:
            print(str([r.cookies['email'],r.cookies['logintime'],r.cookies['client']]))
            logintime=str(r.cookies['logintime'])
            logintime=ast.literal_eval(logintime)
            print(logintime)
            email=r.cookies['email']
            email=ast.literal_eval(email)
            cookies=[email,logintime,r.cookies['client']]
            print(cookies)
            #for item in cookies:
            #    f.write("%s\n" % item)
            #f.write(str([r.cookies['email'],r.cookies['logintime'],r.cookies['client']]))
            f.write(str({'email':email,'logintime':logintime,'client':r.cookies['client']}))
        return
    try:

        cookie=getfileeverylinetolist(cookiepath)
        cookie = cookie[0]
        cookie = ast.literal_eval(cookie)
        print("++++++++++++++++")
        print(cookie)
    except:
        print("------------------bug-------------------")
        pass
    if str(today)!="noinfo":
        r= requests.get(str(url)+'/today',cookies=cookie)
        #print(r.text)
        for k,v in r.json().iteritems():
            print "id is "+str(k)+" task is "+str(v)

        return "allok"
    if str(update)!="noupdate":
        id = str(id)
        project = str(project)
        taskstatus=str(taskstatus)
        r=requests.post(str(url)+'/update',cookies=cookie,json={"id":id,"project":project,"plantime":plantime,"taskstatus":taskstatus})
        print(r.text)
        return "allok"

    inboxthing = str(inbox)
    inputtime = str((time.ctime()))
    specifytasktime = str(plantime)
    status = str(taskstatus)
    print(str(tasktime))
    print(inbox)
    #upload-data = {'inbox':inboxthing,'input-time':inputtime,'task-status':status,'plantime':specifytasktime}
    uploaddata = {'inbox':inboxthing,'input-time':inputtime,'project':project,'task-status':status,'plantime':specifytasktime}
    try:
        r = requests.post(str(url)+'/gtdcli',cookies=cookie, json =uploaddata)
        print('server return info==>',r.text)
    except BaseException as e:
        print("upload fail,please resend later")
        print("error info is ",str(e))
def test():
    print("i am test the setup.py")

def getfileeverylinetolist(fname):
    '''
    this fucntion is  used to get
    everyline to a list
    '''
    try:
        with open(fname,encoding='utf8') as f:
            content = f.readlines()
    except:
        '''
        this line is designed for python2
        '''
        with open(fname) as f:
            content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    content = [k for k in content if k!='']
    return content
