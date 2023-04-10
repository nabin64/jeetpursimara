from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *

# from app.models import Course, Session_Year, CustomUser, Student, Staff, Subject,
from django.contrib import messages
from django.db.models import Avg, Count, Min, Sum
from django.utils.translation import gettext_lazy as _
from django.db.models import Q


@login_required(login_url='/')
def HOME(request):

    petrol_cost = 0
    disel_cost = 0
    rate_petrol = 0
    rate_disel = 0
    total_budget = 0
    employee_count = Employee.objects.all().count()
    department_count = Department.objects.all().count()
    petrolpump_count = Petrolpump.objects.all().count()

    disel_consume = FuelExpense.objects.filter(Q(fueltype='2') & Q(
        status=1)).aggregate(disel_consume_sum=Sum('liter'))['disel_consume_sum']

    petrol_consume = FuelExpense.objects.filter(Q(fueltype='1') & Q(
        status=1)) .aggregate(petrol_consume_sum=Sum('liter'))['petrol_consume_sum']

    coupon_count = FuelExpense.objects.filter(status=1).count()
    if (coupon_count > 0 and disel_consume == None):

        rate_petrol = float(rate_petrol) + \
            float(Budget.objects.values_list('rate_petrol')[0][0])

        rate_disel = float(rate_disel) + \
            float(Budget.objects.values_list('rate_disel')[0][0])
        total_budget = total_budget + \
            float(Budget.objects.values_list('total_budget')[0][0])
        petrol_consume = FuelExpense.objects.filter(Q(fueltype='1') & Q(
            status=1)) .aggregate(petrol_consume_sum=Sum('liter'))['petrol_consume_sum']
        disel_consume = 0
        disel_cost = rate_disel * 0
        petrol_cost = float(petrol_cost) + float(petrol_consume*rate_petrol)
        total_cost = petrol_cost+disel_cost
        fuel = FuelExpense.objects.all().order_by('-id')[0:5]
        context = {
            "disel_consume": disel_consume,
            "employee_count": employee_count,
            "petrolpump_count": petrolpump_count,
            "petrol_consume": petrol_consume,
            "fuel": fuel,
            "petrol_cost": petrol_cost,
            "disel_cost": disel_cost,
            "total_cost": total_cost,
            "total_budget": total_budget,
            "department_count": department_count,
            "coupon_count": coupon_count,
        }

        return render(request, "Hod/home.html", context)
    elif (coupon_count > 0 and petrol_consume == None):
        rate_petrol = float(rate_petrol) + \
            float(Budget.objects.values_list('rate_petrol')[0][0])

        rate_disel = float(rate_disel) + \
            float(Budget.objects.values_list('rate_disel')[0][0])
        total_budget = total_budget + \
            float(Budget.objects.values_list('total_budget')[0][0])
        petrol_consume = 0
        petrol_cost = rate_petrol*petrol_consume
        disel_consume = FuelExpense.objects.filter(Q(fueltype='2') & Q(
            status=1)).aggregate(disel_consume_sum=Sum('liter'))['disel_consume_sum']
        disel_cost = float(disel_cost) + float(rate_disel * disel_consume)
        total_cost = petrol_cost + disel_cost
        fuel = FuelExpense.objects.all().order_by('-id')[0:5]
        context = {
            "disel_consume": disel_consume,
            "employee_count": employee_count,
            "petrolpump_count": petrolpump_count,
            "petrol_consume": petrol_consume,
            "fuel": fuel,
            "petrol_cost": petrol_cost,
            "disel_cost": disel_cost,
            "total_cost": total_cost,
            "total_budget": total_budget,
            "department_count": department_count,
            "coupon_count": coupon_count,
        }

        return render(request, "Hod/home.html", context)
    elif (coupon_count > 0 and (petrol_consume != None and disel_consume != None)):
        rate_petrol = float(rate_petrol) + \
            float(Budget.objects.values_list('rate_petrol')[0][0])

        rate_disel = float(rate_disel) + \
            float(Budget.objects.values_list('rate_disel')[0][0])
        total_budget = total_budget + \
            float(Budget.objects.values_list('total_budget')[0][0])

        disel_consume = FuelExpense.objects.filter(Q(fueltype='2') & Q(
            status=1)).aggregate(disel_consume_sum=Sum('liter'))['disel_consume_sum']

        petrol_consume = FuelExpense.objects.filter(Q(fueltype='1') & Q(
            status=1)) .aggregate(petrol_consume_sum=Sum('liter'))['petrol_consume_sum']

        disel_consume = float(disel_consume)
        disel_cost = float(disel_cost) + float(rate_disel * disel_consume)
        total_cost = petrol_cost + disel_cost
        fuel = FuelExpense.objects.all().order_by('-id')[0:5]
        context = {
            "disel_consume": disel_consume,
            "employee_count": employee_count,
            "petrolpump_count": petrolpump_count,
            "petrol_consume": petrol_consume,
            "fuel": fuel,
            "petrol_cost": petrol_cost,
            "disel_cost": disel_cost,
            "total_cost": total_cost,
            "total_budget": total_budget,
            "department_count": department_count,
            "coupon_count": coupon_count,
        }

        return render(request, "Hod/home.html", context)

    else:
        employee_count = Employee.objects.all().count()
        department_count = Department.objects.all().count()
        coupon_count = 0
        petrolpump_count = Petrolpump.objects.all().count()

        rate_petrol = rate_petrol + \
            Budget.objects.values_list('rate_petrol')[
                0][0]
        rate_disel = rate_disel + \
            Budget.objects.values_list('rate_disel')[
                0][0]
        total_budget = total_budget + \
            Budget.objects.values_list('total_budget')[
                0][0]
        disel_consume = 0
        petrol_consume = 0
        petrol_cost = 0
        disel_cost = 0

        total_cost = petrol_cost+disel_cost
        fuel = FuelExpense.objects.all().order_by('-id')[0:5]
        context = {
            "disel_consume": disel_consume,
            "employee_count": employee_count,
            "petrolpump_count": petrolpump_count,
            "petrol_consume": petrol_consume,
            "fuel": fuel,
            "petrol_cost": petrol_cost,
            "disel_cost": disel_cost,
            "total_cost": total_cost,
            "total_budget": total_budget,

            "department_count": department_count,
            "coupon_count": coupon_count,
        }

        return render(request, "Hod/home.html", context)


