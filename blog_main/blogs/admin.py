from django.contrib import admin

# Register your models here.
from .models import Category
from .models import blog




class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}   # slug auto fill from title
    list_display = ('title','category', 'status', 'is_featured' ,'created_at', 'updated_at') # list display with fields
    search_fields = ('title', 'category__Category_name')  # search fields
    list_editable = ( 'is_featured',)  # editable fields in list display 
admin.site.register(Category)
admin.site.register(blog, blogAdmin)
