from django.shortcuts import render , redirect
from .models import Student , Comment
from django.views.generic.edit import UpdateView , CreateView
from django.utils.text import slugify
from django.contrib.auth import logout
from django.contrib import  messages
# Create your views here.
from .forms import UpdateStudentsProfile



def homePageView(request):
    all_students = Student.objects.all()
    data = {
        'all_std':all_students
    }
    return render(request , 'index.html' , context=data)



def del_std(request , std_id):
    std = Student.objects.filter(pk=std_id)
    std.delete()
    
    return redirect('/')


def full_std_about(request , pk ):
    all_std = Student.objects.select_related("admin").get(id=pk)
    std_payment = Student.objects.filter(payment=True)
    com = Comment.objects.filter(post=pk)   
    data = {
        'pay':std_payment,
        'all_std':all_std,
        'coment':com,
        'len_com':len(com)
    }
    return render(request , 'std.html' , context=data)

  
def add_new_coment(request , pk):
    all_std = Student.objects.select_related("admin").get(id=pk)
    com = Comment.objects.filter(post=pk)   
    data = {
        'all_std':all_std,
        'coment':com,
        'len_com':len(com)
    }
    full_name = request.POST.get('full_name')
    coment = request.POST.get('comment')
    com = Comment.objects.filter(id=pk)
    com.create(post=all_std , user_name=full_name , coments=coment )
    return render(request , 'std.html' , context=data)



def cards(request):
    students = Student.objects.all()
    data = {
        'std':students
    }
    return render(request , 'cards.html' , context=data)


def del_com(request , pk):
    com = Comment.objects.filter(id=pk)
    com.delete()
    
    return redirect('/')


def filter_payment_true(request):
    std = Student.objects.filter(payment=True)
    data = {
        'std_filter':std
    }
    
    return render(request , 'filter.html' , context=data)

def filter_payment_false(request):
    std = Student.objects.filter(payment=False)
    data = {
        'std_filter':std
    }
    
    return render(request , 'filter.html' , context=data)


def filter_age15(request):
    std = Student.objects.filter(age__in=[15 , 16 , 17])
    data = {
        'std_filter':std
    }
    
    return render(request , 'filter.html' , context=data)

def filter_age18(request):
    std = Student.objects.filter(age__gte=19)
    data = {
        'std_filter':std
    }
    
    return render(request , 'filter.html' , context=data)

def filter_age20(request):
    std = Student.objects.filter(age__gte=20)
    data = {
        'std_filter':std
    }
    
    return render(request , 'filter.html' , context=data)

def filter_lvl_green(request):
    std = Student.objects.filter(lavel=3)
    data = {
        'std_filter':std
    }
    
    return render(request , 'filter.html' , context=data)



def filter_lvl_yellow(request):
    std = Student.objects.filter(lavel=2)
    data = {
        'std_filter':std
    }
    
    return render(request , 'filter.html' , context=data)


def filter_lvl_red(request):
    std = Student.objects.filter(lavel=1)
    data = {
        'std_filter':std
    }
    
    return render(request , 'filter.html' , context=data)

def search_method(request):
    if request.method == 'GET':
        search_text = request.GET.get('search_text')
        std = Student.objects.filter(student_name__icontains = search_text)
        if std:
            data = {
                'std_filter':std
            }
            return render(request , 'filter.html' , context=data)
        else:
            return render(request , 'filter.html' , {'result_filter':'sudent not found!'})
    
class Update_student_profile(UpdateView):
    model = Student
    form_class = UpdateStudentsProfile
    success_url = '/'
        
    
def add_new_student(request):
    form_class = UpdateStudentsProfile(request.POST)
    
    if form_class.is_valid():
        std_name = form_class.save(commit=False)
        std_name.slug_name = slugify(std_name.student_name)
        std_name.save()
        return redirect('/')
    return render(request , 'main_app/student_deail.html' , {'form':form_class})