@login_required(login_url='/')
def PRINT_COUPON_HOME(request):
    petrol_cost = 0
    disel_cost = 0
    rate_petrol = 0
    rate_disel = 0
    total_budget = 0
    employee_count = Employee.objects.all().count()
    department_count = Department.objects.all().count()
    petrolpump_count = Petrolpump.objects.all().count()

    disel_consume = FuelExpense.objects.filter(Q(fueltype='2') & Q(
        status=1)).aggregate(disel_consume_sum=Sum('liter'))['disel_consume_sum']

    petrol_consume = FuelExpense.objects.filter(Q(fueltype='1') & Q(
        status=1)) .aggregate(petrol_consume_sum=Sum('liter'))['petrol_consume_sum']

    coupon_count = FuelExpense.objects.filter(status=1).count()
    if (coupon_count > 0 and disel_consume == None):

        rate_petrol = float(rate_petrol) + \
            float(Budget.objects.values_list('rate_petrol')[0][0])

        rate_disel = float(rate_disel) + \
            float(Budget.objects.values_list('rate_disel')[0][0])
        total_budget = total_budget + \
            float(Budget.objects.values_list('total_budget')[0][0])
        petrol_consume = FuelExpense.objects.filter(Q(fueltype='1') & Q(
            status=1)) .aggregate(petrol_consume_sum=Sum('liter'))['petrol_consume_sum']
        disel_consume = 0
        disel_cost = rate_disel * 0
        petrol_cost = float(petrol_cost) + float(petrol_consume*rate_petrol)
        total_cost = petrol_cost+disel_cost
        fuel = FuelExpense.objects.all().order_by('-id')[0:5]
        context = {
            "disel_consume": disel_consume,
            "employee_count": employee_count,
            "petrolpump_count": petrolpump_count,
            "petrol_consume": petrol_consume,
            "fuel": fuel,
            "petrol_cost": petrol_cost,
            "disel_cost": disel_cost,
            "total_cost": total_cost,
            "total_budget": total_budget,
            "department_count": department_count,
            "coupon_count": coupon_count,
        }

        return render(request, "Hod/home.html", context)
    elif (coupon_count > 0 and petrol_consume == None):
        rate_petrol = float(rate_petrol) + \
            float(Budget.objects.values_list('rate_petrol')[0][0])

        rate_disel = float(rate_disel) + \
            float(Budget.objects.values_list('rate_disel')[0][0])
        total_budget = total_budget + \
            float(Budget.objects.values_list('total_budget')[0][0])
        petrol_consume = 0
        petrol_cost = rate_petrol*petrol_consume
        disel_consume = FuelExpense.objects.filter(Q(fueltype='2') & Q(
            status=1)).aggregate(disel_consume_sum=Sum('liter'))['disel_consume_sum']
        disel_cost = float(disel_cost) + float(rate_disel * disel_consume)
        total_cost = petrol_cost + disel_cost
        fuel = FuelExpense.objects.all().order_by('-id')[0:5]
        context = {
            "disel_consume": disel_consume,
            "employee_count": employee_count,
            "petrolpump_count": petrolpump_count,
            "petrol_consume": petrol_consume,
            "fuel": fuel,
            "petrol_cost": petrol_cost,
            "disel_cost": disel_cost,
            "total_cost": total_cost,
            "total_budget": total_budget,
            "department_count": department_count,
            "coupon_count": coupon_count,
        }

        return render(request, "Hod/home.html", context)
    elif (coupon_count > 0 and (petrol_consume != None and disel_consume != None)):
        rate_petrol = float(rate_petrol) + \
            float(Budget.objects.values_list('rate_petrol')[0][0])

        rate_disel = float(rate_disel) + \
            float(Budget.objects.values_list('rate_disel')[0][0])
        total_budget = total_budget + \
            float(Budget.objects.values_list('total_budget')[0][0])

        disel_consume = FuelExpense.objects.filter(Q(fueltype='2') & Q(
            status=1)).aggregate(disel_consume_sum=Sum('liter'))['disel_consume_sum']

        petrol_consume = FuelExpense.objects.filter(Q(fueltype='1') & Q(
            status=1)) .aggregate(petrol_consume_sum=Sum('liter'))['petrol_consume_sum']

        disel_consume = float(disel_consume)
        disel_cost = float(disel_cost) + float(rate_disel * disel_consume)
        total_cost = petrol_cost + disel_cost
        fuel = FuelExpense.objects.all().order_by('-id')[0:5]
        context = {
            "disel_consume": disel_consume,
            "employee_count": employee_count,
            "petrolpump_count": petrolpump_count,
            "petrol_consume": petrol_consume,
            "fuel": fuel,
            "petrol_cost": petrol_cost,
            "disel_cost": disel_cost,
            "total_cost": total_cost,
            "total_budget": total_budget,
            "department_count": department_count,
            "coupon_count": coupon_count,
        }

        return render(request, "Hod/home.html", context)

    else:
        employee_count = Employee.objects.all().count()
        department_count = Department.objects.all().count()
        coupon_count = 0
        petrolpump_count = Petrolpump.objects.all().count()

        rate_petrol = rate_petrol + \
            Budget.objects.values_list('rate_petrol')[
                0][0]
        rate_disel = rate_disel + \
            Budget.objects.values_list('rate_disel')[
                0][0]
        total_budget = total_budget + \
            Budget.objects.values_list('total_budget')[
                0][0]
        disel_consume = 0
        petrol_consume = 0
        petrol_cost = 0
        disel_cost = 0

        total_cost = petrol_cost+disel_cost
        fuel = FuelExpense.objects.all().order_by('-id')[0:5]
        context = {
            "disel_consume": disel_consume,
            "employee_count": employee_count,
            "petrolpump_count": petrolpump_count,
            "petrol_consume": petrol_consume,
            "fuel": fuel,
            "petrol_cost": petrol_cost,
            "disel_cost": disel_cost,
            "total_cost": total_cost,
            "total_budget": total_budget,

            "department_count": department_count,
            "coupon_count": coupon_count,
        }

        return render(request, "Hod/home.html", context)


