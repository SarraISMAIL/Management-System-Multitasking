from django.urls import path
from . import views
app_name='demo'
urlpatterns = [
    path('',views.index,name="index"),
    path('computer-specs',views.coputerSpecs,name="specs"),
    path('nots',views.nots,name="nots"),
    path('kill_process/<int:id>/',views.kill_process,name="kill_process"),
    path('kill/<int:id>/',views.kill,name="kill"),
    path('test/',views.test,name="chart"),
]