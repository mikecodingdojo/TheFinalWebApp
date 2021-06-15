from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages
from django.conf import settings




def index(request):
        
    return render(request, 'index.html')

def dashboard(request):
    images = Upload.objects.all()
    profile_image = UploadProfile.objects.all()
    
    context = {
            'user': User.objects.get(id=request.session['id']), 
            'images':images,
            'profile_image':profile_image
    
        } 
    return render(request, 'dashboard.html', context)

def success(request): 
    if 'user' not in request.session:
        return redirect('/')
    
    context = {
        'wall_messages': Wall_Message.objects.all(), 
        'photo': Upload.objects.all()
        
    }
    return render(request, 'feed.html', context)

def register(request): 
    print("reg32")
    # Create a user object
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
        print("Reg 43")
    return redirect('/user_dashboard')

def login(request):
    print("login")
    if request.method=="POST":
        print("line 48 ")
        errors = User.objects.login_validator(request.POST)
        if len(errors)>0:
            print("Inside Line 51")
            for key, value in errors.items():
                messages.error(request, value)
                print("line 54")
            return redirect('/')
        print("56")
        # retrieving a user from the db
        logged_user = User.objects.filter(email=request.POST['email'])
        print("Line 59", logged_user)
        if len(logged_user) > 0:
            print("Login 2")
            logged_user = logged_user[0]
            if logged_user.password == request.POST['password']:
                print("Line 63")
                request.session['user'] = logged_user.first_name
                request.session['id'] = logged_user.id
                print("loging 3")
                return redirect('/user_dashboard')
                print("line 68")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def process_message(request):
        if request.POST['mess']=='':
            return redirect('/success')
        else:
            Wall_Message.objects.create(message=request.POST['mess'], poster=User.objects.get(id=request.session['id']))
            return redirect('/success')
        
    

def post_comment(request, id):
    #create
    poster = User.objects.get(id=request.session['id'])
    message = Wall_Message.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], poster=poster, wall_message=message)
    return redirect('/success')

def add_like(request, id):
    liked_message = Wall_Message.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/success')

def delete_comment(request, id):
    destroyed = Comment.objects.get(id=id)
    destroyed.delete()
    return redirect('/success')
    
def delete_message(request, id):
    destroyed = Wall_Message.objects.get(id=id)
    destroyed.delete()
    return redirect('/success')

def edit(request, id):
    edit_user = User.objects.get(id=id)
    edit_user.first_name = request.POST['first_name']
    edit_user.last_name = request.POST['last_name']
    edit_user.email = request.POST['email']
    edit_user.save()
    return redirect('/success')

def linklogin(request):
    return render(request, 'login.html')

def regpage(request):
    return render(request, 'register.html')

def add_images(request):
    if request.method == "POST":
        new_file = Upload(file=request.FILES['image'], imgpost=User.objects.get(id=request.session['id']))
        new_file.save()
        return redirect("/user_dashboard")


def largerpicture(request):
    picture = Upload.objects.all()
    
    context = {
        "picture":picture 
        
        
    }
    return render(request, 'largerpicture.html', context)

def dashpost(request):
    if request.POST['post']=='':
            return redirect('/user_dashboard')
    else:
        Wall_Message.objects.create(message=request.POST['post'], poster=User.objects.get(id=request.session['id']))
        return redirect('/success')

def photodel(request, id):
    destroyed = Upload.objects.get(id=id)
    destroyed.delete()
    return redirect('/largerpicture')

