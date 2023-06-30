from django.shortcuts import render
from .models import BlogPost

#Created a method blog_post_list to render to the html template to display the results
def blog_post_list(request):
    blog_posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'blog_post_list.html', {'blog_posts': blog_posts})

