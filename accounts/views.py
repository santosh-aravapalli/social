from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserProfileForm,UserUpdateForm
from django.views.generic.base import View
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User


class UserRegisterView(View):

    def get(self, request):
        form = UserRegisterForm()
        P_form = UserProfileForm()
        return render(request, 'register.html', {'form': form, "p_form": P_form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        P_form = UserProfileForm(request.POST)
        if form.is_valid() and P_form.is_valid():
            user = form.save()
            profile = P_form.save(commit=False)
            profile.user = user
            profile.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {name}')
            return redirect('Post')
        else:
            return redirect('register')


class PaswdResetView(PasswordResetView):
    template_name = 'paswd.html'


class UserUpdateView(LoginRequiredMixin,View):
    def get(self,request):
        form = UserUpdateForm(instance=request.user)
        return render(request,'update.html',{'form':form})

    def post(self,request):
        form=UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f'Account for {name} is updated')
        return redirect('home')
