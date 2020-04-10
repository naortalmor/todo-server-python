from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import Http404
from .serializers import UserSerializer

class LoginUsers(APIView):
    def post(self, request, format=None):
        client_id = "235366402903-658ku15fjjjdnadc75k3ksvb68hvqbd7.apps.googleusercontent.com"
        try:
            idinfo = id_token.verify_oauth2_token(request.data['token'], requests.Request(), client_id)
            userid = idinfo['sub']
            users_set = User.objects.all()
            user = users_set.filter(mail = idinfo['email'])
            if user.count() != 1:
                new_user = User(first_name=idinfo['given_name'],
                                last_name=idinfo['family_name'],
                                mail=idinfo['email'],
                                image_url=idinfo['picture'])
                new_user.save()
                breakpoint()
                s = UserSerializer(new_user)
                breakpoint()
                return Response(s.data)
            else:
                s = UserSerializer(user[0])
                return Response(s.data)

        except:
            raise Http404('Failed to authenticate user')
