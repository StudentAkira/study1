import django_filters
from django import forms


class PostFilter(django_filters.FilterSet):

    subscriptions_only = django_filters.BooleanFilter(
        field_name='author',
        method='subscriptions_only_method',
        label='Only subscriptions : ',
        widget=forms.CheckboxInput,
    )

    subscribers_only = django_filters.BooleanFilter(
        field_name='author',
        method='subscribers_only_method',
        label='Only subscribers : ',
        widget=forms.CheckboxInput,
    )

    def subscriptions_only_method(self, queryset, name, value):
        if value:
            queryset = queryset.\
                prefetch_related('author__followed').\
                filter(author__followed__follower=self.request.user)
        return queryset

    def subscribers_only_method(self, queryset, name, value):
        if value:
            queryset = queryset.\
                prefetch_related('author__follower').\
                filter(author__follower__followed=self.request.user)
        return queryset
