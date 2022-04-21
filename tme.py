import os,platform
os.system('git pull')

tme=platform.architecture()[0]
if tme=="32bit":
    print('Sorry Update Your Phone...')
elif tme=="64bit":
    __import__("tm").reg()
