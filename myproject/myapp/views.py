from django.shortcuts import render

# Create your views here.
# myqpp/views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Student


def hello_world(request, name):
    return HttpResponse("Hello, " + name + "!")


def hi_name(request):
    name = request.GET.get('name')
    if name:
        return HttpResponse("Hi " + name + "!")
    else:
        return HttpResponse("Hi, Bro!")


@csrf_exempt
def hello_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # 获取表单中名为 'name' 的字段值
        if name:
            return HttpResponse(f"Hello, {name}!")
    return HttpResponse("Form not submitted or name field is empty.")


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_add(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    age = request.GET.get('age')

    if first_name and last_name and age:
        new_student = Student(first_name=first_name, last_name=last_name, age=age)  # 根据你的模型字段设置数据
        # 保存学生对象到数据库
        new_student.save()

        # 将多个变量放入字典中作为模板的上下文
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            # 其他变量...
        }

        return render(request, 'success.html', context)  # 可以重定向到成功页面或其他页面
    else:
        return render(request, 'failure.html')
    # 创建一个新的学生对象


