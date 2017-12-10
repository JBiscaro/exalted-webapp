from django.forms import ModelForm
from calculator.models import Charm


class CharmForm(ModelForm):
    class Meta:
        model = Charm
        fields = ('name', 'description')
