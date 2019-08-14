from django.contrib import admin
from django.urls import path
from myapp.views import objects_output

urlpatterns = [
    path('admin/', admin.site.urls),
    path('objects_output/', objects_output, name='objects-output')
]
