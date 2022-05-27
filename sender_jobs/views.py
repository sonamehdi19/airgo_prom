from django.shortcuts import render
from .models import SenderJobs, CarrierJobs
from django.views import View
from .models import CarrierJobs, SenderJobs
from .forms import SenderForm, CarrierForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from datetime import datetime, timedelta


class SenderJobListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        sender_posts = SenderJobs.objects.all().order_by('-date_created')
        form = SenderForm()
        context = {
            'sender_posts':   sender_posts,
            'form':   form,
            'job':   'Sender',
        }
        return render(request, 'send.html', context)

    def post(self, request, *args, **kwargs):
        sender_posts = SenderJobs.objects.all().order_by('-date_created')
        from_location = request.POST.get('from')
        to_location = request.POST.get('to')
        due_date = request.POST.get('due')
        phone_number = request.POST.get('phone')
        additional_note = request.POST.get('note')
        item_file = request.FILES['item']
        print('Image ', item_file)

        try:
            due_date = datetime.strptime(due_date, '%d-%m-%Y')
        except:
            due_date = datetime.strptime(due_date, '%d/%m/%Y')

        try:
            sender_jobs_obj = SenderJobs(location=from_location, destination=to_location, due_date=due_date,
                                         add_image=item_file, contact_number=phone_number, additional_note=additional_note, owner=request.user)
            sender_jobs_obj.save()
            return JsonResponse({"success": True, "message": "Job posted successfuly"}, safe=False)

        except Exception as exc:
            print('Exception errors: ', exc)
            return JsonResponse({"success": False, "message": exc}, safe=False)


class CarrierJobListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        carrier_posts = CarrierJobs.objects.all().order_by('-date_created')
        form = CarrierForm()
        context = {
            'carrier_posts':   carrier_posts,
            'form':   form,
            'job':   'Carrier',
        }
        return render(request, 'carry.html', context)

    def post(self, request, *args, **kwargs):
        carrier_posts = CarrierJobs.objects.all().order_by('-date_created')
        from_location = request.POST.get('from')
        departure_date = request.POST.get('departure')
        to_location = request.POST.get('to')
        arrival_date = request.POST.get('arrival')
        phone_number = request.POST.get('phone')
        additional_note = request.POST.get('note')

        try:
            carrier_jobs_obj = CarrierJobs(location=from_location, departure_date=departure_date, destination=to_location,
                                           arrival_date=arrival_date, contact_number=phone_number, additional_note=additional_note, owner=request.user)
            carrier_jobs_obj.save()
            return JsonResponse({"success": True, "message": "Job posted successfuly"}, safe=False)

        except Exception as exc:
            print('Exception errors: ', exc)
            return JsonResponse({"success": False, "message": exc}, safe=False)

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


@login_required(login_url='join_page')
def account(request):
    current_user = request.user
    my_posts = CarrierJobs.objects.all().filter(owner=current_user)
    form = CarrierForm()
    context = {'my_posts': my_posts,
               'form': form, }
    return render(request, 'account.html', context)
