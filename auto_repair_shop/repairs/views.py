from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import FormView, ListView

from repairs.forms import CustomerForm, TechnicianForm, MasterForm, WorkerForm
from repairs.mixins import RepairMixin
from repairs.models import Repair
from users.models import Role

User = get_user_model()


class DetailRepair(RepairMixin, View):
    """Класс представления заявки."""

    template_name = 'detail.html'

    def _get_form(self, repair):
        """Возвращаем форму для роли пользователя."""
        user_form = {
            Role.CUSTOMER: None,
            Role.TECHNICIAN: TechnicianForm(instance=repair),
            Role.MASTER: MasterForm(instance=repair),
            Role.WORKER: WorkerForm(instance=repair),
        }
        return user_form.get(self.request.user.role)

    def get(self, request, pk):
        _filter = self._get_repair_filter(self.request.user)
        repair = get_object_or_404(Repair, pk=pk, **_filter)
        context = {
            'repair': repair,
            'form': self._get_form(repair)
        }
        return render(request, self.template_name, context)


class ListRepair(RepairMixin, ListView):
    """Класс списка заявок."""

    template_name = 'repairs.html'
    model = Repair
    paginate_by = 5

    def get_queryset(self):
        """Возвращаем заявки по её статусу"""
        _filter = self._get_repair_filter(self.request.user)
        return Repair.objects.filter(**_filter)


class CreateRepair(FormView):
    """Класс создания заявки на ремонт автомобиля."""

    template_name = 'create_repair.html'
    form_class = CustomerForm
    success_url = '/repairs/'

    def form_valid(self, form):
        repair = form.save()
        repair.users.add(self.request.user)
        return super().form_valid(form)
