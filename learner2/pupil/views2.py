from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from pupil.forms import User_infoForm,LoginForm
from pupil.models import User_info,Questions2,User_data,FeedBack,SessionData
from django.http import HttpResponseRedirect
from datetime import timedelta
from django.utils import timezone
from django.contrib.sessions.backends.db import SessionStore

#machine learning imports
import random
import sqlite3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os
import subprocess
import pandas as pd
import numpy as np
import scipy as sp
from sklearn import tree
from StringIO import StringIO
from pylab import *

#global vars
key = 0
qualified = 0
session_count = 0
level = 0
sess_data = 0

# Create your views here.

from django.http import HttpResponse

def ds(request):
	context = RequestContext(request)
	response = render_to_response('pupil/ds.html', context)
	questid = int(request.COOKIES.get('questid', '0'))
	response.set_cookie('questid',questid+1)
	return response

def extract2(request):
	context = RequestContext(request)
	time = request.POST['disp']
	t = int(time[1:3])
	print t
	time = (180-(60*int(time[1:3])+int(time[4:6])))
	print time
	answer = request.POST['option']
	hint = request.POST['hints']
	user_id = request.session['userid']
	uid = User_info.objects.filter(name=user_id).values('id')
	uid = User_info.objects.get(id=uid)
	obj = User_data(ans=answer,hint=hint,time=timedelta(seconds=time),user=uid)	
	obj.save()
	questid = int(request.COOKIES.get('questid', '0'))
	if questid <=11:
			return HttpResponseRedirect('/pupil/test7')
	elif (questid >= 11) and (questid <= 21) :
			return HttpResponseRedirect('/pupil/test8')
	else:
			return HttpResponseRedirect('/pupil/test9')


def test7(request):
	context = RequestContext(request)
	i = int(request.COOKIES.get('questid'))
	a = [0,0,0,0,0,0,0,0,0,0]
	num = Questions2.objects.count()
	if (i<=10) :
		question = Questions2.objects.values_list('question',flat=True).get(pk=i)
		option1 = Questions2.objects.values_list('option1',flat=True).get(pk=i)
		option2 = Questions2.objects.values_list('option2',flat=True).get(pk=i)
		option3 = Questions2.objects.values_list('option3',flat=True).get(pk=i)
		option4 = Questions2.objects.values_list('option4',flat=True).get(pk=i)
		hint1 = Questions2.objects.values_list('hint1',flat=True).get(pk=i)
		hint2 = Questions2.objects.values_list('hint2',flat=True).get(pk=i)
		hint3 = Questions2.objects.values_list('hint3',flat=True).get(pk=i)
		hint4 = Questions2.objects.values_list('hint4',flat=True).get(pk=i)
	else:
		return HttpResponseRedirect('/pupil/result21')
	context_dict = {'set_id':"Set-1",'question': str(i)+":-\n\t"+question,'option1': option1,'option2': option2,'option3': option3,'option4': option4,'hint1': hint1,'hint2': hint2,'hint3': hint3,'hint4': hint4}
	response = render_to_response('pupil/testtemp2.html',context_dict,context)
	response.set_cookie('questid',i+1)
	return response

def test8(request):
	context = RequestContext(request)
	i = int(request.COOKIES.get('questid'))
	a = [0,0,0,0,0,0,0,0,0,0]
	num = Questions2.objects.count()
	if (i<=20) :
		question = Questions2.objects.values_list('question',flat=True).get(pk=i)
		option1 = Questions2.objects.values_list('option1',flat=True).get(pk=i)
		option2 = Questions2.objects.values_list('option2',flat=True).get(pk=i)
		option3 = Questions2.objects.values_list('option3',flat=True).get(pk=i)
		option4 = Questions2.objects.values_list('option4',flat=True).get(pk=i)
		hint1 = Questions2.objects.values_list('hint1',flat=True).get(pk=i)
		hint2 = Questions2.objects.values_list('hint2',flat=True).get(pk=i)
		hint3 = Questions2.objects.values_list('hint3',flat=True).get(pk=i)
		hint4 = Questions2.objects.values_list('hint4',flat=True).get(pk=i)
	else:
		return HttpResponseRedirect('/pupil/result22')
	context_dict = {'set_id':"Set-2",'question': str(i)+":-\n\t"+question,'option1': option1,'option2': option2,'option3': option3,'option4': option4,'hint1': hint1,'hint2': hint2,'hint3': hint3,'hint4': hint4}
	response = render_to_response('pupil/testtemp2.html',context_dict,context)
	response.set_cookie('questid',i+1)
	return response

