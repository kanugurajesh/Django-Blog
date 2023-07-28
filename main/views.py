from django.shortcuts import render,redirect
from .forms import RegisterForm,PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login,authenticate,logout
from .models import Post

# Create your views here.
@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = Post.objects.filter(id=post_id).first()
        if post and (post.author == request.user or request.user.has_perm('main.delete_post')):
            post.delete()

    return render(request, 'main/home.html',{"posts":posts})

@login_required(login_url='/login')
@permission_required('main.add_post', raise_exception=True, login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()
    
    return render(request, 'main/create_post.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign-up.html', {'form': form})

@login_required(login_url='/login')
def edit_post(request,post_id):
    post = Post.objects.filter(id=post_id).first()
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'main/edit_post.html', {'form': form})