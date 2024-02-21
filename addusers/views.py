from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from addusers.models import Addusers, Position
from addusers.forms import AddUserForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# Create your views here.
def index(request):
    users_list = Addusers.objects.all()
    context = {'users_list': users_list}
    return render(request, 'addusers/index.html', context)

def create(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addusers:index')
    else:
        form = AddUserForm()

    positions = Position.objects.all()  # Get all positions to pass to the template

    context = {'form': form, 'positions': positions}
    return render(request, 'addusers/addUser.html', context)

def edit(request, id):
    user = get_object_or_404(Addusers, id=id)
    form = AddUserForm(instance=user)
    context = {'user': user, 'form': form, 'position': Position.objects.all()}
    return render(request, 'addusers/editUser.html', context)

def update(request, id):
    user = get_object_or_404(Addusers, id=id)

    if request.method == 'POST':
        form = AddUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('addusers:edit', args=(user.id,)))
    else:
        form = AddUserForm(instance=user)

    context = {'user': user, 'form': form, 'position': Position.objects.all()}
    return render(request, 'addusers/editUser.html', context)

def delete(request, user_id):
    try:
        user = Addusers.objects.get(pk=user_id)
        user.delete()
    except Addusers.DoesNotExist:
        pass

    return redirect('addusers:index')


