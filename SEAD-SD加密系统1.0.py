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
            tip=chr(ord(a[times:times+1])+key)
        else:
            tip=chr(ord(a[times:times+1])-key)
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
        if c == 1:
            tip=chr(ord(a[times:times+1])+key)
        elif c == 0:
            tip=chr(ord(a[times:times+1])-key)
        awnser+=tip
        times+=1
    return awnser#解凯撒加密

Type=''
while Type != '1':
    Type=input('输入e加密，输入d解密，结束请按1')
    if Type == 'e':
        mi_wen=input('加密的文字')
        ci_shu=1
        mi_ma_1=input('key-1')
        mi_ma_2=input('key-2')
        dis_plus=1
        mi_wen=wy(mi_wen,ci_shu)
        mi_wen=ks(mi_wen,mi_ma_1,dis_plus)
        mi_wen=wy(mi_wen,ci_shu)
        if mi_ma_1 != mi_ma_2:
            plus_de=0
        mi_wen=ks(mi_wen,mi_ma_2,plus_de)
        print(mi_wen)
    if Type == 'd':
        mi_wen=input('解密的文字')
        ci_shu=1
        mi_ma_1=input('key-1')
        mi_ma_2=input('key-2')
        re_dis_plus=0
        if mi_ma_1 != mi_ma_2:
            re_dis_plus=1
        mi_wen=re_ks(mi_wen,mi_ma_2,re_dis_plus)
        mi_wen=re_wy(mi_wen,ci_shu)
        re_dis_plus=0
        mi_wen=re_ks(mi_wen,mi_ma_1,re_dis_plus)
        mi_wen=re_wy(mi_wen,ci_shu)
        print(mi_wen)
