from django import forms
from django.contrib.auth.hashers import check_password

from .models import User

# 회원가입 폼
class UserJoinForm(forms.Form):
    username = forms.CharField(
        label='이름',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    re_password = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(attrs={'class':'form-control'})
    )


    def clean(self):
        # 요청파라미터값 조회
        cleaned_data = super().clean() #dict변환
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        #password == repassword
        if password != re_password:
            self.add_error('password','비밀번호가 다릅니다.')
            self.add_error('re_password','비밀번호가 다릅니다.')

        #이메일 중복 체크
        try:
            User.objects.get(pk=username)
            self.add_error('username', '이미 가입된 이름 입니다.')
        except:
            pass


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    def clean(self):
        cleaned_data = super().clean() #부모에 있는 값을 clean으로 받아오기
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        try:
            user = User.objects.get(pk=username)
            if not check_password(password, user.password):
                self.add_error('password','비밀번호가 틀렸습니다..')
        except:
            self.add_error('username','가입하지 않은 아이디입니다.')


