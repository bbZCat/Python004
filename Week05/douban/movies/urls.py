from django.urls import path
from . import views #从当前目录载入views.py

urlpatterns = [
    path('', views.index) #匹配所有，调用views.py里面的index函数
]