from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from repairs.forms import CustomerForm
from repairs.models import Status


class ListRepair(View):
    template_name = 'repairs.html'

    def get(self, request):
        return render(request, self.template_name)


class CreateRepair(FormView):
    template_name = 'create_repair.html'
    form_class = CustomerForm
    success_url = '/repairs/'

    def form_valid(self, form):
        repair = form.save()
        repair.status = Status.CREATED
        repair.save()
        repair.users.add(self.request.user)
        return super().form_valid(form)