@login_required(login_url='/')
def ADD_EMPLOYEE(request):
    department = Department.objects.all()
    workplace = WorkPlace.objects.all()
    typeemployee = TypeEmployee.objects.all()
    if request.method == "POST":
        # profile_pic = request.FILES.get('profile_pic')
        appointed_date = request.POST.get('appointed_date')
        name = request.POST.get('name')
        typeemployee_id = request.POST.get('typeemployee')
        
        
        
        workplace_id = request.POST.get('workplace')
        dep_name_id = request.POST.get('dep_name')
        designation = request.POST.get('designation')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        vehicle = request.POST.get('vehicle')
        liscen_no = request.POST.get('liscen_no')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_employee')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_employee')
        else:
            user = CustomUser(

                username=username,
                first_name=name,

                email=email,
                # profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()

            department = Department.objects.get(id=dep_name_id)
            workplace = WorkPlace.objects.get(id=workplace_id)
            typeemployee = TypeEmployee.objects.get(id = typeemployee_id )

            employee = Employee(
                admin=user,
                appointed_date=appointed_date,
                name=name,
                workplace=workplace,
                department=department,
                designation=designation,
                mobile=mobile,
                email=email,
                vehicle=vehicle,
                liscen_no =liscen_no,
                typeemployee = typeemployee,
            )
            employee.save()
            messages.success(request, user.first_name + "  " +
                             "Are Successfully Added !")
            return redirect('view_employee')

    context = {
        "department": department,
        "workplace": workplace,
        "typeemployee":typeemployee,
    }
    return render(request, 'Hod/add_employee.html', context)


@login_required(login_url='/')
def VIEW_EMPLOYEE(request):
    employee = Employee.objects.all()
    context = {
        "employee": employee
    }
    return render(request, "Hod/view_employee.html", context)


@login_required(login_url='/')
def EDIT_EMPLOYEE(request, id):
    employee = Employee.objects.filter(id=id)
    department = Department.objects.all()
    workplace = WorkPlace.objects.all()
    typeemployee = TypeEmployee.objects.all()
    context = {
        "employee": employee,
        "department": department,
        "workplace": workplace,
        "typeemployee":typeemployee,
    }
    return render(request, 'Hod/edit_employee.html', context)


@login_required(login_url='/')
def UPDATE_EMPLOYEE(request):

    if request.method == "POST":
      

        # profile_pic = request.FILES.get('profile_pic')
        appointed_date = request.POST.get('appointed_date')
        name = request.POST.get('name')
        typeemployee_id = request.POST.get('typeemployee')
        workplace_id = request.POST.get('workplace')
        department_id = request.POST.get('dep_name')
        employee_id = request.POST.get('employee_id')
        email = request.POST.get('email')

        designation = request.POST.get('designation')
        mobile = request.POST.get('mobile')

        password = request.POST.get('password')
        vehicle = request.POST.get('vehicle')
        liscen_no = request.POST.get('liscen_no')
        user = CustomUser.objects.get(id=employee_id)

        user.first_name = name
        user.email = email

        # if profile_pic != None and profile_pic != '':
        #     user.profile_pic = profile_pic
        if password != None and password != '':
            user.set_password(password)
        user.save()
        workplace = WorkPlace.objects.get(id=workplace_id)
        department = Department.objects.get(id=department_id)
        typeemployee = TypeEmployee.objects.get(id = typeemployee_id )
        employee = Employee.objects.get(admin=employee_id)
        employee.appointed_date = appointed_date
        employee.name = name
        employee.email = email
        employee.typeemployee = typeemployee

        employee.designation = designation
        employee.mobile = mobile
        employee.vehicle = vehicle
        employee.liscen_no = liscen_no
        
        employee.workplace_id = workplace
        employee.department_id = department
        employee.save()
        messages.success(request, 'Records are successfully updated')
        return redirect('view_employee')

    return render(request, 'Hod/edit_employee.html')


@login_required(login_url='/')
def VIEW_DEPARTMENT(request):
    department = Department.objects.all()
    context = {
        "department": department
    }
    return render(request, "Hod/view_department.html", context)


@login_required(login_url='/')
def VIEW_PETROLPUMP(request):
    petrolpump = Petrolpump.objects.all()
    context = {
        "petrolpump": petrolpump
    }
    return render(request, "Hod/view_petrolpump.html", context)


@login_required(login_url='/')
def ADD_DEPARTMENT(request):
    department = Department.objects.all().order_by('-id')[0:5]
    context = {
        "department": department
    }

    if request.method == "POST":
        dep_name = request.POST.get('dep_name')

        department = Department(
            dep_name=dep_name
        )
        department.save()
        return redirect("add_department")

    return render(request, 'Hod/add_department.html', context)


def ADD_FUEL_OBJECTIVE(request):
    objective = Objective.objects.all()
    if request.method == "POST":
        objective = request.POST.get('objective')
        obj = Objective(
            name=objective
        )
        obj.save()
        messages.success(request, "Objectives added successfully ")
        return redirect('add_fuel_objective')

    context = {
        "objective": objective
    }

    return render(request, "Hod/add_fuel_objective.html", context)


@login_required(login_url='/')
def ADD_PETROLPUMP(request):
    petrolpump = Petrolpump.objects.all()
    context = {
        "petrolpump": petrolpump
    }

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_petrolpump')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_petrolpump')
        else:
            user = CustomUser(
                first_name=name,
                username=username,
                email=email,
                user_type=3
            )
            user.set_password(password)
            user.save()
            petrolpump = Petrolpump(
                name=name,
                address=address,
                contact=contact,
            )
            petrolpump.save()
            messages.success(request, "Petorlpump added successfully ")
            return redirect('add_petrolpump')

    return render(request, 'Hod/add_petrolpump.html', context)


