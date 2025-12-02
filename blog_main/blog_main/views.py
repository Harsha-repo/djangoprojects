from django.contrib import admin
from django.shortcuts import render

from blogs.models import Category
from blogs.models import blog

def home(request):
    categories = Category.objects.all()
    featured_posts = blog.objects.filter(is_featured=True).order_by('updated_at')
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
    }
    print(categories)
    print("is featured ",featured_posts)
    return render(request, 'home-blogs.html', context)
