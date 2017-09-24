from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'periodo', PeriodoViewSet)
router.register(r'materia', MateriaViewSet)
router.register(r'grado', GradoViewSet)
router.register(r'seccion', SeccionViewSet)
router.register(r'seccion-get', SeccionGetViewSet)
router.register(r'matricula', MatriculaViewSet)
router.register(r'matricula-get', MatriculaGetViewSet)
urlpatterns = [

    url(r'^', include(router.urls)),
    
]

