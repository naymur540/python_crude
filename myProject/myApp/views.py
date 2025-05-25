from django.shortcuts import render
from myApp.models import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm 

def dashboard(req):
    return render (req,'dashboard.html')
  #student View
def student_view(req):
    student =studentmodel.objects.all()
    context={
        'students':student
    }
    return render(req,'student/index.html',context)
def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        date_of_birth = request.POST.get('date_of_birth')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        address = request.POST.get('address')
        img = request.FILES.get('img')

        student = studentmodel(
            name=name,
            age=age,
            date_of_birth=date_of_birth,
            father_name=father_name,
            mother_name=mother_name,
            address=address,
            img=img
        )
        student.save()
        return redirect('student')

    return render(request, 'student/create.html')
def student_detail(request, id):
    student = get_object_or_404(studentmodel, id=id)
    return render(request, 'student/detail.html', {'student': student})

def student_edit(request, id):
    student = get_object_or_404(studentmodel, id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.date_of_birth = request.POST.get('date_of_birth')
        student.father_name = request.POST.get('father_name')
        student.mother_name = request.POST.get('mother_name')
        student.address = request.POST.get('address')

        if request.FILES.get('img'):
            student.img = request.FILES['img']

        student.save()
        return redirect('student')
    
    return render(request, 'student/edit.html', {'student': student})

def student_delete(request, id):
    student = get_object_or_404(studentmodel, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student')  
    return render(request, 'student/delete.html', {'student': student})



    