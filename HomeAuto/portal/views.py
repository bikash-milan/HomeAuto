from django.shortcuts import redirect,render

from django.contrib.auth.models import User

from django.contrib.auth import login,authenticate,logout

from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=='POST':
        username= request.POST['username']

        if request.POST['password1']==request.POST['password2']:
            password = request.POST['password1']
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            messages.success(request, 'User Crerated')
        else:
            return redirect('index')
    return render(request,'index.html')


def Login(request):
    if request.user.is_anonymous:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return render(request,'dashboard.html')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('index')
        else:
            return redirect('index')
    else:
        return redirect('index')

def Logout(request):

    logout(request)
    return redirect('index')