@login_required(login_url='/')
def ISSUE_COUPON(request):
    if request.method == "POST":
        fiscal_year_id = request.POST.get('fiscal_year')
        coupon_date = request.POST.get('date')
        employee_id = request.POST.get('employee_id')
        name = Employee.objects.get(admin=employee_id)
        objective_id = request.POST.get('objective')
        petrolpump_id = request.POST.get('petrolpump_name')
        fuel_type_id = request.POST.get('fuel_type')
        liter = request.POST.get('liter')

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
            objective=objective,
        )
        coupon.save()
        messages.success(request, 'Records are successfully Saved')
        return redirect('view_request_coupon')

    return render(request, 'Hod/view_coupon.html')


@login_required(login_url='/')
def PRINT_COUPON(request, id):
    coupon = FuelExpense.objects.get(id=id)
    context = {
        "coupon": coupon,
    }
    coupon.status = 1
    coupon.save()
    return render(request, 'Hod/print_coupon.html', context)


@login_required(login_url='/')
def VIEW_COUPON(request):
    coupon = FuelExpense.objects.all().order_by('-id')
    context = {
        "coupon": coupon
    }

    return render(request, 'Hod/view_coupon.html', context)


def EDIT_COUPON(request, id):

    coupon = FuelExpense.objects.get(id=id)

    petrolpump = Petrolpump.objects.all()
    fueltype = FuelType.objects.all()
    fiscal_year = FiscalYear.objects.all()
    context = {

        "coupon": coupon,
        "petrolpump": petrolpump,
        "fueltype": fueltype,
        "fiscal_year": fiscal_year,
    }

    return render(request, 'Hod/edit_coupon.html', context)


