from django.shortcuts import render, get_object_or_404
from .forms import CommentForm, PostForm, UserInfoForm, UserProfileInfoForm
from .models import Post, Comment, UserInfo

from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'simple_app/about.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



@login_required
def likes_post(request, id):

    post = get_object_or_404(Post, id=id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(f"/{id}")

@login_required
def your_posts(request):

    obj = Post.objects.filter(author = request.user)

    return render(request, 'simple_app/users_post_list.html', {'posts':obj})

@login_required
def users_post_list(request, id):

    post = Post.objects.get(id=id)
    obj = Post.objects.filter(author = post.author)

    return render(request, 'simple_app/users_post_list.html', {'posts':obj})

@login_required
def favourite_list(request):

    user = request.user
    favourites = user.favourite.all()
    context = {
        'posts': favourites,
    }
    return render(request, 'simple_app/favourites.html', context)

@login_required
def add_favourite_post(request, id):

    post = get_object_or_404(Post, id=id)
    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
    else:
        post.favourite.add(request.user)

    return HttpResponseRedirect(f"/{id}")

@login_required
def profile_edit(request):

    if request.method == 'POST':
        form = UserInfoForm(request.POST or None, instance=request.user)
        profile_form=UserProfileInfoForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():

            user = form.save()
            user.set_password(user.password)
            update_session_auth_hash(request, user)
            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            if 'profile_image' in request.FILES:
                print('found it')

                profile.user.picture = request.FILES['profile_image']

            profile.save()
            return HttpResponseRedirect('profile')


    else:
        form = UserInfoForm(instance=request.user)
        profile_form=UserProfileInfoForm(instance=request.user)


    return render(request, 'simple_app/profile_edit.html', {'form':form, 'profile_form':profile_form})



@login_required
def profile_info(request):
    return render(request, 'simple_app/profile_info.html')

@login_required
def post_edit(request, id):

    context = {}
    obj = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f"/{id}")

    context["form"] = form

    return render(request, 'simple_app/post_edit.html', context)


@login_required
def post_delete(request, id):

    obj = get_object_or_404(Post, id = id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(reverse('list_post'))

    return render(request, 'simple_app/post_delete.html')



def post_detail(request, id):


    post = Post.objects.get(id=id)
    comments = Comment.objects.all()
    is_liked = False
    is_favourite = False

    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    if post.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(f"/{id}")

    else:
        form = CommentForm()

    context = {'post':post, 'comments':comments,'total_likes':post.total_likes(), 'comments_form':form, 'is_liked':is_liked, 'is_favourite':is_favourite}
    return render(request, 'simple_app/post_detail.html', context)


def list_post(request):

    context = {}
    context['posts'] = Post.objects.all()

    return render(request, 'simple_app/post_list.html', context)


@login_required
def create_view(request):

    context = {}
    form = PostForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.author = request.user
        obj.save()
        return HttpResponseRedirect(reverse('list_post'))

    context['form']= form
    return render(request, 'simple_app/create_view.html', context)


def registration(request):

    registered = False
    if request.method == 'POST':

        us_form = UserInfoForm(data = request.POST)
        profile_form=UserProfileInfoForm(data = request.POST)

        if us_form.is_valid() and profile_form.is_valid():

            user = us_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')

                profile.profile_pic = request.FILES['profile_pic']

            profile.save()


            registered = True

        else:
            print(us_form.errors)
    else:
        us_form = UserInfoForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'simple_app/registration.html', {'user_form':us_form, 'registered':registered,'profile_form':profile_form})

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('list_post'))
            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponse('invalid details')
    else:
        return render(request, 'simple_app/login.html')

@login_required
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():

            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(f"/{id}")
        else:
            form = CommentForm
    return render(request, 'simple_app/post_detail.html', {'form':form})
