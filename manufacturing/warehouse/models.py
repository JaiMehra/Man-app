from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

STATES = (
    ('0','Not Started'),
    ('1','Assemble'),
    ('2','Program'),
    ('3','Test'),
    ('4','Done')
)

class WorkOrder(models.Model):
    id = models.AutoField(primary_key=True)
    work_order = models.PositiveIntegerField(unique=True)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=1, choices=STATES, default='0')
    

class Versa(models.Model):
    id = models.AutoField(primary_key=True)
    sn = models.PositiveIntegerField(unique=True)
    model_num = models.CharField(max_length=9)
    work_order = models.ForeignKey(WorkOrder, )
    # sale_order = models.PositiveIntegerField()

    # __str__ is used in the admin interface
    def __str__(self):
        return "Versasync S/N:{}".format(self.sn)


class Task(models.Model):

    id = models.AutoField(primary_key=True)
    versa_sn = models.ForeignKey(Versa, to_field='sn', related_name='task_versa_sn',on_delete=models.CASCADE)
    task_type = models.CharField(max_length=1, choices=STATES, default='0')
    starter = models.ForeignKey(User, related_name='task_starter', null=True, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    finisher= models.ForeignKey(User, related_name='task_ender', null=True, blank=True, on_delete=models.CASCADE)
    finished_time = models.DateTimeField(null=True, blank=True)

    def get_id(self):
        return self.id

    def __str__(self):
        return "{} task for {} started on {}".format(
            self.get_task_type_display(),
            self.versa_sn,
            self.start_time.strftime("%m/%d/%Y-%H:%M:%S"))


class AsmbEntry(models.Model):
    id = models.AutoField(primary_key=True)
    versa_sn = models.OneToOneField(Versa, to_field='sn', related_name='asmb_versa_sn', on_delete=models.CASCADE)
    pcba_rev = models.CharField(max_length=2)
    pcb_rev = models.CharField(max_length=2)
    pcba_sn = models.PositiveIntegerField(unique=True)
    osc_sn = models.PositiveIntegerField(unique=True)
    gnss_sn = models.PositiveIntegerField(unique=True)
    task_id = models.ForeignKey(Task, to_field='id', null=True, blank=True,related_name='asmb_task_id', on_delete=models.CASCADE)

    def __str__(self):
        return "Assembly entry {} for {}".format(self.id, self.versa_sn)


class ProgEntry(models.Model):
    id = models.AutoField(primary_key=True)
    versa_sn = models.ForeignKey(Versa, to_field='sn', related_name='test_versa_sn',on_delete=models.CASCADE)
    sw_ver = models.CharField(max_length=100)
    timing_sys_ver = models.CharField(max_length=100)
    voltage = models.DecimalField(max_digits=5, decimal_places=3)
    current = models.DecimalField(max_digits=4, decimal_places=3)
    task_id = models.ForeignKey(Task, to_field='id', null=True, blank=True,related_name='prog_task_id', on_delete=models.CASCADE)

    def __str__(self):
        return "Programming entry {} for {}".format(self.id, self.versa_sn)

    def power(self):
        return self.voltage * self.current
