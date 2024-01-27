from django.db.models.signals import post_save
from django.dispatch import receiver
from .students import Enrollment
from datetime import datetime

@receiver(post_save, sender=Enrollment)
def generate_enrollment_number(sender, instance, created, **kwargs):
    print(f"signal received for {instance.id} - {instance.email} \
           - {instance.enrollment_number} - {created} - {kwargs} - {sender} - {instance}")
    if created and not instance.enrollment_number:
        current_year = datetime.now().strftime('%Y')
        current_month = datetime.now().strftime('%m')
        enrollment_id = str(instance.id).zfill(5)
        instance.enrollment_number = f'E{current_year}{current_month}{enrollment_id}'
        instance.save()
        print(f"Enrollment number generated: {instance.enrollment_number}")