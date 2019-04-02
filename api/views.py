from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import *
from rest_framework import generics
from .models import *
import datetime
from django.contrib.auth import authenticate
from .webkiosk_utils import *
from rest_framework.permissions import IsAuthenticated

class ProfileMobileView(generics.CreateAPIView):
		queryset=Profile.objects.all()
		serializer_class = ProfileSerializer

		def perform_create(self, serializer):
			print(self.request.data.get('phone'))
			otp=OtpGenration.generate_otp(self.request.data.get('phone'))
			sentsms=aws_sns.sendmobileotp(self.request.data.get('phone'),otp)
			serializer.save(otp=otp,phoneverified=False)

class VerifyOTP(APIView):
	def post(self,request):
		phone=ProfileSerializer().validate_mobile(request.data)
		otp=ProfileSerializer().validate_otp(request.data)
		if phone==True and otp==True:
			if Profile.objects.filter(phone=request.data.get("phone")).exists()==False:
				return Response("Mobile is not registered with us",status=400)	
			profileobj=Profile.objects.get(phone=request.data.get("phone"))
			if profileobj.phoneverified==True:
				return Response("Mobile is already registered with us",status=400)
			if profileobj.otp==request.data.get("otp"):
				profileobj.otp=None
				profileobj.phoneverified=True
				profileobj.save()
				return Response("Phone verified",status=200)
			else:
				return Response("Invalid Otp",status=400)
		else:
			return Response(phone+otp)


class RegisterUser(APIView):

    def post(self, request):
        password = request.data.get("password")
        name=request.data.get("enrollment")
        phone=ProfileSerializer().validate_mobile(request.data)
        if password and name and phone==True:
            user_exists=Profile.objects.filter(phone=request.data.get("phone"))
            if not user_exists.exists():
                return Response("You are not registered with us",status=400)
            checkstudent=webkkiosk.checklogin(name,password)
            if checkstudent==400:
            	return Response("Invalid Webkiosk Crediatils",status=400)
            else:
            	user=User.objects.create_user(username=name,password=password)
            	user.save()
            	print(type(user))
            	user_exists.update(user=user,webpass=password)
            	print(user_exists[0].user)
            	user_exists[0].save()
            	return Response("User Created",status=200)
        else:
        	return Response(phone,"enrollment and password requried",status=400)

# class Login(APIView):
# 	def post(self, request):
# 		username = request.data.get('enrollment')
# 		password = request.data.get('password')
# 		print(username,password)
# 		if username==None or password==None:
# 			return Response({"status":0,"errorString":"enrollment or password required","data": "" },status=400)
# 		user = authenticate(username=username, password=password)
# 		if user:
# 			return Response({"status":1,"errorString":"Logged In","data": "" },status=200)


class Getattendance(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
    	print(request.user.password)
    	content=webkioskupdates.get_attendence(request.user.username,Profile.objects.get(user=request.user).webpass)
    	return Response(content)


