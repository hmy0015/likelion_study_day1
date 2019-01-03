from django.db import models

# Create your models here.
class Hello(models.Model):
    # CharField는 문자열 제한이 있는 필드, 최대 길이를 지정해주어야 함
    title = models.CharField(max_length=20)
    # TextField는 문자열 제한이 큰 필드
    content = models.TextField()
    user = models.CharField(max_length=30)

    # self = 자기 자신 -> Instance
    # Instance.title
    def __str__(self):
        return self.title