from django.shortcuts import render
from .models import One2one,Many2one,Many2Many,User
# Create your views here.
def home(request):
    return render(request,'enroll/home.html')

def user_data(request):
    dataall=User.objects.all()
    data1=User.objects.filter(email='sahu@gmail.com')
    data2=User.objects.filter(one2one__publish_date="2021-06-17")
    data3=User.objects.filter(many2one__song_duration=8)
    data4=User.objects.filter(many2many__song_name='Satisfya')
    context={'dataall':dataall,'data1':data1,'data2':data2,'data3':data3,'data4':data4}
    return render(request,'enroll/user.html',context)

def Onedata(request):
    dataall=One2one.objects.all()
    data1=One2one.objects.filter(page_title='Slayer')
    data2=One2one.objects.filter(publish_date='2021-06-17')
    data3=One2one.objects.filter(page_cat='Winterfall')
    context={'dataall':dataall,'data1':data1,'data2':data2,'data3':data3}
    return render(request,'enroll/one.html',context)


def Manydata(request):
    dataall=Many2one.objects.all()
    data1=Many2one.objects.filter(song_name='Vande')
    #data2=Many2one.objects.filter(user=1)
    data3=Many2one.objects.filter(song_duration=8)
    context={'dataall':dataall,'data1':data1,'data3':data3}
    return render(request,'enroll/many21.html',context)

def Manymanydata(request):
    dataall=Many2Many.objects.all()
    data1=Many2Many.objects.filter(song_name='Tera hone')
    data3=Many2Many.objects.filter(song_duration=8)
    context={'dataall':dataall,'data1':data1,'data3':data3}
    return render(request,'enroll/many2many.html',context)