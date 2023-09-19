# from django.shortcuts import render
# from.models import User
# from django.http import HttpResponse,HttpResponseRedirect


# em=None
# p_word=None
# # Create your views here.
# def home(req):
#     return render(req,'details/index.html')

# def signup1(req):
#     global em
    
#     em=req.POST.get('email')
#     return render(req,'details/signup1.html')

# def signup2(req):
#     return render(req,'details/signup2.html')


# def signup3(req):
#     return render(req,'details/signup3.html',{'em':em})


# def signin(req):
#     return render(req,'details/sign_in.html')


# def complete(req):
#     if req.method=='POST':
#         p_word = req.POST.get('p_word')
#         u = User(user_id=em,password=p_word)
#         u.save()
#         print('User Created')
#         return render (req,'details/sign_in.html')
#     else:
#         return HttpResponse('bad gateway')
    



# def signin(req):
#     if req.method=='POST':
#         signin_id=req.POST.get('signin_id')
#         signin_password=req.POST['signin_password']

#     try:
#         user = User.objects.get(user_id=signin_id)
#         if user.password==signin_password:
#             return HttpResponse("login successfull")     
#         else:
#               return HttpResponse("incorrect password")
        
#     except User.DoesnotExist:
#             return HttpResponse("user does not exist") 
#     return render(req, 'signin.html') 

# def login(req) :
#     return render(req,'details/sign_in.html')
    
# --------------------------------------------------------------------------------------------------------

from django.shortcuts import render
from .models import User
from django.http import HttpResponse,HttpResponseRedirect

# em is a variable to temproprily hold the email value and render it in 3rd page
em = None
p_word = None

# Create your views here.
def home(req):
    return render(req,'details/index.html')

def signup1(req):
    # we declared em as global variable to increase the scope of the variable into the program
    global em
    em=req.POST.get('email')
    return render(req,'details/signup1.html')

def signup2(req):
    return render(req,'details/signup2.html')

def signup3(req):
    return  render(req,'details/signup3.html',{'em':em})


# sign up logic for database storage
def complete(req):
    if req.method=='POST':
        p_word = req.POST.get('p_word')
        u = User(user_id=em,password=p_word)
        u.save()
        print('User Created')
        return render(req,'details/sign_in.html')
    else:
        return HttpResponse("BAD GATEWAY!!")

def signin(req):
    if req.method=='POST':
        signin_id=req.POST.get('signin_id')
        signin_password=req.POST['signin_password'] 

    try:
        user = User.objects.get(user_id=signin_id)
        if user.password==signin_password:
            return HttpResponse("Login successfull")
        else:
                return HttpResponse("Incorrect password")
    except User.DoesNotExist:
            return HttpResponse("User does not exist")
    
    return render(req, 'signin.html')

def login(req):
     return render(req,'details/sign_in.html')