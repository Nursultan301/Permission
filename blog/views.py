from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic, View

from blog.forms import GameForm
from blog.models import Post
from blog.permissions import AuthorPermissionsMixin, MembersPermissionsMixin
from blog.service import Game


# class PostListView(generic.ListView):
#     model = Post
#
#
@method_decorator(login_required, name='get')
class PostDetailView(MembersPermissionsMixin, generic.DetailView):
    model = Post
    permission_required = ['blog.view_post']

    def post(self):
        pass


# @method_decorator(login_required, name='post')
# class PostDetailView(generic.View):
#     # @method_decorator(login_required)
#     def get(self, request, pk):
#         return render(request, 'blog/post_detail.html', {'object': Post.objects.get(id=pk)})
#
#     def post(self):
#         pass
############################## Permissions ##########################################################

########################################### ORM ###################################################
class PostListView(generic.ListView):
    # queryset = Post.custom_manager.custom_filter(author__username='Test1')
    queryset = Post.custom_manager.custom_order_by('-title')


class GameView(View):

    def get(self, request):
        return render(request, 'game/index.html', {'form': GameForm()})

    def post(self, request):
        form = GameForm(request.POST)
        if form.is_valid():
            damage = form.cleaned_data['damage']
            game = Game()
            i_get, i_set = game.set_damage(damage)
        return render(request, 'game/index.html', {'form': GameForm(), 'i_get': i_get, 'i_set': i_set})
