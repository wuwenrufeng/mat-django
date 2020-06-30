from django.shortcuts import render
import seaborn as sns
import matplotlib.pyplot as plt
import io
import urllib, base64
# 切换为agg后端，否则只能查看一次页面，第二次出现线程错误
plt.switch_backend('agg')  
sns.set()

def home(request):
    plt.plot(range(10))
    fig = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'home.html',{'data':uri})