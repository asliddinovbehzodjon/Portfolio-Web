from django.shortcuts import redirect, render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import * 
# developer
#django

from .sendsms import sendTelegram
# Create your views here.
def mainpage(request):
    cvs=Resume.objects.all()
    user=Visitors.objects.get(id=1)
    user.soni=user.soni+1
    user.save()
    profile=Profile.objects.all()
    links=SofialLinks.objects.all()
    all_post=Paginator(Lessons.objects.all(),3)
    all_portfolio=Paginator(Portfolio.objects.all(),3)
    page=request.GET.get('page',1)
    try:
        lessons=all_post.page(page)
    except PageNotAnInteger:
       lessons=all_post.page(1)
    except EmptyPage:
        lessons=all_post.page(all_post.num_pages)
    try:
        portfolios=all_portfolio.page(page)
    except PageNotAnInteger:
       portfolios=all_portfolio.page(1)
    except EmptyPage:
        portfolios=all_portfolio.page(all_post.num_pages)
    context={'profile':profile,'links':links,'posts':lessons,'portfolios':portfolios,'cvs':cvs}
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        text=f"⭐️Yangi Xabar⭐️\n"\
             f"Xabar mavzusi: {subject}\n"\
             f"Xabar yuborgan shaxs: {name}\n"\
             f"Xabar: {message}"

        sendTelegram(text)
        Xabar.objects.create(name=name,subject=subject,text=message)
        
        return redirect('/')
   
   
    return render(request,'index.html',context=context)
    
def error(request,exception):
    return render(request,'404.html')
    