def UPDATE_COUPON(request):

    if request.method == "POST":
        fiscal_year_id = request.POST.get('fiscal_year_id')
        emp_id = request.POST.get('emp_id')
        petrol_id = request.POST.get('petrol_id')
        fuel_type_id = request.POST.get('fuel_type_id')
        coupon_date = request.POST.get('date')
        coupon_id = request.POST.get('coupon_id')
        liter = request.POST.get('liter')

        emp_name = Employee.objects.get(id=emp_id)
        fiscalyear = FiscalYear.objects.get(id=fiscal_year_id)
        petrol = Petrolpump.objects.get(id=petrol_id)
        fueltype = FuelType.objects.get(id=fuel_type_id)

        coupon = FuelExpense.objects.get(id=coupon_id)
        coupon.employee = emp_name
        coupon.patrolpump = petrol
        coupon.fueltype = fueltype
        coupon.liter = liter
        coupon.date = coupon_date
        coupon.fiscalyear = fiscalyear
        coupon.save()
        messages.success(request, 'Records are successfully updated')
        return redirect('view_request_coupon')

    return render(request, 'Hod/edit_coupon.html')


@login_required(login_url='/')
def REPORT_COUPON_EMPLOYEE(request, id):
    coupon = FuelExpense.objects.filter(employee=id)
    context = {
        "coupon": coupon
    }
    return render(request, "Hod/report_coupon.html", context)


@login_required(login_url='/')
def REPORT_COUPON_PETROLPUMP(request, id):
    coupon = FuelExpense.objects.filter(patrolpump=id)
    context = {
        "coupon": coupon
    }
    return render(request, "Hod/report_coupon.html", context)


