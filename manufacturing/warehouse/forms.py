from django.utils.translation import gettext as _

from django.forms import (ModelForm, ModelChoiceField, CharField, IntegerField)
from warehouse.models import *

#-------------------------------------------------------------------------------

class AsmbForm(ModelForm):
    versa_sn = ModelChoiceField(queryset=Versa.objects.filter(sn__gt=0),required=True)
    pcba_rev = CharField(required=True)
    pcb_rev = CharField(required=True)
    pcba_sn = IntegerField(required=True)
    osc_sn = IntegerField(required=True)
    gnss_sn = IntegerField(required=True)
    class Meta:
        model = AsmbEntry
        fields = ['versa_sn', 'pcba_rev', 'pcb_rev', 'pcba_sn', 'osc_sn', 'gnss_sn']
        labels = {
            'versa_sn': _('Versasync S/N'),
            'pcba_rev': _('PCBA Revision'),
            'pcb_rev': _('PCB Revision'),
            'pcba_sn': _('PCBA S/N'),
            'osc_sn': _('Oscillator S/N'),
            'gnss_sn': _('GNSS S/N')
        }


class TestForm(ModelForm):
    class Meta:
        model = TestEntry
        fields = ['versa_sn', 'sw_ver', 'timing_sys', 'voltage', 'current']
        labels = {
            'versa_sn': _('Versasync S/N'),
            'sw_ver': _('Software Version'),
            'timing_sys': _('Timing System'),
            'voltage': _('Supply Voltage'),
            'current': _('Supply Current')
        }
