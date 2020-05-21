"""data_sources URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from nces_data_api import views as views_nces
from cwift_data import views as views_cwift

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nces_json/', views_nces.nces_json, name="nces_json"),
    path('nces_table/', views_nces.nces_table, name="nces_table"),
    path('cwift_data/', views_cwift.CWIFTALLView.as_view()),
    path('cwift_json/', views_cwift.cwift_json, name="cwift_json"),
    path('cwift_pd_table/', views_cwift.cwift_table),
    path('cwift_table/', views_cwift.table),
    path('cwift_scatter/', views_cwift.scatter),
    path('sample/', views_cwift.sample_render),
    path('cwift_bar/', views_cwift.bar)
    # path('cwift_data/get_cwift', views_cwift.get_cwift,)

]
