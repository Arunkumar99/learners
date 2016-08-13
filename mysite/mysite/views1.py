from django.template import Template,Context
from django.http import HttpResponse
import datetime
def hello(request):
    now = datetime.datetime.now()
    html="<html><body>current time %s.</br>im new to django</br>well i will learn it completely any how<script>a=2;b=3;c=a+b</script></body></html>"%now
    return HttpResponse(html)
