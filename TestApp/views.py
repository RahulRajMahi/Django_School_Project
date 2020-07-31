from django.shortcuts import render

# Create your views here.
def view_home(request):
    return render(request, 'TestApp/home.html')

def view_student(request):
    return render(request, 'TestApp/student.html')

def view_teacher(request):
    return render(request, 'TestApp/teacher.html')

def view_book(request):
    return render(request, 'TestApp/book.html')
