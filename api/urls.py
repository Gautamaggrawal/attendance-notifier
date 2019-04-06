from .views import *
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('registermobile/', ProfileMobileView.as_view()),
    path('verifyotp/', VerifyOTP.as_view()),
    path('register/', RegisterUser.as_view()),
    # path('login/', Login.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('attendance/',Getattendance.as_view()),
    path('getdetails/',GetDetailedAttendance.as_view()),

]
