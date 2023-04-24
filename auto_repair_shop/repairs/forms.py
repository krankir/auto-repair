from django import forms

from repairs.models import Repair, Auto


class CustomerForm(forms.ModelForm):
    """Форма для оформления заявки на ремонт."""

    description = forms.CharField(
        label='Описание поломки',
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )
    auto = forms.ModelChoiceField(
        label='Выберите автомобиль',
        widget=forms.Select(attrs={"class": "form-control"}),
        queryset=Auto.objects.all()
    )

    class Meta:
        model = Repair
        fields = ('description', 'auto')
