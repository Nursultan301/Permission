from django.urls import path

from blog.views import PostListView, PostDetailView, GameView

urlpatterns = [
    path('', PostListView.as_view(), name='post'),
    path('game/', GameView.as_view(), name='game'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail')
]
