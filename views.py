from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .forms import DocForms,PatientForm
from .models import Doctor,Patient
# Create your views here.
def index(request):
    return render(request,"index.html")
def success(request):
    return render(request,"success.html")

def appointment(request):
    data=Doctor.objects.all()
    return render(request,'appointment.html',{'data':data})
def details(request):
    form=PatientForm()
    return render(request,'details.html',{'form':form})
def save(request):
    
    if request.method =='POST':
        form =PatientForm(request.POST,request.FILES)  
        if form.is_valid():
            form.save()
            form=PatientForm()
            # data_value=Doctor.objects.all()
            # return render(request,'data.html',{'data':data_value})
            return render(request,'data.html')
        else:
            return render(request,'success.html',{'form':form})
        
    else:
         return render(request,'data.html',{'form':form})
     
def delete_data(request,id):
    Doctor.objects.filter(id=id).delete()
    return redirect('data') 
def edit_data(request,id):
    instance= get_object_or_404(Doctor, id=id)
    form = DocForms(instance=instance)
    return render(request,"appointment.html" ,{'form':form,'instance':instance})


def update(request,pk=None):
    
    if request.method =='POST':
        if pk is not None:
            instance = Patient.objects.get(pk=pk)
            form =PatientForm(request.POST,instance=instance)  
            if form.is_valid():
                form.save()
                data_value=Doctor.objects.all()
                return render(request,'details.html',{'datas':data_value})
               
            else:
                return render(request,'appointment.html',{'form':form})
        
        else:
            return redirect('appointment')
    
    else:
         return render(request,'details.html',{'form':form})
     
def data(request):
    data=Patient.objects.all()
    return render(request,'data.html',{'datas':data})
def add(request):
    data=DocForms()
    return render(request,'add.html',{'datas':data})