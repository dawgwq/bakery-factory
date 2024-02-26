from django.contrib import admin
from .models import *
# Register your models here.
class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]

admin.site.register(Resource)
admin.site.register(Product, ProductAdmin) 
admin.site.register(Order)