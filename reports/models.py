from django.db import models
from docx import Document as DocxDocument

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class Provider(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=50)
    med_number = models.CharField(max_length=50)
    dob = models.DateField()
    service = models.CharField(max_length=255)
    support_plan = models.TextField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def report_upload_to(instance, filename):
    patient_dir = instance.patient.name.replace(' ', '_')
    return f'reports/{patient_dir}/{filename}'

class Report(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    file = models.FileField(upload_to=report_upload_to)  # Updated to use report_upload_to
    def delete(self, *args, **kwargs):
        if self.file:
            self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Report for {self.patient.name} on {self.date}"
    
    def get_preview_text(self):
        if self.file:
            try:
                doc = DocxDocument(self.file.path)
                full_text = [para.text for para in doc.paragraphs]
                return '\n'.join(full_text)
            except Exception as e:
                return f"Error generating preview: {str(e)}"
        return "No file available"