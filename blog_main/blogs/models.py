from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    Category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta :
        verbose_name_plural = "Categories"
        
    
    def __str__(self):
        return self.Category_name
    
    
STATUS_CHOICES = (
    (0, 'Draft'),
    (1, 'Published'),
)
    
class blog(models.Model):
    title = models.CharField(max_length=200)
    slug  = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image  = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    short_description = models.TextField()
    blog_body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0) # Published
    is_featured = models.BooleanField(default=False)  # Featured
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title