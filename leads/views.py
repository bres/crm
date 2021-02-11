from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm


# Create your views here.


def landing_page(request):

    return render(request,"leads/landing.html")


def lead_list(request):
    #return HttpResponse("hello wolrd")
    leads=Lead.objects.all()

    context={
        "leads":leads,
     }
    return render(request,"leads/lead_list.html",context)


def lead_detail(request,pk):
    lead=Lead.objects.get(id=pk)
    context={
        "lead":lead
    } 
    return render(request,"leads/lead_detail.html",context)     


def lead_create(request): 
    #if the request method is not post then assign an empty form
    form=LeadModelForm()
    #if the request method is post then create an object and pass those data
    if request.method=="POST":
        form=LeadModelForm(request.POST)
        #validating the data
        if form.is_valid():
            #clean the data which means simplify their form and pass them to new objects
            #automatically save  the cleaned data
            form.save()
            return redirect("/leads")
    context={
        "form":form
    }
    return render(request,"leads/lead_create.html",context)  



def lead_update(request,pk):
    lead=Lead.objects.get(id=pk)
    form=LeadModelForm(instance=lead)

    if request.method=="POST":
        form=LeadModelForm(request.POST,instance=lead)
        #validating the data
        if form.is_valid():
            #clean the data which means simplify their form and pass them to new objects
            #automatically save  the cleaned data
            form.save()
            return redirect("/leads")
    context={
        "form":form, "lead": lead
    }
    
    return render(request,"leads/lead_update.html",context)  


def lead_delete(request,pk):
    lead=Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")








#option one for model form    
"""
def lead_create(request): 
    #if the request method is not post then assign an empty form
    form=LeadModelForm()
    #if the request method is post then create an object and pass those data
    if request.method=="POST":
        form=LeadModelForm(request.POST)
        #validating the data
        if form.is_valid():
            #clean the data which means simplify their form and pass them to new objects
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            age=form.cleaned_data['age']
            agent=form.cleaned_data['agent']
            #create an object with the past data
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            return redirect("/leads")
    context={
        "form":form
    }
    return render(request,"leads/lead_create.html",context)     


def lead_update(request,pk):
    lead=Lead.objects.get(id=pk)
    form=LeadForm()
    #if the request method is post then create an object and pass those data
    if request.method=="POST":
        form=LeadForm(request.POST)
        #validating the data
        if form.is_valid():
            #clean the data which means simplify their form and pass them to new objects
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            age=form.cleaned_data['age']
            lead.first_name=first_name
            lead.last_name=last_name
            lead.age=age 
            lead.save()        
            return redirect("/leads")
    context={
        "lead":lead,"form":form
    } 
    return render(request,"leads/lead_update.html",context)  

"""