def test9(request):
	context = RequestContext(request)
	i = int(request.COOKIES.get('questid'))
	a = [0,0,0,0,0,0,0,0,0,0]
	num = Questions2.objects.count()
	if (i<=num) :
		question = Questions2.objects.values_list('question',flat=True).get(pk=i)
		option1 = Questions2.objects.values_list('option1',flat=True).get(pk=i)
		option2 = Questions2.objects.values_list('option2',flat=True).get(pk=i)
		option3 = Questions2.objects.values_list('option3',flat=True).get(pk=i)
		option4 = Questions2.objects.values_list('option4',flat=True).get(pk=i)
		hint1 = Questions2.objects.values_list('hint1',flat=True).get(pk=i)
		hint2 = Questions2.objects.values_list('hint2',flat=True).get(pk=i)
		hint3 = Questions2.objects.values_list('hint3',flat=True).get(pk=i)
		hint4 = Questions2.objects.values_list('hint4',flat=True).get(pk=i)
	else:
		return HttpResponseRedirect('/pupil/result23')
	context_dict = {'set_id':"Set-3",'question': str(i)+":-\n\t"+question,'option1': option1,'option2': option2,'option3': option3,'option4': option4,'hint1': hint1,'hint2': hint2,'hint3': hint3,'hint4': hint4}
	response = render_to_response('pupil/testtemp2.html',context_dict,context)
	response.set_cookie('questid',i+1)
	return response

