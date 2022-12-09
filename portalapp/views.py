
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout as logouts
from django.contrib.auth.models import auth
import datetime
from django.utils import timezone
from . models import *
from .forms import *
import pdb
from django.utils import timezone
from django.http import JsonResponse
from django.http import HttpResponse
import pandas as pd
from pandas import ExcelWriter


# Create your views here.


def router(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        return redirect("login_page")


def home(request):
    if request.user.is_authenticated:
        trainer = Trainer.objects.all()
        leads = Training_Lead.objects.all()
        

        learning_partner = Learning_Partner.objects.all()
        users = UserInstance.objects.all()
        df = {"trainer": trainer,"leads": leads,"learning_partner":learning_partner, "users":users}
        return render(request, "home.html", df)
    else:
        return redirect("login_page")


def add_trainer(request):
    if request.user.is_authenticated:
        info = Trainer.objects.all()
        Learning_Partner_info = Learning_Partner.objects.all()
        leads = Training_Lead.objects.all()

        df = {
            "info": info,
            "Learning_Partner_info": Learning_Partner_info,
            "leads": leads,
        }
        print("ERRRRRRRRRRRRRRRRR", df.get('info'))
        if request.method == "POST":
            if len(request.FILES) != 0:
                print("****************", request.FILES["trainer_attachment"])
            trainer_name = request.POST.get("trainer_name")
            address = request.POST.get("address")
            phone_no = request.POST.get("phone_no")
            phone_no_optional = request.POST.get("phone_no_optional")
            email = request.POST.get("email")
            email_optional = request.POST.get("email_optional")
            country = request.POST.get("country")
            primary_language = request.POST.get("primary_language")
            gender = request.POST.get("gender")
            trainer_type = request.POST.get("trainer_type")
            trainer_pricing = request.POST.get("trainer_pricing")
            trainer_course_specialization = request.POST.get(
                "trainer_course_specialization"
            )
            trainer_skill_set = request.POST.get("trainer_skill_set")
            trainer_enrolled_with = request.POST.get("trainer_enrolled_with")
            trainer_tier = request.POST.get("trainer_tier")

            obj = Trainer(trainer_name=trainer_name,address=address,phone_no=phone_no,phone_no_optional=phone_no_optional,email=email,email_optional=email_optional,
            country=country,primary_language=primary_language,gender=gender,trainer_type=trainer_type,trainer_pricing=trainer_pricing,trainer_course_specialization=trainer_course_specialization,
            trainer_skill_set=trainer_skill_set,trainer_enrolled_with_id=trainer_enrolled_with,trainer_tier=trainer_tier )
            obj.save()


        return render(request, "add_trainer.html", df)
    else:
        form = TrainerForm()
        return render(request, "add_trainer.html", {"form": form})

def trainer_attachment(request):
    trainer = Trainer.objects.all()
    if request.method == "POST" :
    
        name = request.POST.get("filename")
        trainer_attachment = request.FILES.getlist("uploadattachment")
        trainer_feedback = request.FILES.getlist("uploadfeedback")
        
        for f in trainer_feedback:
            myuploadfile(trainer_name_id=name,trainer_feedback=f).save()
        
        for v in trainer_attachment:
            myuploadfile(trainer_name_id=name,trainer_attachment=v).save()

        return render(request ,"add_files.html", {"trainer": trainer})
    else:
        return render(request ,"add_files.html", {"trainer": trainer})

    
def update_attachments(request):
    trainer = Trainer.objects.all()

    if request.user.is_authenticated:
        if request.method == "POST" :
            
            files = request.POST.get("files")
            file = myuploadfile.objects.filter(trainer_name_id=files)

            print(files)

            return render(request ,"update_attachments.html", {"trainer": trainer,"file":file,"files":files})
        else:
            return render(request ,"update_attachments.html", {"trainer": trainer})
    else:
        return redirect("router")

    
    

def update_attachment(request):

    trainer = Trainer.objects.all()
    if request.user.is_authenticated:
        trainer = Trainer.objects.all()
        if request.method == "POST" :
            
            files = request.POST.get("files")
            files = myuploadfile.objects.filter(trainer_attachment__contains=files)
            print(files)

            return render(request ,"update_attachments.html", {"trainer": trainer,"files":files})
        else:
            return render(request ,"update_attachments.html", {"trainer": trainer})
    else:
        return redirect("router")

def update_attachment_field(request, id):
    trainer = Trainer.objects.all()
    attachment = myuploadfile.objects.get(id=id)

    if request.user.is_authenticated:
        if request.method == "POST" :
            trainer_name = request.POST.get("trainer_name")
            trainer_attachment = request.POST.get("trainer_attachment")
            trainer_feedback = request.POST.get("trainer_feedback")
            


            attachment.trainer_name_id = trainer_name
            attachment.trainer_attachment = trainer_attachment
            attachment.trainer_feedback = trainer_feedback
            attachment.save()
            return render(request ,"update_attachments.html", {"attachment":attachment, "trainer": trainer})
        else:
            return render(request ,"update_attachments.html", {"trainer": trainer})
    else:
        return redirect("router")



def trainer_info(request, trainer_id):
    if request.user.is_authenticated:
        info = Trainer.objects.get(trainer_id=trainer_id)
        leads = Training_Lead.objects.all()
        myuploadfiles = myuploadfile.objects.filter(trainer_name=trainer_id)


        df = {"infor": info, "leads": leads, "myuploadfiles":myuploadfiles}
        return render(request, "trainer_info.html", df)
    else:
        return redirect("router")


def edit__trainer(request):
    if request.user.is_authenticated:
        trainer = Trainer.objects.all()
        Learning_Partner_info = Learning_Partner.objects.all()
        leads = Training_Lead.objects.all() 

        df = {
            "trainer": trainer,
            "Learning_Partner_info": Learning_Partner_info,
            "leads": leads,
        }
        return render(request, "trainers.html", df)
    else:
        return redirect("router")

def leads(request):
    if request.user.is_authenticated:
        trainer = Trainer.objects.all()
        Learning_Partner_info = Learning_Partner.objects.all()
        leads = Training_Lead.objects.all()

        df = {
            "trainer": trainer,
            "Learning_Partner_info": Learning_Partner_info,
            "leads": leads,
        }
        return render(request, "leads.html", df)


def edit_trainer(request, trainer_id):
    # pdb.set_trace()
    if request.user.is_authenticated:
        info = Trainer.objects.get(trainer_id=trainer_id)
        Learning_Partner_info = Learning_Partner.objects.all()
        leads = Training_Lead.objects.all()

        df = {
            "info": info,
            "Learning_Partner_info": Learning_Partner_info,
            "leads": leads,
        }
        print("ERRRRRRRRRRRRRRRRR", df.get('info'))
        if request.method == "POST":
            if len(request.FILES) != 0:
                print("****************", request.FILES["trainer_attachment"])
            trainer_name = request.POST.get("trainer_name")
            address = request.POST.get("address")
            phone_no = request.POST.get("phone_no")
            phone_no_optional = request.POST.get("phone_no_optional")
            email = request.POST.get("email")
            email_optional = request.POST.get("email_optional")
            gender = request.POST.get("gender")
            trainer_type = request.POST.get("trainer_type")
            trainer_pricing = request.POST.get("trainer_pricing")
            trainer_course_specialization = request.POST.get(
                "trainer_course_specialization"
            )
            trainer_skill_set = request.POST.get("trainer_skill_set")
            trainer_enrolled_with = request.POST.get("trainer_enrolled_with")
            trainer_status = request.POST.get("trainer_status")
            trainer_tier = request.POST.get("trainer_tier")
            

            info.trainer_name = trainer_name
            info.address = address
            info.phone_no = phone_no
            info.phone_no_optional = phone_no_optional
            info.email = email
            info.email_optional = email_optional
            info.gender = gender
            info.trainer_type = trainer_type
            info.trainer_pricing = trainer_pricing
            info.trainer_course_specialization = trainer_course_specialization
            info.trainer_skill_set = trainer_skill_set
            info.trainer_enrolled_with_id = trainer_enrolled_with
            info.trainer_status = trainer_status
            info.trainer_tier = trainer_tier
            print("eeeeeeeeeeeeeeee", info)
            info.save()
            print(info)
        return render(request, "edit_trainer.html", df)
    else:
        return redirect("router")


def lerning_path(request):
    if request.user.is_authenticated:
        Learning_Partner = Learning_Partner.objects.all()
        trainer = Trainer.objects.all()
        leads = Training_Lead.objects.all()
        df = {"Learning_Partner": Learning_Partner, "trainer": trainer, "leads": leads}
        return render(request, "add_trainer.html", df)
    else:
        return redirect("router")


def add_lerning_path(request):
    if request.user.is_authenticated:
        trainer = Trainer.objects.all()
        leads = Training_Lead.objects.all()
        df = {"trainer": trainer, "leads": leads}
        if request.method == "POST":
            name = request.POST.get("name")
            country = request.POST.get("country")

            obj = Learning_Partner(name=name, country=country)
            obj.save()

        return render(request, "add_lerning_path.html", df)
    else:
        return redirect("router")




def check_lerning_path(request):
    if request.user.is_authenticated:
        learning_partner = Learning_Partner.objects.all()
        leads = Training_Lead.objects.all()
        df = {"learning_partner": learning_partner, "leads": leads}
        
        return render(request, "check_lerning_path.html", df)
    else:
        return redirect("router")

def trainer_under_learning_partner(request, id):
    if request.user.is_authenticated:
        learning_partner = Learning_Partner.objects.get(id=id)
        leads = Training_Lead.objects.all()
        df = {"learning_partner": learning_partner, "leads": leads}
        
        return render(request, "trainer_under_learning_partner.html", df)
    else:
        return redirect("router")



def search_a_trainer(request):
    if request.user.is_authenticated:
        leads = Training_Lead.objects.all()
        if request.method == "POST":
            print(request.POST)
            searched = request.POST.get("searched")
            trainers = Trainer.objects.filter(trainer_name__contains=searched) 

        return render(request,"search_a_trainer_from_name.html",{"searched": searched, "trainers": trainers, "leads": leads})
    else:
        return redirect("router")


def login_page(request):
    if request.user.is_authenticated:
        print("Welcome sir")
        return redirect("router")

    else:
        print("Invalid username or password")
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect("router")
            else:
                return HttpResponse("Invalid username or password")
        else:
            return render(request, "login_page.html")


def logout(request):
    if request.user.is_authenticated:

        logouts(request)
        return redirect("router")

    else:
        return redirect("router")


def registration_page(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            password = request.POST.get("password")

            user = UserInstance.objects.create_user(
                username=username, email=email,mobile=mobile, password=password,is_superuser=True, is_active=True, is_staff=True
            )
            user.save()

            print("User Created")

            return redirect("router")
        else:
            return render(request, "registration_page.html")
    else:
        return redirect("router")


def add_Lead(request):
    if request.user.is_authenticated:
        trainer = Trainer.objects.all()
        users = UserInstance.objects.all()
        partner = Learning_Partner.objects.all()
        trainer_info = Trainer.objects.all()
        leads = Training_Lead.objects.all()
        countries = [{"key":"USA", "value": "usa"},
                        {"key":"India", "value": "in"},
                            {"key": "Canada", "value": "ca"},
                                {"key":"Pakistan", "value": "pk"}]

        if request.method == "POST":
            handel_by = request.POST.get("handel_by")
            learning_partner = request.POST.get("learning_partner")
            assign_to_trainer = request.POST.get("assign_to_trainer")
            course_name = request.POST.get("course_name")
            lead_type = request.POST.get("lead_type")
            getting_lead_date = request.POST.get("getting_lead_date")
            time_zone = request.POST.get("time_zone")
            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")
            lead_status = request.POST.get("lead_status")


            obj = Training_Lead(
                handel_by_id=handel_by,
                learning_partner_id=learning_partner,
                assign_to_trainer_id=assign_to_trainer,
                course_name=course_name,
                lead_type=lead_type,
                getting_lead_date=getting_lead_date,
                time_zone=time_zone,
                start_date=start_date,
                end_date=end_date,
                lead_status=lead_status,
            )
            obj.save()
            print(obj)

        df = {
            "users": users,
            "trainer": trainer,
            "partner": partner,
            "trainer_info": trainer_info,
            "leads": leads,
            "countries": countries,
        }
        return render(request, "add_Lead.html", df)
    else:
        return redirect("router")


def edit_leads(request, id):
    if request.user.is_authenticated:
        users = UserInstance.objects.all()
        partner = Learning_Partner.objects.all()
        trainer_info = Trainer.objects.all()
        leads_info = Training_Lead.objects.all()
        leads = Training_Lead.objects.get(id=id)

        if request.method == "POST":
            handel_by = request.POST.get("handel_by")
            learning_partner = request.POST.get("learning_partner")
            assign_to_trainer = request.POST.get("assign_to_trainer")
            course_name = request.POST.get("course_name")
            lead_type = request.POST.get("lead_type")
            lead_status = request.POST.get("lead_status")
            lead_description = request.POST.get("lead_description")

            
            leads.handel_by_id = handel_by
            leads.learning_partner_id = learning_partner
            leads.assign_to_trainer_id = assign_to_trainer
            leads.course_name = course_name
            leads.lead_type = lead_type
            leads.lead_status = lead_status
            leads.lead_description = lead_description

            print(leads)
            leads.save()
            print(leads)
        df = {
            "users": users,
            "partner": partner,
            "trainer_info": trainer_info,
            "leads": leads,
            "leads_info": leads_info,
        }
        # return redirect("leadhist")
        return render(request, "edit_leads.html", df)
    else:
        return redirect("router")


def trainers_for_schedule_date(request):
    if request.user.is_authenticated:
        user = UserInstance.objects.all()
        partner = Learning_Partner.objects.all()
        trainer_info = Trainer.objects.all()
        leads = Training_Lead.objects.all()

        df = {
            "user": user,
            "partner": partner,
            "trainer_info": trainer_info,
            "leads": leads,
        }
        return render(request, "trainers_for_schedule_date.html", df)
    else:
        return redirect("router")




def report_for_lead_status(request):
    if request.user.is_authenticated:
        user = UserInstance.objects.all()
        partner = Learning_Partner.objects.all()
        trainer_info = Trainer.objects.all()
        if request.method == "POST":

            lead_status = request.POST.get("lead_status", default="")
            trainers_info = Training_Lead.objects.filter(
                lead_status__contains=lead_status
            )
            trainer_info_not_active = Training_Lead.objects.exclude(
                lead_status__contains=lead_status
            )
            print(trainers_info)
            df = {
                "user": user,
                "partner": partner,
                "lead_status": lead_status,
                "trainers_info": trainers_info,
                "trainer_info": trainer_info,
                "trainer_info_not_active": trainer_info_not_active,
            }
        return render(request, "status_report.html", df)
    else:
        return redirect("router")


def status_reports(request):
    if request.user.is_authenticated:
        user = UserInstance.objects.all()
        partner = Learning_Partner.objects.all()
        trainer_info = Trainer.objects.all()
        # if request.method == 'POST':
        # lead_status = request.POST.get('lead_status', default="")
        # trainers = Training_Lead.objects.filter(lead_status__contains=lead_status)

        df = {"user": user, "partner": partner, "trainer_info": trainer_info}

        return render(request, "status_report.html", df)
    else:
        return redirect("router")


def report_for_trainer(request):
    if request.user.is_authenticated:
        user = UserInstance.objects.all()
        partner = Learning_Partner.objects.all()
        trainer_info = Trainer.objects.all()
        trainer = Training_Lead.objects.all()
        if request.method == "POST":

            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")
            lead_status = request.POST.get("lead_status", default="")
            assign_to_trainer = request.POST.get("assign_to_trainer")

            trainers_info = Training_Lead.objects.filter(start_date__gte=start_date,
                                        end_date__lte=end_date,
                                        lead_status__contains=lead_status,
                                        assign_to_trainer=assign_to_trainer,
            )
            trainer_info_not_active = Training_Lead.objects.exclude(
                start_date__gte=start_date,
                end_date__lte=end_date,
                lead_status__contains=lead_status,
            )
            
            df = {"user": user, "partner": partner,"start_date": start_date,"end_date":end_date,"trainer":trainer,"lead_status":lead_status,"assign_to_trainer":assign_to_trainer, "lead_status": lead_status,"trainers_info": trainers_info, "trainer_info": trainer_info, "trainer_info_not_active": trainer_info_not_active}
        return render(request, "trainers_for_schedule_date.html", df)
    else:
        return redirect("router")


def export_data_to_excel(request):
    if request.method == "POST":
            leads = Training_Lead.objects.all()
            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")
            lead_status = request.POST.get("lead_status", default="")
            assign_to_trainer = request.POST.get("assign_to_trainer")
            objs = Training_Lead.objects.filter(
                start_date__gte=start_date,
                end_date__lte=end_date,
                lead_status__contains=lead_status,
                assign_to_trainer=assign_to_trainer,
            )
            data = []

            for obj in objs:
                data.append({
                    "handel_by" : obj.handel_by,
                    "learning_partner" : obj.learning_partner,
                    "assign_to_trainer" : obj.assign_to_trainer,
                    "course_name" : obj.course_name,
                    "lead_type" : obj.lead_type,
                    "time_zone" : obj.time_zone,
                    "getting_lead_date" : obj.getting_lead_date,
                    "start_date" : obj.start_date,
                    "end_date" : obj.end_date,
                    "lead_status" : obj.lead_status,
                    "lead_description" : obj.lead_description
                })
            T= datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            pd.DataFrame(data).to_csv("Training_Reports_"+str(T)+ ".csv")
    return render(request, "trainers_for_schedule_date.html", {"leads":leads})


def available_trainers(request):
    if request.user.is_authenticated:
        trainer = Trainer.objects.all() 
        leads = Training_Lead.objects.all()
        df = {"trainer": trainer, "leads": leads}
        if request.method == "POST":
            searched = request.POST.get("searched")
            trainers = Trainer.objects.filter(
                trainer_skill_set__contains=searched)

        return render(request,"Available_trainers.html",df)
    else:
        return redirect("router")

def report_for_trainer_skill(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            searched = request.POST.get("searched")
            trainers = Trainer.objects.filter(trainer_skill_set__contains=searched)


        # df2 = {"searched": searched, "trainers": trainers}
        return render(request,"trainer_skill.html")
    else:
        return redirect("router")


def all_leads(request):
    if request.user.is_authenticated:
        users = UserInstance.objects.all()
        leads = Training_Lead.objects.all()
        initial = Training_Lead.objects.filter(lead_status="Initial")
        in_progress = Training_Lead.objects.filter(lead_status="In Progress")
        follow_up = Training_Lead.objects.filter(lead_status="Follow Up")
        cancelled = Training_Lead.objects.filter(lead_status="Cancelled")
        confirmed = Training_Lead.objects.filter(lead_status="Confirmed")
        po_received = Training_Lead.objects.filter(lead_status="PO Received")
        df = {"leads": leads, "users": users,"cancelled":cancelled,"confirmed":confirmed,"po_received":po_received, "initial":initial,"in_progress":in_progress,"follow_up":follow_up}
        return render(request,"all_leads.html", df)
    else:
        return redirect("router")
    




def all_trainer(request):
    if request.user.is_authenticated:
        users = UserInstance.objects.all()
        all_trainers = Trainer.objects.all()
        df = {"all_trainer": all_trainers, "users": users}
        return render(request,"all_trainer.html", df)
    else:
        return redirect("router")
    
    

def all_users(request):
    if request.user.is_authenticated:
        users = UserInstance.objects.all()
        all_trainers = Trainer.objects.all()
        df = {"all_trainer": all_trainers, "users": users}
        return render(request,"all_users.html", df)
    else:
        return redirect("router")
    
    
def all_lerning_partner(request):
    if request.user.is_authenticated:
        users = UserInstance.objects.all()
        all_lerning_partners = Learning_Partner.objects.all()
        df = {"all_lerning_partners": all_lerning_partners, "users": users}
        return render(request,"all_lerning_partner.html", df)
    else:
        return redirect("router")


def checkStatus(list):
    if len(list) == 1:
        return True
    for item in list[1:]:
        if item != list[0]:
            return False
        return True

        
def search_a_skill(request):
    users = UserInstance.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            searched = request.POST.get("searched")
            trainers = Trainer.objects.filter(
                trainer_skill_set__contains=searched)
            print(trainers)
            free_trainers = []
            for single_trainer in trainers:
                print(single_trainer,"-------------single_trainer")
                is_present = Training_Lead.objects.filter(assign_to_trainer=single_trainer.trainer_id)
                print(is_present,"-------------is_present")
                if is_present:
                    status_list = [x.lead_status for x in is_present]
                    print(status_list, "------------Status list")
                    if "Cancelled" in status_list:
                        if checkStatus(status_list):
                            free_trainers.append(single_trainer)
                            print(free_trainers, "--------------------------free_trainers")
                        else:
                            pass
                    else:
                        pass
                else:
                    free_trainers.append(single_trainer)


            df = {"free_trainers": free_trainers, "users": users, "searched": searched}

        return render(request,
            "search_a_trainer.html",df)
    else:
        return redirect("router")


def free_trainer(request):
    users = UserInstance.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            searched = request.POST.get("searched")
            trainers = Trainer.objects.filter(
                trainer_skill_set__contains=searched)
            print(trainers)
            free_trainers = []
            for single_trainer in trainers:
                print(single_trainer,"-------------single_trainer")
                is_present = Training_Lead.objects.filter(assign_to_trainer=single_trainer.trainer_id)
                print(is_present,"-------------is_present")
                if is_present:
                    status_list = [x.lead_status for x in is_present]
                    print(status_list, "------------Status list")
                    if "Cancelled" in status_list:
                        if checkStatus(status_list):
                            free_trainers.append(single_trainer)
                            print(free_trainers, "--------------------------free_trainers")
                        else:
                            pass
                    else:
                        pass
                else:
                    free_trainers.append(single_trainer)


            df = {"free_trainers": free_trainers, "users": users, "searched": searched}

        return render(request,
            "search_a_trainer.html",df)
    else:
        return redirect("router")

def training_leadHist(request, id):
    users = UserInstance.objects.all()
    leads = Training_Lead.objects.all()
    if request.user.is_authenticated:
        lead_hist = Training_LeadHist.objects.filter(training_lead_id=id)

        df = {"users":users, "leads":leads, "lead_hist":lead_hist}
        return render(request, "leadhist.html", df)
    else:
        return redirect("router")


def leadhist(request):
    users = UserInstance.objects.all()
    leads = Training_Lead.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            print(request.POST)
            training_lead_id = request.POST.get("training_lead_id")
            updated_user = request.user
            handel_by = request.POST.get("handel_by")
            learning_partner = request.POST.get("learning_partner")
            assign_to_trainer = request.POST.get("assign_to_trainer")
            course_name = request.POST.get("course_name")
            lead_type = request.POST.get("lead_type")
            time_zone = request.POST.get("time_zone")
            getting_lead_date = request.POST.get("getting_lead_date")
            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")
            lead_status = request.POST.get("lead_status")
            lead_description = request.POST.get("lead_description")

            history = Training_LeadHist(training_lead_id=training_lead_id,updated_user=updated_user,handel_by=handel_by,learning_partner=learning_partner,assign_to_trainer=assign_to_trainer,course_name=course_name,lead_type=lead_type, time_zone=time_zone,getting_lead_date=getting_lead_date,start_date=start_date,end_date=end_date, lead_status=lead_status, lead_description=lead_description,)

            history.save()
            print(history)

            return redirect(f"/edit_leads/{training_lead_id}")

        df = {"users":users, "leads":leads}
        return render(request, "leadhist.html", df)
    else:
        return redirect("router")


def lead_hist_download(request):
    leads = Training_Lead.objects.all()
    if request.method == "POST":
            
            training_lead_id = request.POST.get("training_lead_id")
            updated_user = request.POST.get("updated_user")
            

            download_hist = Training_LeadHist.objects.filter( training_lead_id=training_lead_id,)
            data = []

            for obj in download_hist:
                data.append({
                    "training_lead_id" : obj.training_lead_id,
                    "updated_user" : obj.updated_user,
                    "updated_time" : obj.updated_time,
                    "handel_by" : obj.handel_by,
                    "learning_partner" : obj.learning_partner,
                    "assign_to_trainer" : obj.assign_to_trainer,
                    "course_name" : obj.course_name,
                    "lead_type" : obj.lead_type,
                    "time_zone" : obj.time_zone,
                    "getting_lead_date" : obj.getting_lead_date,
                    "start_date" : obj.start_date,
                    "end_date" : obj.end_date,
                    "lead_status" : obj.lead_status,
                    "lead_description" : obj.lead_description,
                })

                print(data)
            
            T= datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            pd.DataFrame(data).to_csv("LeadHistory_"+str(T)+ ".csv")
    return render(request, "leads.html", {"leads":leads})
