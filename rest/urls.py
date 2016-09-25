"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import get_articles,change_article,ArticleViewSet,CategoryViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'articles',ArticleViewSet)
router.register(r'categories',CategoryViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^articles/$', get_articles, name = 'articles'),
#     url(r'^article/(?P<pk>\d+)/$', change_article, name = 'change_article'),
#
# ]