def result21(request):
	global session_count,level,qualified,sess_data
	level = level+1
	sess_data = sess_data+1
	print session_count
	context = RequestContext(request)
	userid = request.session['userid']
	print userid
	f=open('/home/unknown/Django_web/Django-1.8.5/learner2/datain1.csv','r+')
	conn = sqlite3.connect('/home/unknown/Django_web/Django-1.8.5/learner2/db.sqlite3')
	cursor=conn.execute("select id,name from pupil_user_info;")                                                                                                                            																	
	for row0 in cursor:	
		if row0[1]==userid:
			uid = row0[0]
			print uid
	cursor1=conn.execute("select ans,hint,time from pupil_user_data where user_id=%d;" % uid)
	cursor2=conn.execute("select rans from pupil_questions2 where set_id='1';")
	j=0
	row3 = [0,0,0,0,0,0,0,0,0,0]
	row4 = [0,0,0,0,0,0,0,0,0,0]
	for row1 in cursor2:
  		row1 = list(row1)
  		print row1
  		row3[j] = row1[0]
  		j = j+1
	j=0
	for row in cursor1:
  		row = list(row)
  		row[0] = int(row[0])
  		row[1] = int(row[1])
  		row[2] = int(row[2])
  		row[2] = row[2]/1000000
  		print row 
  		if row3[j] == row[0]:
    			row[0] = 1
    			row4[j] = row[0]
    			j = j+1	
  		else:
    			row[0] = 0
    			row4[j] = row[0]
    			j = j+1														
  		for i in range(3):
  			f.write(str(row[i])+',\t')
  		f.write('\n')
	print "fine"
	f.close();
	conn.commit();
	conn.close();

	data2 = sp.genfromtxt("datain1.csv",dtype=int,delimiter=',\t')
	print data2
	data1 = sp.genfromtxt("traindata1.csv",dtype=int,delimiter=',\t')
	print data1
	target = ["low","low","high","high","high","high","high","mid","mid","mid","mid","mid"]
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(data1,target)
	out = StringIO()
	out = tree.export_graphviz(clf, out_file='output1.dot')
	result = clf.predict(data2)
	print result

	obj=['low','mid','high']
	pos =np.arange(len(obj))
	high=mid=low=0
	for i in result:
  	  if(i=='high'):
    		high=high+1
  	  elif(i=='mid'):
    		mid=mid+1
  	  else:
    		low=low+1
	print low,mid,high
	fig1 = figure(1,figsize=(5,5))
	title('How much you know about what you know?!')
	performance=[low,mid,high]
	plt.barh(pos,performance,align="center",color=('blue','brown','green'),alpha=0.9)
	plt.xlim(0, 10)
	grid(True)
	plt.yticks(pos,obj)
	ylabel('Performance scale')
	xlabel('Number of questions')
	fig1.savefig('/home/unknown/Django_web/Django-1.8.5/learner2/static/img/fig11.png')
	plt.clf()

	al,th,kn,ni=2,2,2,2
	fig2 = figure(2,figsize=(6,5))
	width=0.2
	labels = 'Thinking','Analyzing','Knowledge','Need to improve'
	pos = np.arange(len(labels))
	high=mid=low=0
	for i in result:
  		if(i=='high'):
    		 	high=high+1
  		elif(i=='mid'):
    			mid=mid+1
 		else:
    			low=low+1
	if high==10 :
		al,th,kn=99.7,99.4,99.8
	elif(mid==10):
		al,th,kn,ni=79,85,75,38
	elif(low>=9):
		ni=99
	elif high>=7 and mid>=3 and low<=2:
		al,th,kn,ni=82,86,90,25
	elif high>=7 and mid<=3 and low<=2:
		al,th,kn,ni=88,86,80,24
	elif high>=5 and mid>=4 and low<=3:
		al,th,kn,ni=68,79,70,40
	elif high>=6 and mid<=4 and low<=3:
		al,th,kn,ni=75,79,74,38
	elif high>=4 and mid<=5 and low<=3:
		al,th,kn,ni=65,72,70,38
	elif mid>=7 and low<=3 and high<=3:
		al,th,kn,ni=62,60,62,58
	elif mid>=4 and low<=3 and high<=3:
		al,th,kn,ni=58,60,62,57
	elif mid<=6 and low>=4 and high<=3:
		al,th,kn,ni=42,40,46,62
	elif high>=4 and mid>=3 and low<=3:
		al,th,kn,ni=60,64,57,45
	elif high>=3 and mid>=4 and low<=3:
		al,th,kn,ni=58,60,52,54
	elif high<=3 and mid<=3 and low>=9:
		al,th,kn,ni=18,20,14,95
	elif low>=1 and mid<=4 and high<=3:
		al,th,kn,ni=28,32,22,84
	elif low>=4 and mid<=5 and high<=5:
		al,th,kn,ni=36,42,48,72
	elif low>=3 and mid<=7 and high<=4:
		al,th,kn,ni=32,38,35,80
	elif high>=6 and low<=4 and mid<=3: 
		al,th,kn,ni=58,60,62,55
	elif high<=5 and low>=4 and mid<=4:
		al,th,kn,ni=30,32,35,75
	elif mid<=6 and low>=5 and high<=3:
		al,th,kn,ni=33,35,36,77
	elif high>=4 and mid<=7 and low>=3:
		al,th,kn,ni=62,66,68,39
	elif high>=3 and mid<=3 and low>=3:
		al,th,kn,ni=18,20,22,89
	else:
		al,th,kn,ni=50,50,50,50


	
	title("Learner's Proficiency", bbox={'facecolor':'grey', 'alpha':0.5, 'pad':4})
	fracs = (th,al,kn,ni)
	plt.bar(pos+width,fracs,width,color=('lightcoral','y','g','b'))
	plt.ylim(0,100)
	plt.xlim(0, 4)
	plt.xticks(pos+width+0.1,labels)
	fig2.savefig('/home/unknown/Django_web/Django-1.8.5/learner2/static/img/fig12.png')
	plt.clf() 

	data4 = sp.genfromtxt("traindata12.csv",dtype=str,delimiter=',')
	print data4
	target1 = ["q","q","q","nq","nq","nq","nq","q","q","nq","q","q","nq","q","q","nq","q","nq","nq","q","q","nq"]

	i=j=0

	for i in range(22):
 		for j in range(10):
  			if data4[i][j]=='high':
  				data4[i][j]= 2.0
  			elif data4[i][j]=='mid':
  				data4[i][j]= 1.0
  			else:
  				data4[i][j]= 0.0

	print data4

	for j in range(10):
  		if result[j]=='high':
  			result[j]= 2.0
  		elif result[j]=='mid':
  			result[j]= 1.0
  		else:
  			result[j]= 0.0
	clf1 = tree.DecisionTreeClassifier()
	clf1 = clf1.fit(data4,target1)
	out1 = StringIO()
	out1 = tree.export_graphviz(clf1, out_file='output12.dot')
	result1 = clf1.predict(result)
	result1.reshape(1,-1)
	print result1

	q=nq=0
	flag=0
	fig3 = figure(3, figsize=(5, 5))
	ax = axes([0.27, 0.1, 0.57, 0.8])
	ax.annotate('', xy=(-0.83,0.00), xytext=(0.80, -0.00), arrowprops=dict(arrowstyle="-"))
	ax.annotate('Threshold', xy=(-0.5,0.13), xytext=(-0.25, 0.056))

	labels = 'Reached','Need to improve'

	print low,mid,high
	
	if((high+mid-2) > low):
	   flag=0
	   print flag
	else:
	   flag=1
	   print flag

	if flag == 0:
		if high==10:
			q,nq=100,0
			print q,nq
		elif(mid==10):
			q,nq=87.9,(100-87.9)
			print q,nq
		elif high>=7 and mid>=3 and low<=2:
			q,nq=82,(100-82)
			print q,nq
		elif high>=5 and mid>=5 and low<=3:
			q,nq=67,(100-67)
			print q,nq
		elif high<=8 and mid<=9 and low<=3:
			q,nq=74,(100-74)
			print q,nq
		elif high<=6 and mid<=9 and low<=3:
			q,nq=66,(100-66)
			print q,nq
		elif high>=5 and low<=4 and mid<=7:
			q,nq=68,(100-68)
			print q,nq
		elif mid>=7 and low<=3 and high<=3:
			q,nq=72,(100-72)
			print q,nq
		elif mid>=4 and low<=3 and high<=3:
			q,nq=62,(100-62)
			print q,nq
		elif high>=4 and mid<=8 and low<=3:
			q,nq=70,(100-70)
			print q,nq
		elif high>=4 and mid>=3 and low<=4:
			q,nq=56,(100-56)
			print q,nq
		elif high>=4 and mid>=4 and low<=4:
			q,nq=54,(100-54)
			print q,nq
		else:
			q,nq=50,(100-50)
			print q,nq

	else:
		if low==10:
			nq,q=100,0
		elif high<=3 and mid<=3 and low>=9:
			nq,q=82,(100-82)
		elif mid<=6 and low>=5 and high<=3:
			nq,q=68,(100-68)
		elif low>=6 and mid<=5 and high<=4:
			nq,q=72,(100-72)
		elif low>=4 and mid<=5 and high<=5:
			nq,q=60,(100-60)
		elif high<=4 and mid<=4 and low>=3:
			nq,q=70,(100-70)
		elif high<=4 and low>=4 and mid>=3:
			nq,q=58,(100-58)
		else:
			q,nq=50,(100-50)
  
	title("Learner's competence", bbox={'facecolor':'grey', 'alpha':0.5, 'pad':4})
	fracs = [q,nq]
	explode = (0.04,0.0)
	pie(fracs, explode=explode, labels=labels, colors=('g','w'), autopct='%1.0f%%', shadow=False ,radius=0.8)
	fig3.savefig('/home/unknown/Django_web/Django-1.8.5/learner2/static/img/fig13.png') 
	plt.clf()

	percentage = (high+mid-2)*10

	s = SessionData(user_id = userid,result = result1[0],level = 1,percent = percentage,session_count = session_count)
	s.save()

	if result1[0]=='q':
		qualified = 1
		return HttpResponseRedirect('/pupil/status210')
	else:
		return HttpResponseRedirect('/pupil/status211')

