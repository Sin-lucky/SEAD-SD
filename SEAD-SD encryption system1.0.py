#the System of Encryption And Decoding___Sin/Delta
#The system is developed based on python3.6.4
def wy(a,b):#a is text to encrypt #b is encryption times
    b=int(b)#get the integer times
    times=1
    for times in range(b):
        c=a[::2]+a[1::2]
        times+=1
    return c#Meandering encryption

def ks(a,b,c):#a is text to encrypt，b is key
    key=ord(b)#turn key into code
    wide=len(a)#get text length
    times=0
    awnser=''#create variable to save answer
    for times in range(wide):
        if c == 1:
            tip=chr(ord(a[times:times+1])+key)
        else:
            tip=chr(ord(a[times:times+1])-key)
        awnser+=tip
        times+=1
    return awnser#Caesar encryption

def re_wy(a,b):#a is text of Meandering encryption, b is encryption times
    awnser=''#define answer variable
    wide_1=int(len(a)/2)
    if (len(a)/2)-int(len(a)/2)>0:
        a+='#'
        wide_1=int(len(a)/2)
    b=int(b)
    for times_1 in range(b):
        for times in range(0,wide_1):
            awnser+=a[times::wide_1]
        times_1+=1
    awnser=awnser.rstrip('#')#remove #
    return awnser#Decryption Meandering encryption

def re_ks(a,b,c):#a is text to decrypt, b is key
    key=ord(b)#turn key into code
    wide=len(a)#get text length
    times=0
    awnser=''#create variable to save answer
    for times in range(wide):
        if c == 1:
            tip=chr(ord(a[times:times+1])+key)
        elif c == 0:
            tip=chr(ord(a[times:times+1])-key)
        awnser+=tip
        times+=1
    return awnser#Decryption Caesar encryption

Type=''
while Type != '1':
    Type=input('Input "e" to encryption, input "d" to decrypt, press "1" to exit: ')
    if Type == 'e':
        mi_wen=input('encryption text: ')
        ci_shu=1
        mi_ma_1=input('key-1: ')
        mi_ma_2=input('key-2: ')
        dis_plus=1
        mi_wen=wy(mi_wen,ci_shu)
        mi_wen=ks(mi_wen,mi_ma_1,dis_plus)
        mi_wen=wy(mi_wen,ci_shu)
        if mi_ma_1 != mi_ma_2:
            plus_de=0
        mi_wen=ks(mi_wen,mi_ma_2,plus_de)
        print(mi_wen)
    if Type == 'd':
        mi_wen=input('decrypt text: ')
        ci_shu=1
        mi_ma_1=input('key-1: ')
        mi_ma_2=input('key-2: ')
        re_dis_plus=0
        if mi_ma_1 != mi_ma_2:
            re_dis_plus=1
        mi_wen=re_ks(mi_wen,mi_ma_2,re_dis_plus)
        mi_wen=re_wy(mi_wen,ci_shu)
        re_dis_plus=0
        mi_wen=re_ks(mi_wen,mi_ma_1,re_dis_plus)
        mi_wen=re_wy(mi_wen,ci_shu)
        print(mi_wen)
