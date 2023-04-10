from django.shortcuts import render, redirect
from app.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Avg, Count, Min, Sum


@login_required(login_url='/')
def LOCAL_DASHBOARD(request):
    employee = Employee.objects.filter(admin=request.user.id)
    petrol_consume = 0
    disel_consume = 0
    
   
    for i in employee:
        employee_id = i.id
        employee_coupon = FuelExpense.objects.filter(Q(employee_id=employee_id) & Q(status = 1)).order_by('-id')[0:3] 
        coupon_count = FuelExpense.objects.filter(Q(employee_id=employee_id) & Q(status = 1)).count() 
        petrol_consume = petrol_consume + FuelExpense.objects.filter(Q(employee_id=employee_id) & Q(fueltype='1') & Q(
        status=1)).aggregate(petrol_consume_sum=Sum('liter'))['petrol_consume_sum']
        if  FuelExpense.objects.filter(Q(employee_id=employee_id) & Q(fueltype='2') & Q(
        status=1)).aggregate(disel_consume_sum=Sum('liter'))['disel_consume_sum'] == None:
            
            disel_consume = disel_consume
        else:
            
            disel_consume = FuelExpense.objects.filter(Q(employee_id=employee_id) & Q(fueltype='2') & Q(
        status=1)).aggregate(disel_consume_sum=Sum('liter'))['disel_consume_sum']

        context = {
            "employee_coupon": employee_coupon,
            "petrol_consume":petrol_consume,
            "disel_consume":disel_consume,
            "coupon_count":coupon_count,
        }

         
        return render(request, "Local/home.html", context)





@login_required(login_url='/')
def HOME(request):
    employee = Employee.objects.filter(admin=request.user.id)
   
    for i in employee:
        employee_id = i.id
        employee_coupon = FuelExpense.objects.filter(Q(employee_id=employee_id) & Q(status=0))
        context = {
            "employee_coupon": employee_coupon
        }

        return render(request, "Local/view_coupon.html", context)
    

    


@login_required(login_url='/')
def ADD_COUPON(request, id):
    employee = Employee.objects.filter(id=id)
    objective = Objective.objects.all()
    petrolpump = Petrolpump.objects.all()
    fueltype = FuelType.objects.all()
    fiscal_year = FiscalYear.objects.all()
    context = {
        "employee": employee,
        "petrolpump": petrolpump,
        "fueltype": fueltype,
        "fiscal_year": fiscal_year,
        "objective": objective,
    }

    return render(request, 'Local/add_coupon.html', context)


@login_required(login_url='/')
def EDIT_EMPLOYEE(request, id):
    employee = Employee.objects.filter(id=id)
    department = Department.objects.all()
    workplace = WorkPlace.objects.all()
    context = {
        "employee": employee,
        "department": department,
        "workplace": workplace,
    }
    return render(request, 'Hod/edit_employee.html', context)


@login_required(login_url='/')
def VIEW_COUPON(request):
    employee = Employee.objects.filter(admin=request.user.id).order_by('-id')

    for i in employee:
        employee_id = i.id
        employee_coupon = FuelExpense.objects.filter(employee_id=employee_id)

        context = {
            "employee_coupon": employee_coupon
        }

        return render(request, "Local/view_coupon.html", context)


@login_required(login_url='/')
def STAFF_ADD_COUPON(request):

    employee = Employee.objects.filter(admin=request.user.id)
    objective = Objective.objects.all()
    petrolpump = Petrolpump.objects.all()
    fueltype = FuelType.objects.all()
    fiscal_year = FiscalYear.objects.all()
    context = {
        "employee": employee,
        "petrolpump": petrolpump,
        "fueltype": fueltype,
        "fiscal_year": fiscal_year,
        "objective": objective,
    }
    return render(request, 'Local/ask_coupon.html', context)


@login_required(login_url='/')
def ISSUE_COUPON(request):
    if request.method == "POST":
        fiscal_year_id = request.POST.get('fiscal_year')
        coupon_date = request.POST.get('date')
        employee_id = request.POST.get('employee_id')
        name = Employee.objects.get(admin=employee_id)

        petrolpump_id = request.POST.get('petrolpump_name')
        fuel_type_id = request.POST.get('fuel_type')
        liter = request.POST.get('liter')
        objective_id = request.POST.get('objective')

        fiscal_year = FiscalYear.objects.get(id=fiscal_year_id)
        petrolpump = Petrolpump.objects.get(id=petrolpump_id)
        fuel_type = FuelType.objects.get(id=fuel_type_id)
        objective = Objective.objects.get(id=objective_id)

        coupon = FuelExpense(
            employee=name,
            patrolpump=petrolpump,
            fueltype=fuel_type,
            liter=liter,
            date=coupon_date,
            fiscalyear=fiscal_year,
            objective = objective

        )
        coupon.save()
        messages.success(request, 'Your request has been sent')
        return redirect('view_staff_coupon')

    return render(request, 'Local/view_staff_coupon.html')