def result22(request):
	global session_count,level,qualified,sess_data
	level = level+1
	sess_data = sess_data+1
	print session_count
	context = RequestContext(request)
	userid = request.session['userid']
	print userid
	f=open('/home/unknown/Django_web/Django-1.8.5/learner2/datain1.csv','r+')
	conn = sqlite3.connect('/home/unknown/Django_web/Django-1.8.5/learner2/db.sqlite3')
	cursor=conn.execute("select id,name from pupil_user_info;")                                                                                                                            																	
	for row0 in cursor:	
		if row0[1]==userid:
			uid = row0[0]
			print uid
	cursor1=conn.execute("select ans,hint,time from pupil_user_data where user_id=%d;" % uid)
	cursor2=conn.execute("select rans from pupil_questions2 where set_id='1';")
	j=0
	row3 = [0,0,0,0,0,0,0,0,0,0]
	row4 = [0,0,0,0,0,0,0,0,0,0]
	for row1 in cursor2:
  		row1 = list(row1)
  		print row1
  		row3[j] = row1[0]
  		j = j+1
	j=0
	for row in cursor1:
  		row = list(row)
  		row[0] = int(row[0])
  		row[1] = int(row[1])
  		row[2] = int(row[2])
  		row[2] = row[2]/1000000
  		print row 
  		if row3[j] == row[0]:
    			row[0] = 1
    			row4[j] = row[0]
    			j = j+1	
  		else:
    			row[0] = 0
    			row4[j] = row[0]
    			j = j+1														
  		for i in range(3):
  			f.write(str(row[i])+',\t')
  		f.write('\n')
	print "fine"
	f.close();
	conn.commit();
	conn.close();

	data2 = sp.genfromtxt("datain2.csv",dtype=int,delimiter=',\t')
	print data2
	data1 = sp.genfromtxt("traindata2.csv",dtype=int,delimiter=',\t')
	print data1
	target = ["low","low","high","high","high","high","high","mid","mid","mid","mid","mid"]
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(data1,target)
	out = StringIO()
	out = tree.export_graphviz(clf, out_file='output2.dot')
	result = clf.predict(data2)
	print result

	obj=['low','mid','high']
	pos =np.arange(len(obj))
	high=mid=low=0
	for i in result:
  	  if(i=='high'):
    		high=high+1
  	  elif(i=='mid'):
    		mid=mid+1
  	  else:
    		low=low+1
	print low,mid,high
	fig1 = figure(1,figsize=(5,5))
	title('How much you know about what you know?!')
	performance=[low,mid,high]
	plt.barh(pos,performance,align="center",color=('blue','brown','green'),alpha=0.9)
	plt.xlim(0, 10)
	grid(True)
	plt.yticks(pos,obj)
	ylabel('Performance scale')
	xlabel('Number of questions')
	fig1.savefig('/home/unknown/Django_web/Django-1.8.5/learner2/static/img/fig11.png')
	plt.clf()

	al,th,kn,ni=2,2,2,2
	fig2 = figure(2,figsize=(6,5))
	width=0.2
	labels = 'Thinking','Analyzing','Knowledge','Need to improve'
	pos = np.arange(len(labels))
	high=mid=low=0
	for i in result:
  		if(i=='high'):
    		 	high=high+1
  		elif(i=='mid'):
    			mid=mid+1
 		else:
    			low=low+1
	if high==10 :
		al,th,kn=99.7,99.4,99.8
	elif(mid==10):
		al,th,kn,ni=79,85,75,38
	elif(low>=9):
		ni=99
	elif high>=7 and mid>=3 and low<=2:
		al,th,kn,ni=82,86,90,25
	elif high>=7 and mid<=3 and low<=2:
		al,th,kn,ni=88,86,80,24
	elif high>=5 and mid>=4 and low<=3:
		al,th,kn,ni=68,79,70,40
	elif high>=6 and mid<=4 and low<=3:
		al,th,kn,ni=75,79,74,38
	elif high>=4 and mid<=5 and low<=3:
		al,th,kn,ni=65,72,70,38
	elif mid>=7 and low<=3 and high<=3:
		al,th,kn,ni=62,60,62,58
	elif mid>=4 and low<=3 and high<=3:
		al,th,kn,ni=58,60,62,57
	elif mid<=6 and low>=4 and high<=3:
		al,th,kn,ni=42,40,46,62
	elif high>=4 and mid>=3 and low<=3:
		al,th,kn,ni=60,64,57,45
	elif high>=3 and mid>=4 and low<=3:
		al,th,kn,ni=58,60,52,54
	elif high<=3 and mid<=3 and low>=9:
		al,th,kn,ni=18,20,14,95
	elif low>=1 and mid<=4 and high<=3:
		al,th,kn,ni=28,32,22,84
	elif low>=4 and mid<=5 and high<=5:
		al,th,kn,ni=36,42,48,72
	elif low>=3 and mid<=7 and high<=4:
		al,th,kn,ni=32,38,35,80
	elif high>=6 and low<=4 and mid<=3: 
		al,th,kn,ni=58,60,62,55
	elif high<=5 and low>=4 and mid<=4:
		al,th,kn,ni=30,32,35,75
	elif mid<=6 and low>=5 and high<=3:
		al,th,kn,ni=33,35,36,77
	elif high>=4 and mid<=7 and low>=3:
		al,th,kn,ni=62,66,68,39
	elif high>=3 and mid<=3 and low>=3:
		al,th,kn,ni=18,20,22,89
	else:
		al,th,kn,ni=50,50,50,50


	
	title("Learner's Proficiency", bbox={'facecolor':'grey', 'alpha':0.5, 'pad':4})
	fracs = (th,al,kn,ni)
	plt.bar(pos+width,fracs,width,color=('lightcoral','y','g','b'))
	plt.ylim(0,100)
	plt.xlim(0, 4)
	plt.xticks(pos+width+0.1,labels)
	fig2.savefig('/home/unknown/Django_web/Django-1.8.5/learner2/static/img/fig12.png')
	plt.clf() 

	data4 = sp.genfromtxt("traindata22.csv",dtype=str,delimiter=',')
	print data4
	target1 = ["q","q","q","nq","nq","nq","nq","q","q","nq","q","q","nq","q","q","nq","q","nq","nq","q","q","nq"]

	i=j=0

	for i in range(22):
 		for j in range(10):
  			if data4[i][j]=='high':
  				data4[i][j]= 2.0
  			elif data4[i][j]=='mid':
  				data4[i][j]= 1.0
  			else:
  				data4[i][j]= 0.0

	print data4

	for j in range(10):
  		if result[j]=='high':
  			result[j]= 2.0
  		elif result[j]=='mid':
  			result[j]= 1.0
  		else:
  			result[j]= 0.0
	clf1 = tree.DecisionTreeClassifier()
	clf1 = clf1.fit(data4,target1)
	out1 = StringIO()
	out1 = tree.export_graphviz(clf1, out_file='output22.dot')
	result1 = clf1.predict(result)
	result1.reshape(1,-1)
	print result1

	q=nq=0
	flag=0
	fig3 = figure(3, figsize=(5, 5))
	ax = axes([0.27, 0.1, 0.57, 0.8])
	ax.annotate('', xy=(-0.83,0.00), xytext=(0.80, -0.00), arrowprops=dict(arrowstyle="-"))
	ax.annotate('Threshold', xy=(-0.5,0.13), xytext=(-0.25, 0.056))

	labels = 'Reached','Need to improve'

	print low,mid,high
	
	if((high+mid-2) > low):
	   flag=0
	   print flag
	else:
	   flag=1
	   print flag

	if flag == 0:
		if high==10:
			q,nq=100,0
			print q,nq
		elif(mid==10):
			q,nq=87.9,(100-87.9)
			print q,nq
		elif high>=7 and mid>=3 and low<=2:
			q,nq=82,(100-82)
			print q,nq
		elif high>=5 and mid>=5 and low<=3:
			q,nq=67,(100-67)
			print q,nq
		elif high<=8 and mid<=9 and low<=3:
			q,nq=74,(100-74)
			print q,nq
		elif high<=6 and mid<=9 and low<=3:
			q,nq=66,(100-66)
			print q,nq
		elif high>=5 and low<=4 and mid<=7:
			q,nq=68,(100-68)
			print q,nq
		elif mid>=7 and low<=3 and high<=3:
			q,nq=72,(100-72)
			print q,nq
		elif mid>=4 and low<=3 and high<=3:
			q,nq=62,(100-62)
			print q,nq
		elif high>=4 and mid<=8 and low<=3:
			q,nq=70,(100-70)
			print q,nq
		elif high>=4 and mid>=3 and low<=4:
			q,nq=56,(100-56)
			print q,nq
		elif high>=4 and mid>=4 and low<=4:
			q,nq=54,(100-54)
			print q,nq
		else:
			q,nq=50,(100-50)
			print q,nq

	else:
		if low==10:
			nq,q=100,0
		elif high<=3 and mid<=3 and low>=9:
			nq,q=82,(100-82)
		elif mid<=6 and low>=5 and high<=3:
			nq,q=68,(100-68)
		elif low>=6 and mid<=5 and high<=4:
			nq,q=72,(100-72)
		elif low>=4 and mid<=5 and high<=5:
			nq,q=60,(100-60)
		elif high<=4 and mid<=4 and low>=3:
			nq,q=70,(100-70)
		elif high<=4 and low>=4 and mid>=3:
			nq,q=58,(100-58)
		else:
			q,nq=50,(100-50)
  
	title("Learner's competence", bbox={'facecolor':'grey', 'alpha':0.5, 'pad':4})
	fracs = [q,nq]
	explode = (0.04,0.0)
	pie(fracs, explode=explode, labels=labels, colors=('g','w'), autopct='%1.0f%%', shadow=False ,radius=0.8)
	fig3.savefig('/home/unknown/Django_web/Django-1.8.5/learner2/static/img/fig13.png') 
	plt.clf()

	percentage = (high+mid-2)*10

	s = SessionData(user_id = userid,result = result1[0],level = 1,percent = percentage,session_count = session_count)
	s.save()

	if result1[0]=='q':
		qualified = 1
		return HttpResponseRedirect('/pupil/status220')
	else:
		return HttpResponseRedirect('/pupil/status221')