@login_required(login_url='/')
def SEARCH_COUPON(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')

        coupon = FuelExpense.objects.filter(date__range=(
            fromdate, todate)) & FuelExpense.objects.filter(patrolpump=request.POST.get('name'))

        context = {
            "coupon": coupon
        }
        return render(request, 'Hod/search_coupon.html', context)

    coupon = FuelExpense.objects.all()
    patrolpump = Petrolpump.objects.all()
    context = {
        "coupon": coupon,
        "patrolpump": patrolpump,

    }
    return render(request, 'Hod/search_coupon.html', context)


@login_required(login_url='/')
def VIEW_REQUESTED_COUPON(request):
    coupon = FuelExpense.objects.filter(status='0').order_by('-id')
    context = {
        "coupon": coupon
    }

    return render(request, 'Hod/view_request_coupon.html', context)


@login_required(login_url='/')
def SEARCH_COUPON_DATEWISE(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')

        coupon = FuelExpense.objects.filter(date__range=(fromdate, todate))

        context = {
            "coupon": coupon
        }
        return render(request, 'Hod/search_coupon_datewise.html', context)

    coupon = FuelExpense.objects.all()
    patrolpump = Petrolpump.objects.all()
    context = {
        "coupon": coupon,
        "patrolpump": patrolpump,

    }
    return render(request, 'Hod/search_coupon_datewise.html', context)


def ADD_WORKPLACE(request):
    if request.method == "POST":
        workplace = request.POST.get('workplace')

        workplace = WorkPlace(
            name=workplace
        )
        workplace.save()
        return redirect("add_workplace")

    workplace = WorkPlace.objects.all()
    context = {
        "workplace": workplace
    }

    return render(request, 'Hod/add_workplace.html', context)


def ADD_FUELTYPE(request):

    if request.method == "POST":
        fueltype = request.POST.get('fueltype')
        fuel = FuelType(
            name=fueltype
        )
        fuel.save()
        return redirect('hod_home')

    fueltype = FuelType.objects.all()
    context = {
        "fueltype": fueltype
    }
    return render(request, "Hod/add_fueltype.html", context)


def ADD_FISCALYEAR(request):
    if request.method == "POST":
        fiscalyear = request.POST.get('fiscalyear')
        fiscal = FiscalYear(
            name=fiscalyear
        )
        fiscal.save()
        return redirect('hod_home')

    fiscalyear = FiscalYear.objects.all()
    context = {
        "fiscalyear": fiscalyear
    }
    return render(request, "Hod/add_fiscalyear.html", context)


def PAID_COUPON(request):
    coupon = FuelExpense.objects.all().order_by('-id')
    context = {
        "coupon": coupon
    }

    return render(request, 'Hod/paid_coupon.html', context)


def PAID_COUPON_NOW(request, id):
    coupon = FuelExpense.objects.get(id=id)
    coupon.payment = 1
    coupon.save()

    return redirect('paid_coupon')


def BUDGET_ENTRY(request):
    if request.method == "POST":
        fiscal_year_id = request.POST.get('fiscal_year')
        rate_petrol = request.POST.get('rate_petrol')
        rate_disel = request.POST.get('rate_disel')
        total_budget = request.POST.get('total_budget')
        fiscal_year = FiscalYear.objects.get(id=fiscal_year_id)

        budget = Budget(
            fiscalyear=fiscal_year,
            rate_petrol=rate_petrol,
            rate_disel=rate_disel,
            total_budget=total_budget
        )
        budget.save()
        return redirect('budget_entry')
    fiscal_year = FiscalYear.objects.all()
    budget = Budget.objects.all()
    context = {
        "fiscal_year": fiscal_year,
        "budget": budget
    }
    return render(request, "Hod/budget.html", context)


def BUDGET_EDIT(request, id):
    budget = Budget.objects.filter(id=id)
    fiscalyear = FiscalYear.objects.all()

    context = {
        "budget": budget,
        "fiscalyear": fiscalyear,
    }

    return render(request, "Hod/edit_budget.html", context)


def BUDGET_UPDATE(request):
    if request.method == "POST":
        budget_id = request.POST.get('budget_id')
        fiscay_year_id = request.POST.get('fiscal_year')
        print(fiscay_year_id)
        rate_petrol = request.POST.get('rate_petrol')
        rate_disel = request.POST.get('rate_disel')
        total_budget = request.POST.get('total_budget')

        fiscal_year = FiscalYear.objects.get(id=fiscay_year_id)
        print(fiscal_year)

        budget = Budget.objects.get(id=budget_id)
        budget.fiscalyear_id = fiscal_year
        budget.rate_petrol = rate_petrol
        budget.rate_disel = rate_disel
        budget.total_budget = total_budget
        budget.save()
        messages.success(request, 'Records successfully updated')
        return redirect('budget_entry')

    return render(request, 'Hod/edit_budget.html')
def ADD_COUPON_RECEIVER_TYPE(request):
    if request.method == "POST":
        name =   request.POST.get('name')
        type = TypeEmployee(
            type = name
        )
        type.save()
        return redirect("add_coupon_receiver_type")
    
    type = TypeEmployee.objects.all()
    
    context = {
        "type":type
    }
    
    return render(request,"Hod/add_coupon_receiver_type.html",context)