"""afin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.routers import SimpleRouter

from core_module.api import CoreListView
from articles.views import DocumentViewSet, AuthorsListViewSet, AutocompleteAuthors, AutocompletePublishers

router = SimpleRouter()

router.register(r'articles', DocumentViewSet)
# router.register(r'authors', AuthorsListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', CoreListView.as_view()),
    path('authors/', AutocompleteAuthors.as_view()),
    path('publishers/', AutocompletePublishers.as_view()),
]

urlpatterns += router.urls
