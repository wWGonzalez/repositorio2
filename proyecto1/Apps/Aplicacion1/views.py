from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
	template_name='index.html'

class EstudianteView(TemplateView):
	template_name='Estudiante.html'

class AdministradoresView(TemplateView):
	template_name='Administradores.html'

class AcercaDeView(TemplateView):
	template_name='AcercaDe.html'
