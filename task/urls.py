from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from taskList import views as v1


router = routers.DefaultRouter()

#tasklist
router.register(r'task', v1.taskListSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
