from django.shortcuts import render, get_object_or_404, reverse 
from django.views import generic, View
from django.http import HttpResponseRedirect 
from .models import Post
from django.contrib import messages  
from .models import UserProfile 
from .forms import CommentForm 


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html" 


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on") 
        profile = get_object_or_404(UserProfile, user=request.user)     
        liked = False  
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True   

        return render(
            request,
            "blog/blog_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
                "profile": profile,                  
            }, 
        ) 
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on") 
        profile = get_object_or_404(UserProfile, user=request.user)  
        username = request.user  
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username 
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save(request.user.username ) 
            messages.success(request,
                             'Your comment has been posted') 
        else:
            comment_form = CommentForm()
            messages.warning(request,
                             'Something went wrong. Please Try Again')
    
        template = "blog/blog_detail.html" 
        context = {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(), 
                "profile": profile, 
                "username": username,    
        } 
        return render(request, template, context)   


class PostLike(View):
   
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        profile = UserProfile.objects.get(user=request.user) 
        print('USER: ', request.user) 
        print('USER Profile: ', profile) 
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(profile)
        else:
            post.likes.add(profile)


        return HttpResponseRedirect(reverse('post_detail', args=[slug])) 
