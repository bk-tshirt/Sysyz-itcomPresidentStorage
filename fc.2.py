##############################################
#               反向密码+凯撒密码             #
##############################################
import time

mess = input("enter you want to enter words:")
tr=''
i=len(mess)-1
while i>=0:
    tr=tr+mess[i]
    i=i-1

key=86
mode='2'
SYM='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz1234567890!@#$%^&*()><,.:;-=_+[]{ }'

translated=''

for sym in tr:
    if sym in SYM:
        symindex=SYM.find(sym)

        if mode=='1':
            trindex=symindex+key
        elif mode=='2':
            trindex=symindex-key
        
        if trindex >= len(SYM):
            trindex=trindex-len(SYM)
        elif trindex < 0:
            trindex=trindex+len(SYM)

        translated=translated+SYM[trindex]
    else:
        translated=translated+sym
    
print("secert message:",translated)


