import boto3
import random
from .webkiosk_utils import *
from .models import *

class OtpGenration():
	def generate_otp(phone):
		if phone:
			key=''.join(random.sample('0123456789', 4))
			return key
		else:
			return False

class aws_sns():
	def sendmobileotp(mobile,otp):
		client = boto3.client("sns",aws_access_key_id="AKIAIZKSY5VMUA4H2WUA",aws_secret_access_key="FrwRZ30fXN8UnwT5R4I0qGhlbIO/5JgvFbBxvLT1",region_name="us-east-1")
		ss=client.publish(PhoneNumber=('+91'+mobile),Message=otp +" is the OTP code to verify your webkiosk account")
		if ss.get('ResponseMetadata').get("HTTPStatusCode")==200:
			return True
		else:
			return False
	def sendsms(mobile,lowattendancesms):
		client = boto3.client("sns",aws_access_key_id="AKIAIZKSY5VMUA4H2WUA",aws_secret_access_key="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",region_name="us-east-1")
		ss=client.publish(PhoneNumber=('+91'+mobile),Message="You attendance is low please attend the classes"+lowattendancesms)


def check_latest_attendance(data):
	low_attendance_sub=[]
	for i in data:
		for j in range(1,5):
			if i[j].isdigit() and int(i[j])<=80:
				low_attendance_sub.append({i[0]:i[j]})
	return low_attendance_sub

			
def get_latest_student_attendence():
	data=Profile.objects.all().values('user__username','webpass','phone')
	for i in data:
		data=webkioskupdates.get_attendence(i['user__username'],i['webpass'])
		low_attendance_sub=check_latest_attendance(data)
		if len(low_attendance_sub)>0:
			print(low_attendance_sub)
			aws_sns.sendsms(i['phone'],str(low_attendance_sub))
			attendance.objects.filter(profile=Profile.objects.get(user=User.objects.get(username=i['user__username']))).update(attendanceupdated=True,notificationsent=True)
		else:
			attendance.objects.filter(profile=Profile.objects.get(user=User.objects.get(username=i['user__username']))).update(attendanceupdated=True,notificationsent=False)