def result23(request):
	global session_count,level,qualified,sess_data
	level = level+1
	sess_data = sess_data+1
	print session_count
	context = RequestContext(request)
	userid = request.session['userid']
	print userid
	f=open('/home/unknown/Django_web/Django-1.8.5/learner2/datain1.csv','r+')
	conn = sqlite3.connect('/home/unknown/Django_web/Django-1.8.5/learner2/db.sqlite3')
	cursor=conn.execute("select id,name from pupil_user_info;")                                                                                                                            																	
	for row0 in cursor:	
		if row0[1]==userid:
			uid = row0[0]
			print uid
	cursor1=conn.execute("select ans,hint,time from pupil_user_data where user_id=%d;" % uid)
	cursor2=conn.execute("select rans from pupil_questions2 where set_id='1';")
	j=0
	row3 = [0,0,0,0,0,0,0,0,0,0]
	row4 = [0,0,0,0,0,0,0,0,0,0]
	for row1 in cursor2:
  		row1 = list(row1)
  		print row1
  		row3[j] = row1[0]
  		j = j+1
	j=0
	for row in cursor1:
  		row = list(row)
  		row[0] = int(row[0])
  		row[1] = int(row[1])
  		row[2] = int(row[2])
  		row[2] = row[2]/1000000
  		print row 
  		if row3[j] == row[0]:
    			row[0] = 1
    			row4[j] = row[0]
    			j = j+1	
  		else:
    			row[0] = 0
    			row4[j] = row[0]
    			j = j+1														
  		for i in range(3):
  			f.write(str(row[i])+',\t')
  		f.write('\n')
	print "fine"
	f.close();
	conn.commit();
	conn.close();

	data2 = sp.genfromtxt("datain3.csv",dtype=int,delimiter=',\t')
	print data2
	data1 = sp.genfromtxt("traindata3.csv",dtype=int,delimiter=',\t')
	print data1
	target = ["low","low","high","high","high","high","high","mid","mid","mid","mid","mid"]
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(data1,target)
	out = StringIO()
	out = tree.export_graphviz(clf, out_file='output3.dot')
	result = clf.predict(data2)
	print result

	obj=['low','mid','high']
	pos =np.arange(len(obj))
	high=mid=low=0
	for i in result:
  	  if(i=='high'):
    		high=high+1
  	  elif(i=='mid'):
    		mid=mid+1
  	  else:
    		low=low+1
	print low,mid,high
	fig1 = figure(1,figsize=(5,5))
	title('How much you know about what you know?!')
	performance=[low,mid,high]
	plt.barh(pos,performance,align="center",color=('blue','brown','green'),alpha=0.9)
	plt.xlim(0, 10)
	grid(True)
	plt.yticks(pos,obj)
	ylabel('Performance scale')
	xlabel('Number of questions')
	fig1.savefig('/home/unknown/Django_web/Django-1.8.5/learner2/static/img/fig11.png')
	plt.clf()

	al,th,kn,ni=2,2,2,2
	fig2 = figure(2,figsize=(6,5))
	width=0.2
	labels = 'Thinking','Analyzing','Knowledge','Need to improve'
	pos = np.arange(len(labels))
	high=mid=low=0
	for i in result:
  		if(i=='high'):
    		 	high=high+1
  		elif(i=='mid'):
    			mid=mid+1
 		else:
    			low=low+1
	if high==10 :
		al,th,kn=99.7,99.4,99.8
	elif(mid==10):
		al,th,kn,ni=79,85,75,38
	elif(low>=9):
		ni=99
	elif high>=7 and mid>=3 and low<=2:
		al,th,kn,ni=82,86,90,25
	elif high>=7 and mid<=3 and low<=2:
		al,th,kn,ni=88,86,80,24
	elif high>=5 and mid>=4 and low<=3:
		al,th,kn,ni=68,79,70,40
	elif high>=6 and mid<=4 and low<=3:
		al,th,kn,ni=75,79,74,38
	elif high>=4 and mid<=5 and low<=3:
		al,th,kn,ni=65,72,70,38
	elif mid>=7 and low<=3 and high<=3:
		al,th,kn,ni=62,60,62,58
	elif mid>=4 and low<=3 and high<=3:
		al,th,kn,ni=58,60,62,57
	elif mid<=6 and low>=4 and high<=3:
		al,th,kn,ni=42,40,46,62
	elif high>=4 and mid>=3 and low<=3:
		al,th,kn,ni=60,64,57,45
	elif high>=3 and mid>=4 and low<=3:
		al,th,kn,ni=58,60,52,54
	elif high<=3 and mid<=3 and low>=9:
		al,th,kn,ni=18,20,14,95
	elif low>=1 and mid<=4 and high<=3:
		al,th,kn,ni=28,32,22,84
	elif low>=4 and mid<=5 and high<=5:
		al,th,kn,ni=36,42,48,72
	elif low>=3 and mid<=7 and high<=4:
		al,th,kn,ni=32,38,35,80
	elif high>=6 and low<=4 and mid<=3: 
		al,th,kn,ni=58,60,62,55
	elif high<=5 and low>=4 and mid<=4:
		al,th,kn,ni=30,32,35,75
	elif mid<=6 and low>=5 and high<=3:
		al,th,kn,ni=33,35,36,77
	elif high>=4 and mid<=7 and low>=3:
		al,th,kn,ni=62,66,68,39
	elif high>=3 and mid<=3 and low>=3:
		al,th,kn,ni=18,20,22,89
	else:
		al,th,kn,ni=50,50,50,50


	
	title("Learner's Proficiency", bbox={'facecolor':'grey', 'alpha':0.5, 'pad':4})
	fracs = (th,al,kn,ni)
	plt.bar(pos+width,fracs,width,color=('lightcoral','y','g','b'))
	plt.ylim(0,100)
	plt.xlim(0, 4)
	plt.xticks(pos+width+0.1,labels)
	fig2.savefig('/home/unknown/Django_web/Django-1.8.5/learner2/static/img/fig12.png')
	plt.clf() 

	data4 = sp.genfromtxt("traindata32.csv",dtype=str,delimiter=',')
	print data4
	target1 = ["q","q","q","nq","nq","nq","nq","q","q","nq","q","q","nq","q","q","nq","q","nq","nq","q","q","nq"]

	i=j=0

	for i in range(22):
 		for j in range(10):
  			if data4[i][j]=='high':
  				data4[i][j]= 2.0
  			elif data4[i][j]=='mid':
  				data4[i][j]= 1.0
  			else:
  				data4[i][j]= 0.0

	print data4

	for j in range(10):
  		if result[j]=='high':
  			result[j]= 2.0
  		elif result[j]=='mid':
  			result[j]= 1.0
  		else:
  			result[j]= 0.0
	clf1 = tree.DecisionTreeClassifier()
	clf1 = clf1.fit(data4,target1)
	out1 = StringIO()
	out1 = tree.export_graphviz(clf1, out_file='output32.dot')
	result1 = clf1.predict(result)
	result1.reshape(1,-1)
	print result1

	q=nq=0
	flag=0
	fig3 = figure(3, figsize=(5, 5))
	ax = axes([0.27, 0.1, 0.57, 0.8])
	ax.annotate('', xy=(-0.83,0.00), xytext=(0.80, -0.00), arrowprops=dict(arrowstyle="-"))
	ax.annotate('Threshold', xy=(-0.5,0.13), xytext=(-0.25, 0.056))

	labels = 'Reached','Need to improve'

	print low,mid,high
	
	if((high+mid-2) > low):
	   flag=0
	   print flag
	else:
	   flag=1
	   print flag

	if flag == 0:
		if high==10:
			q,nq=100,0
			print q,nq
		elif(mid==10):
			q,nq=87.9,(100-87.9)
			print q,nq
		elif high>=7 and mid>=3 and low<=2:
			q,nq=82,(100-82)
			print q,nq
		elif high>=5 and mid>=5 and low<=3:
			q,nq=67,(100-67)
			print q,nq
		elif high<=8 and mid<=9 and low<=3:
			q,nq=74,(100-74)
			print q,nq
		elif high<=6 and mid<=9 and low<=3:
			q,nq=66,(100-66)
			print q,nq
		elif high>=5 and low<=4 and mid<=7:
			q,nq=68,(100-68)
			print q,nq
		elif mid>=7 and low<=3 and high<=3:
			q,nq=72,(100-72)
			print q,nq
		elif mid>=4 and low<=3 and high<=3:
			q,nq=62,(100-62)
			print q,nq
		elif high>=4 and mid<=8 and low<=3:
			q,nq=70,(100-70)
			print q,nq
		elif high>=4 and mid>=3 and low<=4:
			q,nq=56,(100-56)
			print q,nq
		elif high>=4 and mid>=4 and low<=4:
			q,nq=54,(100-54)
			print q,nq
		else:
			q,nq=50,(100-50)
			print q,nq

	else:
		if low==10:
			nq,q=100,0
		elif high<=3 and mid<=3 and low>=9:
			nq,q=82,(100-82)
		elif mid<=6 and low>=5 and high<=3:
			nq,q=68,(100-68)
		elif low>=6 and mid<=5 and high<=4:
			nq,q=72,(100-72)
		elif low>=4 and mid<=5 and high<=5:
			nq,q=60,(100-60)
		elif high<=4 and mid<=4 and low>=3:
			nq,q=70,(100-70)
		elif high<=4 and low>=4 and mid>=3:
			nq,q=58,(100-58)
		else:
			q,nq=50,(100-50)
  
	title("Learner's competence", bbox={'facecolor':'grey', 'alpha':0.5, 'pad':4})
	fracs = [q,nq]
	explode = (0.04,0.0)
	pie(fracs, explode=explode, labels=labels, colors=('g','w'), autopct='%1.0f%%', shadow=False ,radius=0.8)
	fig3.savefig('/home/unknown/Django_web/Django-1.8.5/learner2/static/img/fig13.png') 
	plt.clf()

	percentage = (high+mid-2)*10

	s = SessionData(user_id = userid,result = result1[0],level = 1,percent = percentage,session_count = session_count)
	s.save()

	if result1[0]=='q':
		qualified = 1
		return HttpResponseRedirect('/pupil/status330')
	else:
		return HttpResponseRedirect('/pupil/status331')

