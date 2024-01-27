from django.db import models

class Institute(models.Model):
    # Basic Information
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='Institute_logos/')
    
    # Contact Information
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    
    # About Us
    mission_statement = models.TextField()
    vision_statement = models.TextField()
    history = models.TextField()
    values = models.TextField()
    class Meta:
        verbose_name = "Institute"
        verbose_name_plural = "Institute Details"
    def __str__(self):
        return self.name


    
# Faculty and Staff
class Faculty(models.Model):
    Institute = models.ForeignKey('Institute', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    qualifications = models.TextField()
    expertise = models.TextField()
    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculty Details"
    
class Staff(models.Model):
    Institute = models.ForeignKey('Institute', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    
    # Student Life
    extracurricular_activities = models.TextField()
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff Details"
    
    # News and Updates
class News(models.Model):
    Institute = models.ForeignKey('Institute', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateField()
    
    # Resources for Current Students
    academic_calendar = models.TextField()
    student_handbook = models.TextField()
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News Details"
    
# Alumni Relations
class Alumni(models.Model):
    Institute = models.ForeignKey('Institute', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    success_story = models.TextField()
    
    # Social Media Integration
    social_media_links = models.URLField()
    
    # Accessibility Information
    accessibility_info = models.TextField()
    
    # Legal Information
    privacy_policy = models.TextField()
    terms_of_use = models.TextField()
    class Meta:
        verbose_name = "Alumni"
        verbose_name_plural = "Alumni Details"
