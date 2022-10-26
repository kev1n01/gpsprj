from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import buses, drivers, students, stopPoints, travelRegisters, users, travelRegisterDetails

router = routers.DefaultRouter()
router.register('users',users )
router.register('buses', buses)
router.register('drivers', drivers)
router.register('students', students)
router.register('travelRegisters', travelRegisters)
router.register('travelRegistersDetails', travelRegisterDetails)
router.register('stopPoints', stopPoints)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apirest/', include(router.urls)),
    path('api/', include('api.urls')),
]
