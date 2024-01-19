import django_filters
from django import forms
from django_filters import DateFilter
from .models import *

class BidFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_placed", lookup_expr='gte', widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'mm/dd/yyyy'}))
    end_date = DateFilter(field_name="date_placed", lookup_expr='lte', widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'mm/dd/yyyy'}))
    class Meta:
        model = Bid
        fields = '__all__'
        exclude = ['user', 'date_placed', 'offer']