from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            # save the form
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)

def edit_item(request, item_id):
    # get the item
    # item = Item.objects.get(id=item_id)
    item = get_object_or_404(Item, id=item_id)
    # check if the request is a POST
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = ItemForm(request.POST, instance=item)
        # check if the form is valid
        if form.is_valid():
            # save the form
            form.save()
            return redirect('get_todo_list')
    # if the request is not a POST, create a blank form
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)

def toggle_item(request, item_id):
    # get the item
    item = get_object_or_404(Item, id=item_id)
    # toggle the item.done value
    item.done = not item.done
    # save the item
    item.save()
    # redirect to the todo list
    return redirect('get_todo_list')

def delete_item(request, item_id):
    # get the item
    item = get_object_or_404(Item, id=item_id)
    # delete the item
    item.delete()
    # redirect to the todo list
    return redirect('get_todo_list')
