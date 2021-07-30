from util import *
import datetime as dt

def hello(name):
	f=open("log.txt","a")

	f.write("this line is expected to appear every min\n")
	f.write(dt.datetime.now().strftime("%Y%m%d %H%M%S"))
	f.write('\n')
	f.close()
	print('job done')
def hello2(name):
    print('hello. hello. hello.hello')

hello('george')
