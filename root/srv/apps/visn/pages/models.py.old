from django.db import models

# Create your models here.
class User_Info(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    isFreelancer = models.BooleanField(default=False)

class Project(models.Model):
#   project_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User_Info', on_delete=models.CASCADE,)
    project_name = models.CharField(max_length=30)

class File(models.Model):
    user_id = models.ForeignKey('User_Info', on_delete=models.CASCADE,)
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE,)
#   file_id = models.AutoField()
    file_name = models.CharField(max_length=30)
    #the_file = models.FileField(FileField.upload_to,) seems important
    project_name = models.CharField(max_length=30)
