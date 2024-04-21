from django.forms import ModelForm
from.models import Experimento


class ExperimentoForm(ModelForm):

    class Meta:
        model = Experimento
        fields = '__all__'

    
    