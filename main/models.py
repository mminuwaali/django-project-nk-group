from django.db import models

def portfolio_image_upload(self, image) -> str:
    return f'portfolio/{self.category.name}/{self.name}/{image}'

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to='clients')
    
    def __str__(self) -> str:
        return self.name.title()
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject =models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self) -> str:
        return f'{self.name} - {self.subject} - {self.created_at}'


class Featured(models.Model):
    bootstrap_icon_class = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    content = models.TextField()
    
    class Meta:
        verbose_name_plural = "featured"
    
    def __str__(self) -> str:
        return self.name

class Icon(models.Model):
    icon = models.FileField(upload_to='icons')
    name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
    

class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to=portfolio_image_upload)
    category = models.ForeignKey('PortfolioCategory', on_delete=models.CASCADE, related_name='category')
    
    def __str__(self) -> str:
        return self.name.title()
    
    
class PortfolioCategory(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self) -> str:
        return self.name.title()

class Service(models.Model):
    bootstrap_icon_class = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
    
class Subscribe(models.Model):
    email = models.EmailField()
    subscribed_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Subscribers'
        
    def __str__(self) -> str:
        return self.email