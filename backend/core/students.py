from django.core.validators import RegexValidator, EmailValidator
from django.db import models
from datetime import datetime

# Academic Programs
class Program(models.Model):
    program_name = models.CharField(max_length=255)
    program_details = models.TextField()
    
    # Admissions Information
    admission_requirements = models.TextField()
    application_process = models.TextField()
    
    # Campus Facilities
    facilities_overview = models.TextField()
    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Program Details"
        
    def __str__(self):
        return self.program_name

class Enrollment(models.Model):
    QUALIFICATION_CHOICES = [
        ('PG', 'Post Graduate'),
        ('UG', 'Under Graduate'),
        ('12TH', 'Intermediate'),
        ('10TH', 'High School'),
        ('OTHERS', 'Others'),
    ]
    CAST_CHOICES = [
        ('SC/ST', 'Scheduled Castes/Tribes'),
        ('OBC', 'Other Backward Classes'),
        ('Minority', 'Minority'),
        ('GEN', 'General'),
        ('OTHERS', 'Others'),
    ]
    program_name = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True)
    enrollment_number = models.CharField(max_length=20,unique=True, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    f_first_name = models.CharField(max_length=255)
    f_last_name = models.CharField(max_length=255)
    address = models.TextField(max_length=30)
    email = models.EmailField(validators=[EmailValidator(message='Invalid email address.')])
    mobile = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Mobile number must be 10 digits without +91.',
            )
        ],
        help_text='Enter a 10-digit mobile number without +91.',
    )  
    qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    cast = models.CharField(max_length=20, choices=CAST_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.enrollment_number}"

class Student(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE)
    # Add other fields for student details

    student_id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f"{self.enrollment.first_name} {self.enrollment.last_name} - {self.student_id}"

class Certificate(models.Model):
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True)
    student_name = models.CharField(max_length=255)
    certificate_type = models.CharField(max_length=255)
    issue_date = models.DateField()
    # Add the following ForeignKey field
    certificate_program = models.ForeignKey('Program', on_delete=models.CASCADE, null=True, blank=True)
    # New field for certificate number
    certificate_number = models.CharField(max_length=20, unique=True, editable=False)

    # Add other fields as needed

    def save(self, *args, **kwargs):
        # Generate certificate number based on program name, year, month, and student ID
        if self.certificate_program:
            program_name = "".join([i[0] for i in self.certificate_program.program_name.split()])
            year = str(self.issue_date.year)[-2:]
            month = str(self.issue_date.month).zfill(2)
            student_id = str(self.student_id.student_id).zfill(4)  # Assuming student ID is an integer field
            # Combine the components to form the certificate number
            certificate_number = f"{program_name}{year}{month}{student_id}"

            self.certificate_number = certificate_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_name} - {self.certificate_number}"
