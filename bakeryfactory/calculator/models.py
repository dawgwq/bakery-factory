from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.name
    

class Resource(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=250)
    measure = models.CharField(max_length=50)
    quantity_availabe = models.FloatField()
    def __str__(self):
        return self.name
    


class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE,default=0)
    quantity_requirement = models.FloatField()
    insctruction = models.TextField()
    def __str__(self):
        return f"Рецепт продукта: {self.product.name}"
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_requirement = models.IntegerField()
    date_created = models.DateTimeField("date published")
    address = models.TextField()
    def __str__(self):
        return f"ID заказа: {self.id}, Адрес заказа: {self.address}"
    
    def calculate_total_resources(self):
        total_resources = {}
        measure = {}
        recipes = Recipe.objects.filter(product=self.product)
        for recipe in recipes:
            resource_name = recipe.resource.name
            quantity_required = recipe.quantity_requirement * self.quantity_requirement
            if resource_name in total_resources:
                total_resources[resource_name] += quantity_required
            else:
                total_resources[resource_name] = quantity_required
            measure[resource_name] = recipe.resource.measure        
        return total_resources, measure
    

        