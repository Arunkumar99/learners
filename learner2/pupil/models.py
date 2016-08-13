from django.db import models

# Create your models here.

class User_info(models.Model):
	name = models.CharField('user name',max_length=30,unique=True)
	password = models.CharField('user password',max_length=30)
	emailid = models.CharField('emailid of user',max_length=50)
	personal = models.TextField()
	
	def __str__(self):
		return self.name

class User_data(models.Model):
	ans = models.IntegerField()
	hint = models.IntegerField()
	time = models.DurationField()
	user = models.ForeignKey('User_info')

	def __str__(self):
		return 

class Questions(models.Model):
	set_id = models.IntegerField(default=0)
	question = models.TextField()
	rans = models.IntegerField(default=0)
	option1 = models.CharField(max_length=60)
	option2 = models.CharField(max_length=60)
	option3 = models.CharField(max_length=60)
	option4 = models.CharField(max_length=60)
	hint1 = models.CharField(max_length=60)
	hint2 = models.CharField(max_length=60)
	hint3 = models.CharField(max_length=60)
	hint4 = models.CharField(max_length=60)

	def __str__(self):
		return self.question

class Questions1(models.Model):
	set_id = models.IntegerField(default=0)
	question = models.TextField()
	rans = models.IntegerField(default=0)
	option1 = models.CharField(max_length=60)
	option2 = models.CharField(max_length=60)
	option3 = models.CharField(max_length=60)
	option4 = models.CharField(max_length=60)
	hint1 = models.CharField(max_length=60)
	hint2 = models.CharField(max_length=60)
	hint3 = models.CharField(max_length=60)
	hint4 = models.CharField(max_length=60)

	def __str__(self):
		return self.question

class Questions2(models.Model):
	set_id = models.IntegerField(default=0)
	question = models.TextField()
	rans = models.IntegerField(default=0)
	option1 = models.CharField(max_length=60)
	option2 = models.CharField(max_length=60)
	option3 = models.CharField(max_length=60)
	option4 = models.CharField(max_length=60)
	hint1 = models.CharField(max_length=60)
	hint2 = models.CharField(max_length=60)
	hint3 = models.CharField(max_length=60)
	hint4 = models.CharField(max_length=60)

	def __str__(self):
		return self.question

class Questions3(models.Model):
	set_id = models.IntegerField(default=0)
	question = models.TextField()
	rans = models.IntegerField(default=0)
	option1 = models.CharField(max_length=60)
	option2 = models.CharField(max_length=60)
	option3 = models.CharField(max_length=60)
	option4 = models.CharField(max_length=60)
	hint1 = models.CharField(max_length=60)
	hint2 = models.CharField(max_length=60)
	hint3 = models.CharField(max_length=60)
	hint4 = models.CharField(max_length=60)

	def __str__(self):
		return self.question

class Questions4(models.Model):
	set_id = models.IntegerField(default=0)
	question = models.TextField()
	rans = models.IntegerField(default=0)
	option1 = models.CharField(max_length=60)
	option2 = models.CharField(max_length=60)
	option3 = models.CharField(max_length=60)
	option4 = models.CharField(max_length=60)
	hint1 = models.CharField(max_length=60)
	hint2 = models.CharField(max_length=60)
	hint3 = models.CharField(max_length=60)
	hint4 = models.CharField(max_length=60)

	def __str__(self):
		return self.question

class FeedBack(models.Model):
	user = models.CharField(max_length=30,default=0)
	feedback = models.TextField()

	def __str__(self):
		return 


class SessionData(models.Model): 	
	user_id = models.CharField(max_length=30,primary_key=True,unique=False)
	session_count = models.IntegerField(default=1)
	result = models.CharField(max_length=10)
	level = models.IntegerField(default=0)
	percent = models.IntegerField(default=0)

	def __str__(self):
		return self.user_id







