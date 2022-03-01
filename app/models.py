from django.db import models

# Create your models here.
class Visitors(models.Model):
    soni=models.IntegerField()
    date_entered=models.DateTimeField(auto_now_add=True)
class Profile(models.Model):
    image=models.ImageField(upload_to='profile_images')
    def __str__(self):
        return self.image.url
    def imageShow(self):
        return self.image.url
class Resume(models.Model):
    cv=models.FileField(upload_to='cv')
    def __str__(self):
        return f"CV"
    class Meta:
        verbose_name='Resume'
        verbose_name_plural="Resumelar"
    
class Lessons(models.Model):
    image=models.ImageField(upload_to='lesson_images')
    url=models.URLField()
    title=models.CharField(max_length=600)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Dars'
        verbose_name_plural="Darslar"

class Portfolio(models.Model):
    image=models.ImageField(upload_to='portfolio_images')
    url=models.URLField()
    title=models.CharField(max_length=600)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Portfolio'
        verbose_name_plural="Portfoliolar"
class SofialLinks(models.Model):
    phone=models.CharField(max_length=300)
    telegram=models.URLField()
    facebook=models.URLField()
    instagram=models.URLField()
    linkedin=models.URLField()
    youtube=models.URLField()
    def __str__(self):
        return "Ijtimoiy tarmoqlar"
    class Meta:
        verbose_name='SocialLink'
        verbose_name_plural="SocialLinks"


class Xabar(models.Model):
    name=models.CharField(max_length=500)
    subject=models.CharField(max_length=400)
    text=models.TextField()
    def __str__(self):
        return f"{self.name} nomli shaxs xabar yubordi!"
    class Meta:
        verbose_name='Xabar'
        verbose_name_plural="Xabarlar"


    