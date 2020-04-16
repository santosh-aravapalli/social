"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from social import settings
from app1.views import BaseView,PostView,NewView,GetPassView,PostListView,PostUpdateView
from accounts.views import UserRegisterView,PaswdResetView,UserUpdateView
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetDoneView,PasswordChangeView,PasswordChangeDoneView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',BaseView.as_view(),name = 'home'),
    path('post/',PostView.as_view(),name='Post'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('new/',NewView.as_view(),name='new'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('pass/',GetPassView,name = 'passing'),
    path('list/',PostListView.as_view(),name='list'),
    #path('postajax/',PostAjaxView.as_view(),name='postajax'),
    path('<int:pk>/update/',PostUpdateView.as_view(),name='PostUpdate'),
    path('passwd_reset/',PaswdResetView.as_view(),name='passwd-change'),
    path('passwd_change/',PasswordChangeView.as_view(template_name='paswd.html'),name='passwd-reset'),
    path('passwd_change_done/',PasswordChangeDoneView.as_view(template_name='base.html'),name='password_change_done'),
    path('password_rest_done',PasswordResetDoneView.as_view(template_name='Rest_done.html'),name='password_reset_done'),
    path('user_update/',UserUpdateView.as_view(),name='user-update'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

