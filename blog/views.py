from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic

from blog.models import Post
from blog.permissions import AuthorPermissionsMixin, MembersPermissionsMixin


class PostListView(generic.ListView):
    model = Post


@method_decorator(login_required, name='get')
class PostDetailView(MembersPermissionsMixin, generic.DetailView):
    model = Post
    # permission_required = ['blog.view_post']

    # def post(self):
    #     pass

# @method_decorator(login_required, name='post')
# class PostDetailView(generic.View):
#     # @method_decorator(login_required)
#     def get(self, request, pk):
#         return render(request, 'blog/post_detail.html', {'object': Post.objects.get(id=pk)})
#
#     def post(self):
#         pass
