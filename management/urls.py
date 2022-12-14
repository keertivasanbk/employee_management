"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
from employe.views import signout
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',signout,name='logout'),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='/home/keerthivasan/Public/internship_review/employee_management/employee/management/template/common/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='/home/keerthivasan/Public/internship_review/employee_management/employee/management/template/common/password-reset/password_reset_form.html',
             subject_template_name='/home/keerthivasan/Public/internship_review/employee_management/employee/management/template/common/password-reset/password_reset_subject.txt',
             email_template_name='/home/keerthivasan/Public/internship_review/employee_management/employee/management/template/common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='/home/keerthivasan/Public/internship_review/employee_management/employee/management/template/common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='/home/keerthivasan/Public/internship_review/employee_management/employee/management/template/common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='/home/keerthivasan/Public/internship_review/employee_management/employee/management/template/common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('',include('employe.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
