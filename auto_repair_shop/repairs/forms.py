from django import forms
from django.contrib.auth import get_user_model

from repairs.models import Repair, Auto, PlacesToWork, TypeRepair, Parts, Status
from users.models import Role

User = get_user_model()


class WorkerForm(forms.ModelForm):
    """Форма для работы с заявками для слесаря."""

    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[
            item for item in Status.choices if item[0] in (
                'PROGRESS', 'TESTS',
            )
        ]
    )

    class Meta:
        model = Repair
        fields = (
            'status',
        )


class MasterForm(forms.ModelForm):
    """Форма для работы с заявками для мастера."""

    parts = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        queryset=Parts.objects.all(),
    )
    users = forms.ModelMultipleChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=User.objects.filter(role=Role.WORKER),
    )
    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[
            item for item in Status.choices if item[0] in (
                'CONFIRMED', 'READY_TO_WORK', 'RE_REPAIR',
            )
        ]
    )

    class Meta:
        model = Repair
        fields = (
            'parts',
            'users',
            'status',
        )


class TechnicianForm(forms.ModelForm):
    """Форма для работы с заявкой для техников."""

    description = forms.CharField(
        label='Описание поломки',
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )
    time_to_work = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"class": "form-control"}),
    )
    places_to_work = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=PlacesToWork.objects.all(),
    )
    type_repair = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=TypeRepair.objects.all(),
    )
    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[
            item for item in Status.choices if item[0] == 'CONFIRMED'
        ]
    )

    class Meta:
        model = Repair
        fields = (
            'description',
            'time_to_work',
            'places_to_work',
            'type_repair',
            'status',
        )


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
