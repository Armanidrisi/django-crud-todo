from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm


def home(request):
  tasks = Todo.objects.all()
  if request.method == "POST":
    form = TodoForm(request.POST)
    if form.is_valid():
         form.save()
         return render(request,"index.html",{'alert':'Task Added Success','alert_type':'success','tasks':tasks})
    else:
      form = TodoForm()
      return render(request,"index.html",{'alert':'Please Enter Valid Details','alert_type':'danger','tasks':tasks})
  return render(request,"index.html",{'tasks':tasks})

def deleteTask(request,id):
  todo =Todo.objects.filter(id=id).first()
  if todo:
    todo.delete()
    return redirect("/")
  
def updateTask(request,id):
  todo = Todo.objects.filter(id=id).first()
  if request.method=="POST":
    form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
      form.save()
      tasks = Todo.objects.all()
      return redirect("/")
    else:
        form = TodoForm(instance=todo)
  return render(request,"edit.html",{'task':todo})
  
def about(request):
  return render(request,"about.html")