# yourapp/urls.py
from django.urls import path
from .views import InstituteList, CertificateListCreateView, CertificateDetailView

urlpatterns = [
    path('certificates/', CertificateListCreateView.as_view(), name='certificate-list-create'),
    path('certificates/<int:pk>/', CertificateDetailView.as_view(), name='certificate-detail'),
    path('institute_details/', InstituteList.as_view(), name='institute-details'),
    # Add more paths if needed
]
