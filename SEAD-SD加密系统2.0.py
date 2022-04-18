#本代码程序为Sin（宁夜Quiet-Night）与Delta（雾漩Spray-Swirl）开发的加密系统(the System of Encryption And Decoding___Sin/Delta)
#系统基于Python3.6.4开发
def wy(a,b):#a为加密的文字#b为加密次数
    b=int(b)#取整数加密次数
    times=1
    for times in range(b):
        c=a[::2]+a[1::2]
        times+=1
    return c#蜿蜒加密

def ks(a,b,c):#a为加密的文字，b为key
    key=ord(b)#将key转化为编码
    wide=len(a)#获取文本长度
    times=0
    awnser=''#创建结果的变量
    for times in range(wide):
        if c == 1:
            tip=chr(ord(a[times:times+1])-key)
        else:
            tip=chr(ord(a[times:times+1])+key)
        awnser+=tip
        times+=1
    return awnser#凯撒加密

def re_wy(a,b):#a为输入的蜿蜒加密文本,b为加密次数
    awnser=''#定义结果变量
    wide_1=int(len(a)/2)
    if (len(a)/2)-int(len(a)/2)>0:
        a+='#'
        wide_1=int(len(a)/2)
    b=int(b)
    for times_1 in range(b):
        for times in range(0,wide_1):
            awnser+=a[times::wide_1]
        times_1+=1
    awnser=awnser.rstrip('#')#去除加的#号
    return awnser#解蜿蜒加密

def re_ks(a,b,c):#a为解密文本，b为key
    key=ord(b)#将key转化为编码
    wide=len(a)#获取文本长度
    times=0
    awnser=''#创建结果的变量
    for times in range(wide):
        if c == 0:
            tip=chr(ord(a[times:times+1])-key)
        elif c == 1:
            tip=chr(ord(a[times:times+1])+key)
        awnser+=tip
        times+=1
    return awnser#解凯撒加密

Type=''
while Type != '1':
    Type=input('输入e加密,输入d解密,结束请按1')
    mi_wen=input('加工的文字')
    key_all=input('key')
    key_wide=len(key_all)
    keys=[None] * key_wide#建立key的空列表
    for key_turn in range(key_wide):
        keys[key_turn]=key_all[key_turn]
    if Type == 'e':
        ci_shu=1
        dis_plus=1
        a=keys[0]
        for times_1 in range(key_wide):
            mi_wen=wy(mi_wen,ci_shu)
            true_key=keys[times_1]
            if true_key == a :
                dis_plus=1
                mi_wen=ks(mi_wen,true_key,dis_plus)
            else:
                dis_plus=0
                mi_wen=ks(mi_wen,true_key,dis_plus)
                a=true_key
        print(mi_wen)
    if Type == 'd':
        ci_shu=1
        re_dis_plus=1
        a=keys[0]
        for times_2 in range(key_wide):
            true_key=keys[times_2]
            if true_key == a:
                re_dis_plus=1
                mi_wen=re_ks(mi_wen,true_key,re_dis_plus)
                mi_wen=re_wy(mi_wen,ci_shu)
            else:
                re_dis_plus=0
                mi_wen=re_ks(mi_wen,true_key,re_dis_plus)
                mi_wen=re_wy(mi_wen,ci_shu)
                a=true_key
        print(mi_wen)
