from django.http import Http404


class AuthorPermissionsMixin:
    def has_permissions(self):
        return self.get_object().author == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class MembersPermissionsMixin(AuthorPermissionsMixin):
    def has_permissions(self, ):
        return self.request.user in self.get_object().members.all()



