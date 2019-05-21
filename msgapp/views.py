from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse,JsonResponse
# Create your views here.
def msgproc(request):
    datalist=[]
    if request.method== "POST":
        userA=request.POST.get("userA",None)
        userB=request.POST.get("userB",None)
        msg= request.POST.get("msg",None)
        time = datetime.now()
        with open("msgdata.txt",'a+') as f:
            f.write("{}--{}--{}--{}--\n".format(userB,userA,\
                                                  msg,time.strftime("%Y-%m-%d %H:%M:%S")))
    elif request.method == "GET":
        userC = request.GET.get("userC",None)
        if userC != None:
            with open("msgdata.txt","r") as f :
                count = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        count=count+1
                        d = {"userA":linedata[1],'msg':linedata[2]\
                             ,"time":linedata[3]}
                        datalist.append(d)
                        if count>=10:
                            break
    return  render(request,'MsgSingleWeb.html',{'data':datalist})

def homepeag(request):
    return  HttpResponse("<p>这是首页，留言点<a href='./msggate'>这里</a></p>")

# json 请求
# def homepeag1(request):
#     rs=JsonResponse({"key":1})
#     return  rs

