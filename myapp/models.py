from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class school(models.Model):
    mat=models.CharField(max_length=20,unique=True,null=False)
    tent=models.CharField(max_length=100,null=False,unique=True)
    def __str__(self):
          return f'{self.mat,self.tent}'
class khoa(models.Model):
    mak=models.CharField(max_length=20,unique=True,null=False)
    tenk=models.CharField(max_length=40,unique=True,null=False)
    def __str__(self):
          return f'{self.mak,self.tenk}'
          
class sinhvien(models.Model):
        masv=models.CharField(max_length=20,unique=True,null=False)
        tensv=models.CharField(max_length=30)
        school=models.ForeignKey(school,on_delete=models.CASCADE,related_name="sinhviens")
        khoa=models.ForeignKey(khoa,on_delete=models.CASCADE,related_name="sinhviens")
        lop=models.CharField(max_length=10)
        image=models.ImageField(upload_to="image",null=False)
        gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))

        def __str__(self) -> str:
              return f"{self.masv,self.tensv,self.school,self.khoa,self.lop,self.image,self.gender}"
class comment(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      text=models.TextField()
      create_time=models.DateTimeField(auto_now_add=True)
      def __str__(self):
            return f'{self.user,self.text,self.create_time}'
      

