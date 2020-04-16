from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import ListView
from django.views.generic.base import View
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from .models import Post
from django.views.generic.edit import CreateView,UpdateView


class BaseView(View):

    def get(self,request):
        return render(request,'base.html')


class PostView(PermissionRequiredMixin,CreateView):
    login_url = '/login/'
    permission_required = ('app1.add_post','app1.view_post','app1.delete_post')
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = '/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = 'postlist.html'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class NewView(View):
    def get(self,request):
        return HttpResponse('Hello World')


def test(user):
    if user.username == 'santosh':
        print(user.username)
        return None
    else: return True


@user_passes_test(test_func=test,login_url='/login/')
def GetPassView(request):
    return HttpResponse('User Pass The test')


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'app1.change_post'
    login_url = '/login/'
    success_url = '/new/'
    model = Post
    form_class = PostForm
    template_name = 'post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:return False









'''
class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

class PostAjaxView(AjaxableResponseMixin,CreateView):
    model = Post
    fields = "__all__"
    template_name = 'PostAjax.html'
'''