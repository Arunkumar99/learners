from django.template import Template,Context
from django.http import HttpResponse
import datetime
def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</br>im new to django enjoying its  funny</br>im new to django enjoying its funny</br>im new to django enjoying its funny</br>im new to django enjoying its funny</br>im new to django enjoying its funny</br>im new to django enjoying its funny</br>im new to django enjoying its funny</br>im new to django enjoying its funny</br>im new to django enjoying its funny</br>im new to django enjoying its funny</body></html>" % now
	return HttpResponse(html)
