from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True, verbose_name='사용자명')
    email = models.EmailField(max_length=50, verbose_name='비밀번호')
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
