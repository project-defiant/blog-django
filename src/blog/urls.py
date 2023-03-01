from django.urls import path

from .views import index, post_detail, posts

urlpatterns = [
    path("", view=index, name="index-page"),
    path("posts", view=posts, name="posts-page"),
    path("posts/<slug:slug>", view=post_detail, name="post-detail-page"),
]
