from turtle import pd
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout as logouts
from django.contrib.auth.models import auth
import datetime
from django.utils import timezone
from .models import *
from .forms import *
import pdb
from pytz import country_timezones
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

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
        df = {"trainer": trainer, "leads": leads}
        return render(request, "home.html", df)
    else:
        return redirect("login_page")


def add_trainer(request):
    if request.method == "POST":
        pdb.set_trace()
        form = TrainerForm(request.POST, request.FILES)
        print("EEEEEEEEEEEEEEEEEEE", request.FILES)
        if form.is_valid():
            form.save()
        return render(request, "add_trainer.html", {"form": form})
    else:
        form = TrainerForm()
        return render(request, "add_trainer.html", {"form": form})


def trainer_info(request, trainer_id):
    if request.user.is_authenticated:
        info = Trainer.objects.get(trainer_id=trainer_id)
        leads = Training_Lead.objects.all()

        df = {"infor": info, "leads": leads}
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
            
            trainer_attachment = request.FILES["trainer_attachment"]

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
            info.trainer_attachment = trainer_attachment
            print("eeeeeeeeeeeeeeee", info.trainer_attachment)
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

            obj = Learning_Partner(name=name)
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
            searched = request.POST.get("searched")
            trainers = Trainer.objects.filter(trainer_name__contains=searched)

        return render(
            request,
            "search_a_trainer.html",
            {"searched": searched, "trainers": trainers, "leads": leads},
        )
    else:
        return redirect("router")


def login_page(request):
    if request.user.is_authenticated:
        print("hello")
        return redirect("router")

    else:
        print("hello else")
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
            password = request.POST.get("password")

            user = UserInstance.objects.create_user(
                username=username, email=email, password=password
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
        user = UserInstance.objects.all()
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
            getting_lead_date = request.POST.get("getting_lead_date")
            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")
            lead_status = request.POST.get("lead_status")
            

            obj = Training_Lead(
                handel_by_id=handel_by,
                learning_partner_id=learning_partner,
                assign_to_trainer_id=assign_to_trainer,
                course_name=course_name,
                getting_lead_date=getting_lead_date,
                start_date=start_date,
                end_date=end_date,
                lead_status=lead_status,
            )
            obj.save()
            print(obj)

        df = {
            "user": user,
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
        user = UserInstance.objects.all()
        partner = Learning_Partner.objects.all()
        trainer_info = Trainer.objects.all()
        leads_info = Training_Lead.objects.all()
        leads = Training_Lead.objects.get(id=id)

        if request.method == "POST":
            handel_by = request.POST.get("handel_by")
            learning_partner = request.POST.get("learning_partner")
            assign_to_trainer = request.POST.get("assign_to_trainer")
            course_name = request.POST.get("course_name")
            lead_status = request.POST.get("lead_status")

            leads.handel_by_id = handel_by
            leads.learning_partner_id = learning_partner
            leads.assign_to_trainer_id = assign_to_trainer
            leads.course_name = course_name
            leads.lead_status = lead_status

            print(leads)
            leads.save()
            print(leads)
        df = {
            "user": user,
            "partner": partner,
            "trainer_info": trainer_info,
            "leads": leads,
            "leads_info": leads_info,
        }
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


def search_a_skill(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            searched = request.POST.get("searched")
            trainers = Trainer.objects.filter(
                trainer_skill_set__contains=searched)

        return render(
            request,
            "search_a_trainer.html",
            {"searched": searched, "trainers": trainers},
        )
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
        if request.method == "POST":

            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")
            lead_status = request.POST.get("lead_status", default="")
            trainers_info = Training_Lead.objects.filter(
                start_date__gte=start_date,
                end_date__lte=end_date,
                lead_status__contains=lead_status,
            )
            trainer_info_not_active = Training_Lead.objects.exclude(
                start_date__gte=start_date,
                end_date__lte=end_date,
                lead_status__contains=lead_status,
            )
            print(trainers_info)
            df = {"user": user, "partner": partner, "lead_status": lead_status, "trainers_info": trainers_info, "trainer_info": trainer_info, "trainer_info_not_active": trainer_info_not_active}
        return render(request, "trainers_for_schedule_date.html", df)
    else:
        return redirect("router")


# def report_for_trainer_skill(request):
#     if request.user.is_authenticated:
#         user = UserInstance.objects.all()
#         partner = Learning_Partner.objects.all()
#         trainer_info = Trainer.objects.all()
#         leads_info = Training_Lead.objects.all()
#         df = {
#             "user": user,
#             "partner": partner,
#             "trainer_info": trainer_info,
#             "leads_info": leads_info,
#         }

#         if request.method == "POST":
#             print(request.POST)
#             searched = request.POST.get("searched")
#             trainers = Trainer.objects.filter(trainer_skill_set__contains=searched)
            


#         return render(request, "trainer_skill.html",{'trainers':trainers},)
#     else:
#         return redirect("router")



def report_for_trainer_skill(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            searched = request.POST.get("searched")
            trainers = Trainer.objects.filter(trainer_skill_set__contains=searched)


        # df2 = {"searched": searched, "trainers": trainers}
        return render(request,"trainer_skill.html")
    else:
        return redirect("router")



