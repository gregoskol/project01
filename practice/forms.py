from django import forms

from .models import CD, GENRE_CHOICES


class ExchangeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=40)
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    price = forms.DecimalField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)

    def clean_artist(self):
        data = self.cleaned_data['artist']
        if CD.objects.filter(artist=data).exists():
            pass
        else:
            raise forms.ValidationError('Данного исполнителя нет в коллекции')
        return data

