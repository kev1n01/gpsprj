import json
from rest_framework import viewsets
from django.http import JsonResponse
from django.views import View
from .serializers import DriverSerializer, BusSerializer, StudentSerializer, TravelRegisterDetailSerializer, TravelRegisterSerializer, StopPointSerializer, UserSerializer
from rest_framework import generics
from .models import Driver, Bus, Student, StopPoint, TravelRegister, TravelRegisterDetail, User
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class Login(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        jd = json.loads(request.body)
        user = User.objects.filter(username=jd["username"],password=jd["password"]).values().first()#consult ORM
        if user:
            type =  'admin' if user.get("type") == 0 else 'student' if user.get("type") == 1 else 'driver' if user.get("type") == 2 else 'guard' #ternary operator
            data = {
                "status" : "success",
                "id" : user.get("id"),
                "username": user.get("username"),
                "type": type,
            }
        else:
            data = { "status" : "failed"}       

        return JsonResponse(data)

class buses(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    
class users(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class drivers(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    
class students(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentFilterApiView(APIView):
    
    def get(self,request,*args, **kwargs):
        queryset = Student.objects.all()
        param_user_id = self.request.query_params.get('user_id',None)
        if param_user_id:
            queryset=queryset.filter(user_id=param_user_id)
        serializer=StudentSerializer(queryset, many=True)
        return Response(serializer.data)
    
class travelRegisters(viewsets.ModelViewSet):
    queryset = TravelRegister.objects.all()
    serializer_class = TravelRegisterSerializer
    
class stopPoints(viewsets.ModelViewSet):
    queryset = StopPoint.objects.all()
    serializer_class = StopPointSerializer

class travelRegisterDetails(viewsets.ModelViewSet):
    queryset = TravelRegisterDetail.objects.all()
    serializer_class = TravelRegisterDetailSerializer

