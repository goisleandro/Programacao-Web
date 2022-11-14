"""inf1407 URL Configuration

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
from django.contrib import admin                                                            #padrão
from django.urls import path                                                                #padrão
from django.contrib.auth.views import LoginView, LogoutView                                 #login/out/senha
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView            #password
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView              #password
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView   #password
from django.views.generic.edit import UpdateView                                            #perfil do usuario
from django.contrib.auth.models import User                                                 #perfil do usuario
from django.urls.base import reverse_lazy

# Importações particulares
from trabalho2 import views
from trabalho2.views import MeuUpdateView #mesmo lugar de settings!!!

urlpatterns = [
    # Aplicação de páginas básicas ################################################################
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('segundaPagina', views.segundaPagina, name='segunda'),

    # Aplicação Contatos ##########################################################################
    path('lista/', views.ContatoListView.as_view(), name='lista-contatos'),
    path('cria/', views.ContatoCreateView.as_view(), name='cria-contato'),
    path('atualiza/<int:pk>/', views.ContatoUpdateView.as_view(), name='atualiza-contato'),
    path('apaga/<int:pk>/', views.ContatoDeleteView.as_view(), name='apaga-contato'),

    # Controle de acesso ##########################################################################
    path('accounts/', views.homeSec, name='sec-home'),
    path('accounts/registro/', views.registro, name='sec-registro'),
    path('accounts/login/', LoginView.as_view(template_name='trabalho2/registro/login.html',), name='sec-login'),
    path('accounts/profile/', views.paginaSecreta, name='sec-paginaSecreta'),
    path('logout/', LogoutView.as_view( next_page=reverse_lazy('sec-paginaSecreta'), ), name='sec-logout'),

    # Perfil do usuário ###########################################################################
    path('accounts/terminaRegistro/<int:pk>/', MeuUpdateView.as_view( 
            template_name='trabalho2/registro/user_form.html',
            success_url=reverse_lazy('sec-home'), 
            model=User, 
            fields=[ 'first_name', 'last_name', 'email', ], #fields=[ '__all__' ], 
        ), name='sec-completaDadosUsuario'),

    # passwordchange

    path('accounts/password_change/', PasswordChangeView.as_view(
            template_name='trabalho2/registro/password_change_form.html',
            success_url=reverse_lazy('sec-password_change_done'),
        ), name='sec-password_change'),
    path('accounts/password_change_done/',PasswordChangeDoneView.as_view(
            template_name='trabalho2/registro/password_change_done.html',
        ), name='sec-password_change_done'),





    path('accounts/password_reset/', PasswordResetView.as_view(
        template_name='trabalho2/registro/recupera/password_reset_form.html',
        success_url=reverse_lazy('sec-password_reset_done'),
        html_email_template_name='trabalho2/registro/recupera/email/password_reset_email.html',
        subject_template_name='trabalho2/registro/recupera/email/password_reset_subject.txt',
        from_email='goisleandro@gmail.com',
        ), name='password_reset'),
    path('accounts/password_reset_done/', PasswordResetDoneView.as_view(
        template_name='trabalho2/registro/recupera/password_reset_done.html',
        ), name='sec-password_reset_done'),
    path('accounts/password_reset_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
        template_name='trabalho2/registro/recupera/password_reset_confirm.html',
        success_url=reverse_lazy('sec-password_reset_complete'),
        ), name='password_reset_confirm'),
    path('accounts/password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='trabalho2/registro/recupera/password_reset_complete.html'
        ), name='sec-password_reset_complete'),

]