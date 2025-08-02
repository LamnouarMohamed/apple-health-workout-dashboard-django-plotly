from django import forms
import datetime

class DateForm(forms.Form):
    YEAR_CHOICES = [(year, year) for year in range(2020, datetime.datetime.now().year + 5)]
    year = forms.ChoiceField(choices=YEAR_CHOICES, label='Year')

    MONTH_CHOICES = [(i, str(i)) for i in range(1, 13)]
    month = forms.ChoiceField(choices=MONTH_CHOICES, label='Month')

    ACTIVITY_CHOICES = [
        ('running', 'Running'),
        ('walking', 'Walking'),
    ]
    activity = forms.ChoiceField(choices=ACTIVITY_CHOICES, label='Activity Type')