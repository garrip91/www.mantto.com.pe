"""ManttoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ManttoApp.views import HomePageView, CategoryNoticiasView, CertificacionesView, ContactoView, CategoryNoticiasLaprimeraetapadelcondominiokentiafueentregadaeneltiempoestimadoView

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'), # MANTTO
    path('category/noticias/', CategoryNoticiasView.as_view(), name='category_noticias'), # BLOG
    path('category/noticias/laprimeraetapadelcondominiokentiafueentregadaeneltiempoestimado/', CategoryNoticiasLaprimeraetapadelcondominiokentiafueentregadaeneltiempoestimadoView.as_view(), name='category_noticias_laprimeraetapadelcondominiokentiafueentregadaeneltiempoestimado'), # BLOG/La primera etapa del Condominio Kentia fue finalizada y entregada en el plazo estimado
    path('certificaciones/', CertificacionesView.as_view(), name='certificaciones'), # CERTIFICACIONES
    path('contacto/', ContactoView.as_view(), name='contacto'), # CONTACTO
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)