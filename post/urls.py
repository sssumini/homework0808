from django.urls import path, include
from .views import PostViewSet, CommentViewSet, PostCommentViewSet
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

app_name="post"

default_router = routers.SimpleRouter()
default_router.register("posts", PostViewSet, basename="posts")

comment_router = routers.SimpleRouter()
comment_router.register("comments", CommentViewSet, basename="comments")

post_comment_router = routers.SimpleRouter()
post_comment_router.register("comments", PostCommentViewSet, basename="comments")


urlpatterns = [
    path("", include(default_router.urls)),
    path("", include(comment_router.urls)),
    path("posts/<int:post_id>/", include(post_comment_router.urls)),
] 