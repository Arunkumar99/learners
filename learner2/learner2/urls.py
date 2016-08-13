"""learner2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('pupil.urls')),
    url(r'^pupil/', include('pupil.urls',namespace='pupil')),
    url(r'^pupil/login/', include('pupil.urls')),
    url(r'^pupil/signup/', include('pupil.urls')),
    url(r'^/signup/', include('pupil.urls')),
    url(r'^/pupil/categories', include('pupil.urls')),
    url(r'^/pupil/c_programming', include('pupil.urls')),
    url(r'^/pupil/test1', include('pupil.urls')),
    url(r'^/pupil/logout', include('pupil.urls')),
    url(r'^/pupil/extract', include('pupil.urls')),
    url(r'^/pupil/result1', include('pupil.urls')),
    url(r'^/pupil/status10', include('pupil.urls')),
    url(r'^/pupil/status11', include('pupil.urls')),
    url(r'^/pupil/test2', include('pupil.urls')), 
    url(r'^/pupil/result2', include('pupil.urls')),
    url(r'^/pupil/status20', include('pupil.urls')),
    url(r'^/pupil/status21', include('pupil.urls')),
    url(r'^/pupil/test3', include('pupil.urls')),
    url(r'^/pupil/result3', include('pupil.urls')),
    url(r'^/pupil/status30', include('pupil.urls')),
    url(r'^/pupil/status31', include('pupil.urls')),
    url(r'^/pupil/beni', include('pupil.urls')),
    url(r'^/pupil/about', include('pupil.urls')),

    url(r'^/pupil/algorithms', include('pupil.urls',namespace='pupil')),
    url(r'^/pupil/test4', include('pupil.urls')),
    url(r'^/pupil/test5', include('pupil.urls')),
    url(r'^/pupil/test6', include('pupil.urls')),
    url(r'^/pupil/result11', include('pupil.urls')),
    url(r'^/pupil/result12', include('pupil.urls')),
    url(r'^/pupil/result13', include('pupil.urls')),
    url(r'^/pupil/status110', include('pupil.urls')),
    url(r'^/pupil/status111', include('pupil.urls')),
    url(r'^/pupil/status120', include('pupil.urls')),
    url(r'^/pupil/status121', include('pupil.urls')),
    url(r'^/pupil/status130', include('pupil.urls')),
    url(r'^/pupil/status131', include('pupil.urls')),

    url(r'^/pupil/ds', include('pupil.urls',namespace='pupil')),
    url(r'^/pupil/test7', include('pupil.urls')),
    url(r'^/pupil/test8', include('pupil.urls')),
    url(r'^/pupil/test9', include('pupil.urls')),
    url(r'^/pupil/result21', include('pupil.urls')),
    url(r'^/pupil/result22', include('pupil.urls')),
    url(r'^/pupil/result23', include('pupil.urls')),
    url(r'^/pupil/status210', include('pupil.urls')),
    url(r'^/pupil/status211', include('pupil.urls')),
    url(r'^/pupil/status220', include('pupil.urls')),
    url(r'^/pupil/status221', include('pupil.urls')),
    url(r'^/pupil/status230', include('pupil.urls')),
    url(r'^/pupil/status231', include('pupil.urls')),

    url(r'^/pupil/dm', include('pupil.urls',namespace='pupil')),
    url(r'^/pupil/test10', include('pupil.urls')),
    url(r'^/pupil/test11', include('pupil.urls')),
    url(r'^/pupil/test12', include('pupil.urls')),
    url(r'^/pupil/result31', include('pupil.urls')),
    url(r'^/pupil/result32', include('pupil.urls')),
    url(r'^/pupil/result33', include('pupil.urls')),
    url(r'^/pupil/status310', include('pupil.urls')),
    url(r'^/pupil/status311', include('pupil.urls')),
    url(r'^/pupil/status320', include('pupil.urls')),
    url(r'^/pupil/status321', include('pupil.urls')),
    url(r'^/pupil/status330', include('pupil.urls')),
    url(r'^/pupil/status331', include('pupil.urls')),

    url(r'^/pupil/python', include('pupil.urls',namespace='pupil')),

    url(r'^/pupil/toc', include('pupil.urls',namespace='pupil')),
    url(r'^/pupil/test13', include('pupil.urls')),
    url(r'^/pupil/test14', include('pupil.urls')),
    url(r'^/pupil/test15', include('pupil.urls')),
    url(r'^/pupil/result41', include('pupil.urls')),
    url(r'^/pupil/result42', include('pupil.urls')),
    url(r'^/pupil/result43', include('pupil.urls')),
    url(r'^/pupil/status410', include('pupil.urls')),
    url(r'^/pupil/status411', include('pupil.urls')),
    url(r'^/pupil/status420', include('pupil.urls')),
    url(r'^/pupil/status421', include('pupil.urls')),
    url(r'^/pupil/status430', include('pupil.urls')),
    url(r'^/pupil/status431', include('pupil.urls')),

    url(r'^/pupil/feedback', include('pupil.urls')),
]

if settings.DEBUG:
  urlpatterns += patterns('django.views.static',(r'media/(?P<path>.*)','serve',{'document_root': settings.MEDIA_ROOT}),)
