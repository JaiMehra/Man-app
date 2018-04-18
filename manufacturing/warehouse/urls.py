from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [
    path('assembly_form/',views.AsmbFormView.as_view(),name='assembly_form'),
    path('prog_form/',views.ProgFormView.as_view(),name='prog_form'),
    path('report/',views.ReportView.as_view(),name='report'),
]
