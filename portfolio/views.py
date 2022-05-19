#  hello/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

#from .models import Tarefa
#from .forms import TarefaForm

from .models import Blog_Post
from .models import Language
from .models import Class
from .forms import BlogPostForm
from .forms import QuizForm
from .models import Hobbie
from .models import Quiz

from .functions import build_graph

from django.urls import reverse

# Create your views here.


def home_page_view(request):
    return render(request, 'portfolio/layout.html')

def about_me_page_view(request):
    context = {
        'languages': Language.objects.all(),
        'classes': Class.objects.all(),
        'hobbies': Hobbie.objects.all(),
    }
    return render(request, 'portfolio/about_me.html', context)

def blog_page_view(request):
    context = {'blog_posts': Blog_Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)

@login_required
def edita_blog_post_view(request, blog_post_id):
    session_username = request.user.username
    post_username = (Blog_Post.objects.get(id=blog_post_id).autor)

    if(session_username != post_username):
        print("post username and session username !=")
        return render(
            request, 'portfolio/login.html',
            {'message': "To edit this post you must login with:" + post_username}
        )

    blog_post = Blog_Post.objects.get(id=blog_post_id)
    form = BlogPostForm(request.POST or None, request.FILES, instance=blog_post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog'))

    context = {'form': form, 'blog_post_id': blog_post_id}
    return render(request, 'portfolio/edita.html', context)

@login_required
def nova_blog_post_view(request):
    form = BlogPostForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog'))

    context = {'form': form}

    return render(request, 'portfolio/nova.html', context)

def apaga_blog_post_view(request, blog_post_id):
    Blog_Post.objects.get(id=blog_post_id).delete()
    return HttpResponseRedirect(reverse('blog'))

def web_programming_view(request):

    winner_names = ""
    for quiz in Quiz.objects.all():
        print("#####")
        print(quiz.name)
        winner_names += quiz.name + "; "
    print(winner_names)

    build_graph(Quiz.objects.all())

    form = QuizForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.path_info)

    context = {
        'form': form,
        'winner_names': winner_names
    }

    return render(request, 'portfolio/web_programming.html', context)


def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            context = {'blog_posts': Blog_Post.objects.all()}
            return render(request, 'portfolio/blog.html', context)
        else:
            return render(
                request, 'portfolio/login.html',
                {'message': "Invalid Credentials"}
        )

    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return render(
        request, 'portfolio/login.html',
        {'message': "Logged Out"}
    )