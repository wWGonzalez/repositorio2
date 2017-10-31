

from django.conf.urls import url,include
from .views import IndexView,EstudianteView,AdministradoresView,AcercaDeView


urlpatterns = [
	url(r'^$', IndexView.as_view()),
	url(r'^Estudiante$', EstudianteView.as_view()),
	url(r'^Administradores$', AdministradoresView.as_view()),
	url(r'^AcercaDe$', AcercaDeView.as_view()),
]