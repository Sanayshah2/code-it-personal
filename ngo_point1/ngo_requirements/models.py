from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Donor(models.Model):

    user = models.OneToOneField(User,default='',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username}"



class Ngo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,default='')
    def __str__(self):
        return f"{self.user.username}"

class Help_category(models.Model):

    help_category = models.CharField(max_length=300,default='')
    def __str__(self):
        return f"{self.help_category}"

class Requirement(models.Model):
    
    requirement_heading=models.CharField(max_length=300,default='')
    requirement_content=models.TextField()
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE, default='')
    category = models.ForeignKey(Help_category,on_delete=models.CASCADE, default='')
    #quantity=models.Field(max_length=300,default='')
    quantity=models.IntegerField(max_length=999999,null=True)
    amount=models.IntegerField(max_length=999999,null=True)
    requirement_fulfilled=models.IntegerField(max_length=255,default=0)
    fulfilled_by=models.ManyToManyField(Donor,related_name='fulfillers')


    # from_ngo=models.ForeignKey(Student,on_delete=models.CASCADE)
    # college=models.CharField(max_length=300,default='',choices=college_choices)
    # branch=models.CharField(max_length=300,blank='true', null='true',choices=branch_choices)
    date_posted =models.DateTimeField(default=timezone.now)
    # date_resolved = models.CharField(default='', max_length = 40)
    # status = models.CharField(choices = status_choices, default='Pending', max_length = 20)
    # response = models.TextField(default='')
    # related_to = models.CharField(choices = related_to_choices, default='', max_length = 20, verbose_name = 'Complain Related to')
    # transfer = models.BooleanField(default=False)
    # likes=models.ManyToManyField(User,related_name='complain')

    # def total_likes(self):
    #     return self.likes.count()

    # def __str__(self):
    #     return f"{self.college} : {self.branch}"


    class Meta:
        ordering=['-date_posted']



