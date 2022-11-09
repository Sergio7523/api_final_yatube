from rest_framework import filters, permissions, mixins, viewsets

from rest_framework.pagination import LimitOffsetPagination
from .permissions import IsOwnerOrReadOnly
from posts.models import Group, Post
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)


def get_post(self):
    post_id = self.kwargs.get('post_id')
    return Post.objects.get(pk=post_id)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,
    )

    def get_queryset(self):
        return get_post(self).comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=get_post(self))


class FollowViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        return self.request.user.follower.all()
