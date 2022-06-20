from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'posts/index.html')

def boxing(request):
    boxing=Boxing.objects.all()
    return render(request,'posts/boxing.html',{'posts':boxing})

def upload(request):
    upload = BoxingCreate()
    if request.method == 'POST':
        upload = BoxingCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('boxing')
        else:
            return HttpResponse("""Error, reload on <a href= "{{ url : 'boxing' }}">reload</a>""")
    else:
        return render(request, 'posts/upload_from.html', {'upload_from':upload})

def update_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Boxing.objects.get(id = post_id)
    except Boxing.DoesNotExist:
        return redirect('boxing')
    post_form = BoxingCreate(request.POST or None, instance=post_sel)
    if post_form.is_valid():
        post_form.save()
        return redirect('boxing')
    return render(request, 'posts/upload_form.html', {'upload_from':upload})

def delete_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Boxing.objects.get(id = post_id)
    except Boxing.DoesNotExist:
        return redirect('boxing')
    post_sel.delete()
    return redirect('boxing')

def wrestling(request):
    wrestling = Wrestling.objects.all()
    return render(request,'posts/wrestling.html',{'posts':wrestling})

def athletics(request):
    athletics = Athletics.objects.all()
    return render(request,'posts/athletics.html',{'posts':athletics})

def weightlifting(request):
    weightlifting = Weightlifting.objects.all()
    return render(request,'posts/weightlifting.html',{'posts':weightlifting})

def cycling(request):
    cycling = Cycling.objects.all()
    return render(request,'posts/cycling.html',{'posts':cycling})

def team_sports(request):
    team_sports = Team_sports.objects.all()
    return render(request,'posts/team_sports.html',{'posts':team_sports})




