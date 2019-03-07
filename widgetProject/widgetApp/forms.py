from django import forms
from .models import Cities

RICH_OR_SUP = (
    ("rich", "Rich"),
    ("superpower", "SuperPower"),
)

YOUR_SUPERPOWER = (
    ("flight", "Flight"),
    ("speed", "Speed"),
    ("invisibility", "Invisibility"),
    ("telekenetic", "Telekenetic"),
    ("healing", "Healing"),
    ("other", "Other"),
)

YOUR_LEVEL = (
    ("good", "Good"),
    ("kinda good", "Kinda good"),
    ("neutral", "Neutral"),
    ("a little evil", "A little evil"),
    ("evil", "Evil"),
)


class CitiesForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = '__all__'
        labels = {
            'name': 'Name',
            'cityOrOrigin': 'Where are you from?',
            'richOrSuperPower': 'Are you rich or have super powers? ',
            'whichSuperPower': 'If you have a super power, which ones?',
            'level': 'Which of the following are you? ',
            'examples': 'Give us 3 examples of when you used your super hero abilities'
        }
        widgets = {
            'richOrSuperPower': forms.Select(choices=RICH_OR_SUP),
            'whichSuperPower': forms.SelectMultiple(choices=YOUR_SUPERPOWER),
            'level': forms.RadioSelect(choices=YOUR_LEVEL),
        }
