from django.utils.translation import gettext as _

from django.forms import (Form, ModelForm, ModelChoiceField,
                          DecimalField, CharField, IntegerField)
from warehouse.models import *

# CRISPY FORMS SPECIFIC
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Submit, Layout, Div, Fieldset
#-------------------------------------------------------------------------------

class AsmbForm(ModelForm):

    versa_sn = ModelChoiceField(queryset=Versa.objects.filter(sn__gt=0),required=True)
    pcba_rev = CharField(required=True)
    pcb_rev = CharField(required=True)
    pcba_sn = IntegerField(required=True)
    osc_sn = IntegerField(required=True)
    gnss_sn = IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        super(AsmbForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'asmb-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Submit',css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            HTML("""<h2>Assembly Form</h2>"""),
            Fieldset('Versasync Serial Number',
                Field('versa_sn')
            ),
            Fieldset('Hardware Revisions',
                Field('pcb_rev', placeholder = ' pcb revision'),
                Field('pcba_rev', placeholder = ' pcba revision')
            ),
            Fieldset('Component Serial Numbers',
                Field('pcba_sn', placeholder = ' pcba s/n'),
                Field('osc_sn', placeholder = ' osc s/n'),
                Field('gnss_sn', placeholder = ' gnss s/n')
            )
        )

    class Meta:
        model = AsmbEntry
        fields = ['versa_sn','pcba_rev','pcb_rev','pcba_sn','osc_sn','gnss_sn']


class ProgForm(ModelForm):

    versa_sn = ModelChoiceField(queryset=Versa.objects.filter(sn__gt=0),required=True)
    sw_ver = CharField(required=True)
    timing_sys_ver = CharField(required=True)
    voltage = DecimalField(required=True)
    current = DecimalField(required=True)

    def __init__(self, *args, **kwargs):
        super(ProgForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'asmb-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Submit',css_class='btn-success'))
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            HTML("""<h2>Programming Form</h2>"""),
            Fieldset('Versasync Serial Number',
                Field('versa_sn')
            ),
            Fieldset('Software Versions',
                Field('sw_ver', placeholder = ' software version'),
                Field('timing_sys_ver', placeholder = ' timing system version')
            ),
            Fieldset('Measured Values',
                Field('voltage', placeholder = ' Voltage'),
                Field('current', placeholder = ' Current')
            )
        )

    class Meta:
        model = ProgEntry
        fields = ['versa_sn', 'sw_ver', 'timing_sys_ver', 'voltage', 'current']
