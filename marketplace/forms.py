from django import forms

from .models import Auction, Category

import datetime

this_year = datetime.date.today().year

class AuctionForm(forms.ModelForm):
    
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      initial=Category.objects.get(name = 'Other'),
                                      empty_label=None,
                                      required = False)

    class Meta:
        model = Auction
        fields = ['name', 'category', 'price', 'photo', 'description']


class AuctionFilterForm(forms.ModelForm):
    name = forms.CharField(required=False,
                           label='',
                           widget=forms.TextInput(
                                attrs={'placeholder': 'Name'})
                            )

    date_from = forms.DateField(label='From mm/dd/yy:',
                                required=False,
                                widget=forms.SelectDateWidget(
                                    years = range(this_year, this_year - 10, -1))
                                )

    date_to = forms.DateField(label='To mm/dd/yy:',
                              required=False,
                              widget=forms.SelectDateWidget(
                                years = range(this_year, this_year - 10, -1))
                              )

    price_from = forms.DecimalField(decimal_places=2,
                                    required=False,
                                    label='',
                                    widget=forms.NumberInput(
                                        attrs={'placeholder': 'Price From'})
                                    ) 

    price_to = forms.DecimalField(decimal_places=2,
                                    required=False,
                                    label='',
                                    widget=forms.NumberInput(
                                        attrs={'placeholder': 'Price To'})
                                    ) 

    price_sort = forms.ChoiceField(choices=(('', ''), ('ASC', 'Ascending'), ('DESC', 'Descending')),
                                  required=False,
                                  label='Sort by price:'
                                  )                             


    class Meta:
        model = Auction
        fields = ('name', 'date_from', 'date_to', 'price_from', 'price_to', 'price_sort')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)     

