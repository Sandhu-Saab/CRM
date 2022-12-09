from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserInstance(AbstractUser):
    mobile = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField( blank=True, null=True)

    def __str__(self):
        return str(self.username)


class Learning_Partner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5000, null=False, blank=False)
    country = models.CharField(max_length=5000, null=False, blank=False)

    def __str__(self):
        return str(self.name)


class Trainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    trainer_name = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False)
    phone_no = models.CharField(max_length=15, unique=True, null=True, blank=True)
    phone_no_optional = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=500)
    email_optional = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    primary_language = models.CharField(max_length=500, null=True, blank=True)
    gender = models.CharField(choices=(('Male', 'Male'), ('Female', 'Female')), max_length=30, blank=True, null=True)
    trainer_type = models.CharField(choices=(('Corporate Trainer', 'Corporate Trainer'), ('Academic Trainer', 'Academic Trainer')), max_length=30, blank=True, null=True)
    trainer_pricing = models.CharField(max_length=1000, null=True, blank=True)
    trainer_course_specialization = models.CharField(max_length=100000)
    trainer_skill_set = models.CharField(max_length=100000, null=True, blank=True)
    trainer_enrolled_with = models.ForeignKey(Learning_Partner, on_delete=models.PROTECT, blank=True, null=True)
    trainer_tier = models.CharField(choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')), max_length=10, null=True, blank=True)



    def __str__(self):
        return str(self.trainer_name)



class myuploadfile(models.Model):
    trainer_name = models.ForeignKey(Trainer ,on_delete=models.PROTECT)
    trainer_attachment = models.FileField(upload_to='attachment', blank=True, null=True)
    trainer_feedback = models.FileField(upload_to='feedback', blank=True, null=True)
    last_modification = models.DateTimeField(auto_now_add='True')




class Training_Lead(models.Model):
    handel_by = models.ForeignKey(UserInstance, on_delete=models.PROTECT)
    learning_partner = models.ForeignKey(Learning_Partner, on_delete=models.PROTECT, blank=False, null=False)
    assign_to_trainer = models.ForeignKey(Trainer, on_delete=models.PROTECT, null=True, blank=True)
    course_name = models.CharField(max_length=2000)
    lead_type = models.CharField(max_length=2000)
    time_zone = models.CharField(choices=(('IST', 'IST'), ('GMT', 'GMT'), ('BST', 'BST'), (
        'CET', 'CET'), ('SAST', 'SAST'), ('EST', 'EST'), ('PST', 'PST'), ('MST', 'MST'), ('UTC', 'UTC')), max_length=40, blank=False, null=False)
    getting_lead_date = models.DateTimeField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    lead_status = models.CharField(choices=(('Initial', 'Initial'), ('In Progress', 'In Progress'), ('Follow Up', 'Follow Up'), (
        'Cancelled', 'Cancelled'), ('Confirmed', 'Confirmed'), ('PO Received', 'PO Received')), max_length=40, blank=False, null=False)
    lead_description = models.CharField(max_length=9000, blank=True, null=True)


    
    # def __str__(self):
    #     return str(self.assign_to_trainer)

    class Meta:
        ordering = ['start_date']

class Training_LeadHist(models.Model):
    hist_id = models.AutoField(primary_key=True)
    training_lead_id = models.CharField(max_length=20000)
    updated_user = models.ForeignKey(UserInstance, on_delete=models.PROTECT)
    updated_time = models.DateTimeField(auto_now_add='True')
    handel_by = models.CharField(max_length=2000)
    learning_partner = models.CharField(max_length=2000)
    assign_to_trainer = models.CharField(max_length=2000)
    course_name = models.CharField(max_length=2000)
    lead_type = models.CharField(max_length=2000)
    time_zone = models.CharField(max_length=2000)
    getting_lead_date = models.CharField(max_length=2000)
    start_date = models.CharField(max_length=2000)
    end_date = models.CharField(max_length=2000)
    lead_status = models.CharField(max_length=2000)
    lead_description = models.CharField(max_length=100000)
