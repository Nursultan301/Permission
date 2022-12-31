from django.urls import path

from blog.views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail')
]