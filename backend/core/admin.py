from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Institute, Faculty, Staff, News, Alumni
from .students import Program, Enrollment, Student, Certificate

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'short_program_details', 'short_admission_requirements', 'short_application_process', 'short_facilities_overview')
    search_fields = ('program_name',)

    def short_program_details(self, obj):
        return (obj.program_details[:20] + '...') if len(obj.program_details) > 20 else obj.program_details
    short_program_details.short_description = 'Program Details'

    def short_admission_requirements(self, obj):
        return (obj.admission_requirements[:20] + '...') if len(obj.admission_requirements) > 20 else obj.admission_requirements
    short_admission_requirements.short_description = 'Admission Requirements'

    def short_application_process(self, obj):
        return (obj.application_process[:20] + '...') if len(obj.application_process) > 20 else obj.application_process
    short_application_process.short_description = 'Application Process'

    def short_facilities_overview(self, obj):
        return (obj.facilities_overview[:20] + '...') if len(obj.facilities_overview) > 20 else obj.facilities_overview
    short_facilities_overview.short_description = 'Facilities Overview'


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('enrollment_number', 'first_name', 'last_name', 'program_name', 'qualification')
    search_fields = ('enrollment_number', 'first_name', 'last_name')
    list_filter = ('qualification',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'enrollment', 'get_enrollment_details')
    search_fields = ('student_id', 'enrollment__enrollment_number')

    def get_enrollment_details(self, obj):
        return f"{obj.enrollment.first_name} {obj.enrollment.last_name} - {obj.enrollment.enrollment_number}"
    get_enrollment_details.short_description = 'Enrollment Details'


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_number', 'student_name', 'certificate_type', 'issue_date', 'certificate_program')
    search_fields = ('certificate_number', 'student_name', 'certificate_type')
    list_filter = ('certificate_program',)

admin.site.register(Program, ProgramAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Certificate, CertificateAdmin)

class InstituteAdmin(admin.ModelAdmin):
    list_display = ('display_logo','name', 'email', 'phone_number')
    readonly_fields = ('display_logo',)
    def display_logo(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="40" height="20" />')
        else:
            return 'No Logo'
    display_logo.short_description = 'Logo'
    display_logo.allow_tags = True

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'Institute', 'qualifications', 'expertise')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'Institute', 'position')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'Institute', 'date_published')

class AlumniAdmin(admin.ModelAdmin):
    list_display = ('name', 'Institute', 'success_story')

# Register your models with the custom admin classes
admin.site.register(Institute,InstituteAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Alumni, AlumniAdmin)