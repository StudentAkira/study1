import django_filters
from django import forms


class PostFilter(django_filters.FilterSet):

    subscriptions_only = django_filters.BooleanFilter(
        field_name='author',
        method='subscriptions_only_method',
        label='Only subscriptions : ',
        widget=forms.CheckboxInput,
    )

    def subscriptions_only_method(self, queryset, name, value):
        if value:
            queryset = queryset.filter(author__followed__follower=self.request.user)
            print(queryset, self.request.user)
        return queryset