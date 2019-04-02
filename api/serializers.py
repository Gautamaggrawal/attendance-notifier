from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=Profile
		fields=('phone',)
	
	def validate_mobile(self, data):
		print(data)
		if not data.get("phone"):
			raise serializers.ValidationError("phone is requried")
		if len(data['phone'])==10 and data['phone'].isalnum() and(data['phone'].startswith("6") or data['phone'].startswith("7") or data['phone'].startswith("8") or data['phone'].startswith("9")):
			pass
		else:
			raise serializers.ValidationError("incorrect mobile")
		return True

	def validate_otp(self,data):
		if not data.get("otp"):
			raise serializers.ValidationError("otp is requried")
		return True

class UserSerializer(serializers.ModelSerializer):
	model=User
	fields=("username","password",)