from django.shortcuts import render, redirect
from django.contrib import messages
from .models import List
from .form import NewForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def form_view(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            new_todo = List(name=form.cleaned_data['name'],
                            title=form.cleaned_data['title'],
                            content=form.cleaned_data['content'])
            new_todo.save()
            messages.success(request, "Added successfully")
            return redirect('todo:list_view')

        messages.warning(request, "Error")
    new_form = NewForm()
    template = 'form.html'
    return render(request, template_name=template, context={"form": new_form})


def list_view(request):
    template = 'list.html'
    return render(request, template_name=template, context={'all_items': List.objects.all()})


def delete_view(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, "Deleted successfully")
    return redirect('todo:list_view')


def todo_view(request, view_id):
    item = List.objects.get(pk=view_id)
    template = 'view.html'
    return render(request, template_name=template, context={"item": item})
