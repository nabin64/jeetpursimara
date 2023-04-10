import os

from django.contrib.auth.models import User
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout


from django.contrib.auth import get_user_model


from django.shortcuts import render
from .models import *

import pandas as pd
from django.http import JsonResponse



class ExcelPageView(TemplateView):
    template_name = "excel_home.html"


# Super User - admin - password




def export_users_xls(request):
    
    
    objs = FuelExpense.objects.filter(status = 1)
    data = []
    for obj in objs:
        data.append({
            "employee": obj.employee,
            "patrolpump": obj.patrolpump,
            "fueltype": obj.fueltype,
            "liter": obj.liter,
             "date": obj.date,
            
        })
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="fuelconsumption.xlsx"'                                        
    df.to_excel(response)
    return response

