import re
from django.db import models
from django.forms import ValidationError
# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name="제목") # 길이제한(CharField)
    content = models.TextField() # 길이제한(TextField) X
    tags = models.CharField(max_length=100,blank=True)
    Inglat = models.CharField(max_length=50,validators=[lnglat_validator], blank=True, help_text='위도경도포맷으로입력')
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)

    # 밑에 두개는 값을 대입할 필요가 없다
    created_at = models.DateTimeField(auto_now_add=True) # 최초생성 할때 저장
    updated_at = models.DateTimeField(auto_now=True)# 해당record가 갱신할때마다 저장

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title