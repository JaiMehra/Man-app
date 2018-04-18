from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WarehouseConfig(AppConfig):
    name = 'warehouse'

class WorkOrderPopulation(AppConfig):
    name = 'warehouse'
    verbose_name = _('warehouse')

    def ready(self):
        import warehouse.signals
