from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['titulo', 'descricao', 'data_inicio', 'hora_inicio', 'data_final', 'hora_final', 'localizacao']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("data_inicio")
        start_time = cleaned_data.get("hora_inicio")
        end_date = cleaned_data.get("data_final")
        end_time = cleaned_data.get("hora_final")

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("A data de término deve ser posterior à data de início.")
            elif end_date == start_date and end_time <= start_time:
                raise forms.ValidationError("A hora de término deve ser posterior à hora de início, quando as datas são iguais.")
