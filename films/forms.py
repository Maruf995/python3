from django import forms

from films import parser, models


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Film', 'Film'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'Film':
            films_data = parser.films_parser()
            for i in films_data:
                models.Film.objects.create(**i)
