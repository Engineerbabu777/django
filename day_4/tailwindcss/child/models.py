from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KL", "KIWI"),
        ("PL", "PLAIN"),
        ("EL", "ELACHI"),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    # description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
# ONE TO MANY!
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
    
# MANY TO MANY!
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety,related_name="stores")
    
    def __str__(self):
        return f'{self.name}'
   
# ONE TO ONE!
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.chai.name}'
        