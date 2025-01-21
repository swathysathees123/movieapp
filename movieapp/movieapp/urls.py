
from django.contrib import admin
from django.urls import path
from watch_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='hello_world'),
    path('pos', views.pos),
    path('del', views.delete)

]
