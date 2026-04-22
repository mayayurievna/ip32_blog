from django.shortcuts import render, redirect
from .models import User, Role
from .forms import UserForm, RoleForm
from .decorators import login_required, is_director, is_manager, is_aothorized

def index(request):
    if request.session.get('user_id'):
        u_id = request.session.get('user_id')
        u = User.objects.get(id=u_id)
        return render(request, 'index.html', {'user': u})
    else:
        return redirect('/login/')

@is_aothorized
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

@login_required
def for_authorized(request):
    u_id = request.session.get('user_id')
    u = User.objects.get(id=u_id)
    return render(request, 'page_for_authorized.html', {'user': u})

@is_director
def for_director(request):
    u_id = request.session.get('user_id')
    u = User.objects.get(id=u_id)
    return render(request, 'page_for_director.html', {'user': u})

@is_manager
def for_manager(request):
    u_id = request.session.get('user_id')
    u = User.objects.get(id=u_id)
    return render(request, 'page_for_manager.html', {'user': u})

def add_user(request):
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
        return redirect('/users/')
    else:
        form = UserForm()
        return render(request, "add_user.html", {'form': form})
    
def add_role(request):
    if request.method == "POST":
        role = RoleForm(request.POST)
        if role.is_valid():
            role.save()
        return redirect('/users/')
    else:
        form = RoleForm()
        return render(request, "add_role.html", {'form': form})

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        login = request.POST.get('login')
        password = request.POST.get('pas')

        try:
            user = User.objects.get(login=login)
        except User.DoesNotExist:
            print('нет такого пользователя')
            return redirect('/login')
        
        if password != user.password:
            print('неверный пароль')
            return redirect('/login')
        
        request.session['user_id'] = user.id
        request.session['login'] = user.login
        return redirect('/')

def logout_view(request):
    request.session.flush()
    return redirect('/login')