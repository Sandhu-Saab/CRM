from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.router, name="router"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout, name="logout"),
    path('login_page/', views.login_page, name="login_page"),
    path('add_trainer/', views.add_trainer, name="add_trainer"),
    path('edit_trainer/<int:trainer_id>', views.edit_trainer, name="edit_trainer"),
    path('lerning_path/', views.lerning_path, name="lerning_path"),
    path('add_lerning_path/', views.add_lerning_path, name="add_lerning_path"),
    path('trainer_info/<int:trainer_id>', views.trainer_info, name="trainer_info"),
    path('search_a_trainer/', views.search_a_trainer, name="search_a_trainer"),
    path('add_Lead/', views.add_Lead, name="add_Lead"),
    path('edit_leads/<int:id>', views.edit_leads, name="edit_leads"),
    path('search_a_skill/', views.search_a_skill, name="search_a_skill"),
    path('registration_page/', views.registration_page, name="registration_page"),
    path('trainers_for_schedule_date/', views.trainers_for_schedule_date, name="trainers_for_schedule_date"),
    path('report_for_trainer/', views.report_for_trainer, name="report_for_trainer"),
    path('report_for_trainer_skill/', views.report_for_trainer_skill, name="report_for_trainer_skill"),
    path('status_reports/', views.status_reports, name="status_reports"),
    # path('report_trainer/<int:id>', views.report_trainer, name="report_trainer"),
    path('report_for_lead_status/', views.report_for_lead_status, name="report_for_lead_status"),
    path('check_lerning_path/', views.check_lerning_path, name="check_lerning_path"),
    path('edit__trainer/', views.edit__trainer, name="edit__trainer"),
    path('leads/', views.leads, name="leads"),
    path('trainer_under_learning_partner/<int:id>', views.trainer_under_learning_partner, name="trainer_under_learning_partner"),
    path("trainer_attachment",views.trainer_attachment,name="trainer_attachment"),
    path("update_attachments/", views.update_attachments, name="update_attachments"),
    path("update_attachment/", views.update_attachment, name="update_attachment"),
    path("update_attachment_field/<int:id>", views.update_attachment_field, name="update_attachment_field"),
    path("export_data_to_excel/", views.export_data_to_excel, name="export_data_to_excel"),
    path("available_trainers/", views.available_trainers, name="available_trainers"),
    path("all_leads/", views.all_leads, name="all_leads"),
    path("all_trainer/", views.all_trainer, name="all_trainer"),
    path("all_users/", views.all_users, name="all_users"),
    path("all_lerning_partner/", views.all_lerning_partner, name="all_lerning_partner"),
    path('training_leadHist/<int:id>', views.training_leadHist, name='training_leadHist'),
    path("leadhist/", views.leadhist, name="leadhist"),
    path("lead_hist_download/", views.lead_hist_download, name="lead_hist_download"),
    path("free_trainer/", views.free_trainer, name="free_trainer"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
