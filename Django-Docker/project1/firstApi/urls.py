from django.conf.urls import url 
from firstApi import views

urlpatterns = [
    url(r'^api/modelList', views.pytorchModel_list),
    url(r'^api/runModel', views.runModel),
]