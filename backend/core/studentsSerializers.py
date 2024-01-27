from .students import Certificate,Program
from rest_framework import serializers

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    program_name = serializers.StringRelatedField(source='certificate_program.program_name', read_only=True)

    class Meta:
        model = Certificate
        exclude = ['certificate_program']