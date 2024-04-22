from django.shortcuts import render
from django.contrib import messages
from .forms import ExcelUploadForm
from .models import ATMSite, State, City
from django.shortcuts import render, get_object_or_404
from .models import ATMSite
import openpyxl
import json

def upload_excel(request):
    import pdb
    pdb.set_trace()
    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['file']
            
            workbook = openpyxl.load_workbook(excel_file)
            sheet = workbook.active
            
            for row in sheet.iter_rows(min_row=2, values_only=True):
                name, site_id, address, state_name, city_name, person_name, phone, email = row
                
                state, created = State.objects.get_or_create(name=state_name)
                city, created = City.objects.get_or_create(name=city_name, state=state)
                
                contact_details = json.dumps({
                    'name': person_name,
                    'phone': phone,
                    'email': email
                })
                
                ATMSite.objects.create(
                    name=name,
                    site_id=site_id,
                    address=address,
                    state=state,
                    city=city,
                    contact_details=contact_details
                )
            
            messages.success(request, "File uploaded and processed successfully!")
            return render(request, 'atm_management/upload.html', {'form': form})
    else:
        form = ExcelUploadForm()
    
    return render(request, 'atm_management/upload.html', {'form': form})


def atm_site_list(request):
    sites = ATMSite.objects.all()
    return render(request, 'atm_management/atm_site_list.html', {'sites': sites})

def atm_site_detail(request, site_id):
    site = get_object_or_404(ATMSite, site_id=site_id)
    return render(request, 'atm_management/atm_site_detail.html', {'site': site})