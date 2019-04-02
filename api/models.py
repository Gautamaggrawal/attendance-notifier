from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError

def validate_phone(value):
    if len(value)==10 and value.isalnum() and(value.startswith("6") or value.startswith("7") or value.startswith("8") or value.startswith("9")):
    	pass
    else:
        raise ValidationError(
            ('%(value)s is a invalid phone number'),
            params={'value': value},
        )

class Profile(models.Model):
	user = models.OneToOneField(User,default=None, null=True,on_delete=models.CASCADE)
	phone=models.CharField(max_length=10,validators=[validate_phone],unique=True)
	phoneverified=models.BooleanField(default=False)
	otp=models.CharField(max_length=5,null=True)
	createddate= models.DateTimeField(auto_now=True)
	updateddate = models.DateTimeField(blank=True,null=True)
	webpass=models.CharField(max_length=100,blank=True,null=True)

	def __str__(self):
		return self.phone
	def save(self, *args, **kwargs):
		if self.createddate:
			self.updateddate = datetime.datetime.now()
		super(Profile, self).save(*args, **kwargs)




class attendance(models.Model):
	profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
	created_on = models.DateTimeField("Created on", auto_now_add=True)
	updated_on = models.DateTimeField("Updated on", auto_now=True)
	notificationsent=models.BooleanField(default=False)
	attendanceupdated=models.BooleanField(default=False)

	def __str__(self):
		return str(self.pk)




