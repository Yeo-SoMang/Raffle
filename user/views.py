from django.shortcuts import render, redirect
from django.views.generic import FormView
# 패스워드 암호화 해주는 함수.
from django.contrib.auth.hashers import make_password
from .forms import UserJoinForm, LoginForm
from .models import User

# Create your views here.
# 가입처리
class JoinView(FormView):
    template_name = 'User/signup.html'
    form_class = UserJoinForm
    success_url = '/'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data  # dict
        email = cleaned_data.get('email')
        password = make_password(cleaned_data.get('password'))  # 암호화
        username = cleaned_data.get('username')
        user = User(email=email, password=password, username=username)
        user.save()

        return super().form_valid(form)


# 로그인 처리 View
class LoginView(FormView):
    template_name = 'User/login.html'
    form_class = LoginForm
    success_url = '/'
    # 메인으로
    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        username = cleaned_data.get('username')
        # db에 저장되어 있는 email
        # Session객체-dictionary 형태:key-value쌍이 필요
        # 로그인 -> session에 로그인 여부를 확인할 수 있는 체크값을 넣어둔다.
        self.request.session['User'] = username
        # request: HttpRequest(사용자 HTTP 요청정보)
        return super().form_valid(form)


# 로그 아웃
def logout(request):
    request.session.clear()

    return redirect('/')
