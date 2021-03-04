
class MyModelBaseViewSet:

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(owner=self.request.user)
        return queryset
