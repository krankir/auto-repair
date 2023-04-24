from django.contrib.auth import get_user_model
from django.views.generic import FormView, ListView

from repairs.forms import CustomerForm
from repairs.models import Status, Repair
from users.models import Role

User = get_user_model()


class ListRepair(ListView):
    """Класс списка заявок."""

    template_name = 'repairs.html'
    model = Repair
    paginate_by = 5

    def get_queryset(self):
        """Возвращаем заявки по её статусу"""
        queryset = []
        user: User = self.request.user

        if user.role == Role.CUSTOMER:
            queryset = Repair.objects.filter(users=user)

        elif user.role == Role.TECHNICIAN:
            queryset = Repair.objects.filter(
                status__in=Status.statuses_for_list_technician(),
            )

        elif user.role == Role.MASTER:
            queryset = Repair.objects.filter(
                status__in=Status.statuses_for_list_master()
            )

        elif user.role == Role.WORKER:
            queryset = Repair.objects.filter(
                status__in=Status.statuses_for_list_worker()
            )

        return queryset


class CreateRepair(FormView):
    """Класс создания заявки на ремонт автомобиля."""

    template_name = 'create_repair.html'
    form_class = CustomerForm
    success_url = '/repairs/'

    def form_valid(self, form):
        repair = form.save()
        repair.status = Status.CREATED
        repair.save()
        repair.users.add(self.request.user)
        return super().form_valid(form)
