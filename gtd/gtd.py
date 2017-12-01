import click
import time
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



def test():
    print("i am test the setup.py")
