from django.http import HttpResponse
from django.shortcuts import render, redirect
from App_User_Profile.models import Profile
from .models import TblPost
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.

def PostList(request):
    all_posts_data = TblPost.objects.order_by('-timestamp')
    return render(request, 'App_Post/PostList.html', {'all_posts_data': all_posts_data})


@login_required()
def CreatePost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user.profile
            post.save()
            print('Post Created Successfully.')
            return redirect('posts')
    else:
        form = PostForm()
        print('Please Fill Valid Info in Form.')
        return render(request, 'App_Post/PostForm.html', {'form': form})


def UpdatePost(request, id):
    post = get_object_or_404(TblPost, pk=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            print('Post Updated Successfully.')
            return redirect('posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'App_Post/PostForm.html', {'form': form})


def DeletePost(request, id):
    post = get_object_or_404(TblPost, pk=id)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request, 'App_Post/PostDelete.html', {'object': post})
