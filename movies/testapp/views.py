from django.shortcuts import render
from testapp.forms import movies_form
def movies_views(request):
    name=''
    submmited=False
    if request.method=='POST':
        form=movies_form(request.POST)
        if form.is_valid():
            print("data send successful")
            form.save(commit=True)
        name=form.cleaned_data['name']
        submmited=True
    form=movies_form()
    return render(request,'testapp/movies_form.html',{'form':form,'name':name,'submmited':submmited})

from testapp.models import movies_db
def movies_db_views(request):
    data=movies_db.objects.all()
    return render(request,'testapp/movies_table.html',{'data':data})
def main(request):
    return render(request,'testapp/main.html')
