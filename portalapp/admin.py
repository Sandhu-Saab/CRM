from django.contrib import admin
from .models import *


# Register your models here.

class UserInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'mobile', 'email')
admin.site.register(UserInstance, UserInstanceAdmin)

class Learning_PathAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
admin.site.register(Learning_Partner, Learning_PathAdmin)


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('trainer_id', 'trainer_name')
admin.site.register(Trainer, TrainerAdmin)

class myuploadfileAdmin(admin.ModelAdmin):
    list_display = ('id','trainer_name','last_modification')
admin.site.register(myuploadfile, myuploadfileAdmin)


class Training_LeadHistAdmin(admin.ModelAdmin):
    list_display = ('hist_id','training_lead_id','updated_user','updated_time')
admin.site.register(Training_LeadHist, Training_LeadHistAdmin)
# admin.site.register(myuploadfile)


class Training_LeadAdmin(admin.ModelAdmin):
    list_display = ('id','handel_by','learning_partner', 'assign_to_trainer', 'course_name','lead_type' ,'getting_lead_date','time_zone', 'start_date', 'end_date', 'lead_status', 'lead_description')
admin.site.register(Training_Lead, Training_LeadAdmin)