def status210(request):
	context = RequestContext(request)
	context_dict = {'result': "Congradulations.You are qualified for the next level.",'qualified':qualified}
	conn = sqlite3.connect('/home/unknown/Django_web/Django-1.8.5/learner2/db.sqlite3')
	conn.execute("delete from pupil_user_data;")
	conn.commit();
	conn.close();
	return render_to_response('pupil/status210.html', context_dict, context)

def status211(request):
	context = RequestContext(request)
	context_dict = {'result': "Sorry.You are not qualified for the next level.",'qualified':qualified}
	return render_to_response('pupil/status211.html', context_dict, context)

def status220(request):
	context = RequestContext(request)
	context_dict = {'result': "Congradulations.You are qualified for the next level.",'qualified':qualified}
	conn = sqlite3.connect('/home/unknown/Django_web/Django-1.8.5/learner2/db.sqlite3')
	conn.execute("delete from pupil_user_data;")
	conn.commit();
	conn.close();
	return render_to_response('pupil/status220.html', context_dict, context)

def status221(request):
	context = RequestContext(request)
	context_dict = {'result': "Sorry.You are not qualified for the next level.",'qualified':qualified}
	return render_to_response('pupil/status221.html', context_dict, context)

def status230(request):
	context = RequestContext(request)
	context_dict = {'result': "Congradulations.You are qualified for the next level.",'qualified':qualified}
	conn = sqlite3.connect('/home/unknown/Django_web/Django-1.8.5/learner2/db.sqlite3')
	conn.execute("delete from pupil_user_data;")
	conn.commit();
	conn.close();
	return render_to_response('pupil/status230.html', context_dict, context)

def status231(request):
	context = RequestContext(request)
	context_dict = {'result': "Sorry.You are not qualified for the next level.",'qualified':qualified}
	return render_to_response('pupil/status231.html', context_dict, context)







