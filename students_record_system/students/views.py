from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
import os
FILE_NAME = 'students\students_data.json'
# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    return render(request,'add.html')
def search(request):
    return render(request,'search.html')
def update(request):
    return render(request,'update.html')
def delete(request):
    return render(request,'delete.html')

def insert(request):
    try :
        std_name = request.POST['name']
        std_rno = request.POST['r_no']
        std_age = request.POST['age']
        std_gender = request.POST['gender']
        new_data = {}
        
        new_data['name'] = std_name
        new_data['rollno'] = std_rno
        new_data['age']=std_age
        new_data['gender']=std_gender
        with open(FILE_NAME,'r+') as file:
            file_data = json.load(file)
            file_data['students_data'].append(new_data)
            file.seek(0)
            result = json.dump(file_data, file, indent = 4)
        return HttpResponse("successfully inserted")
    except Exception as e:
        return e

def find(request):
    result = ""
    std_r_no = request.POST['r_no']
    f_data = read_file(FILE_NAME)
    for dt in f_data['students_data']:
        if std_r_no in dt['rollno']:
            result = dt.items()
            break
        else:
            result = "Result Not Found"

    return HttpResponse(result)
def read_file(file_name):
    with open(FILE_NAME,'r+') as file:
        file_data = json.load(file)
    return file_data

def change(request):
    result = ""
    field = request.POST['attr']
    new_value = request.POST['change_data']
    r_no = request.POST['r_no']
    

    with open(FILE_NAME,'r+') as file:
        f_data = json.load(file)
        for dt in f_data['students_data']:
            if r_no in dt['rollno']:
                dt[field]= new_value
                file.seek(0)
                json.dump(f_data, file, indent = 4)
                result = "Updated Successfully"
                break
            else:
                result = "Data Not Found"
    return HttpResponse (result)

def remove(request):
    result = ""
    std_r_no = request.POST['r_no']
    with open(FILE_NAME,'r+') as file:
        f_data = json.load(file)
        for dt in f_data['students_data']:
            if std_r_no in dt['rollno']:
                f_data['students_data'].remove(dt)
                file.seek(0)
                json.dump(f_data, file, indent = 4)
                result = "Successfully deleted"
                break
        else:
            result = "Recorde no found"
    return HttpResponse(result)





    




 