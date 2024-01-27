# views.py
from rest_framework import generics
from .models import Institute, Faculty, Staff, News, Alumni
from .students import Program, Certificate
from .serializers import InstituteSerializer, FacultySerializer, StaffSerializer, NewsSerializer, AlumniSerializer
from .studentsSerializers import ProgramSerializer, CertificateSerializer
class InstituteList(generics.ListCreateAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer

class ProgramList(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

# class CertificateList(generics.ListCreateAPIView):
#     queryset = Certificate.objects.all()
#     serializer_class = CertificateSerializer

class CertificateListCreateView(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class CertificateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


