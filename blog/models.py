from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name
class Tag(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        verbose_name='标签'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
class Post(models.Model):
    title=models.CharField('标题',max_length=70)
    body=models.TextField('正文')
    create_time=models.DateTimeField('创建时间',default=timezone.now())
    modified_time=models.DateTimeField('最后修改时间')
    category=models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE)
    excerpt=models.CharField('摘要',max_length=200,blank=True)
    tag=models.ManyToManyField(Tag,verbose_name='标签',blank=True)
    author=models.ForeignKey(User,verbose_name='作者',on_delete=models.CASCADE)
    def save(self,*args,**kwargs):
        self.modified_time=timezone.now()
        super().save(*args,**kwargs)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    class Meta:
        verbose_name='文章'
        verbose_name_plural=verbose_name