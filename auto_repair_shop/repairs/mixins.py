from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import AccessMixin

from repairs.models import Status
from users.models import Role

User = get_user_model()


class CustomerLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and role is CUSTOMER"""

    def dispatch(self, request, *args, **kwargs):
        if (
                request.user.is_authenticated and
                request.user.role != Role.CUSTOMER
        ):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class RepairMixin:
    """Миксин для фильтрации заявок по роли пользователя."""

    @staticmethod
    def _get_repair_filter(user: User) -> dict:
        """Возвращает фильтр для заявки для роли пользователя."""
        repair_filter = {
            Role.CUSTOMER: {
                'users': user
            },
            Role.TECHNICIAN: {
                'status__in': Status.statuses_for_list_technician()
            },
            Role.MASTER: {
                'status__in': Status.statuses_for_list_master()
            },
            Role.WORKER: {
                'status__in': Status.statuses_for_list_worker()
            }
        }
        return repair_filter.get(user.role)
