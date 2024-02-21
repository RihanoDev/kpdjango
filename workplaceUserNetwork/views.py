from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import WorkplaceUserNetwork, User, Department, Division, Interaction
from workplaceUserNetwork.forms import WorkplaceUserNetworkForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    # Get the filter parameters from the request's GET parameters
    selected_divisions = request.GET.getlist('division')
    selected_interactions = request.GET.getlist('interaction_type')
    selected_month_from = request.GET.get('month_from')
    selected_month_to = request.GET.get('month_to')

    # Filter the queryset based on the selected filters
    workplace_user_network = WorkplaceUserNetwork.objects.all()

    if selected_divisions:
        workplace_user_network = workplace_user_network.filter(posting_division__in=selected_divisions)

    if selected_interactions:
        workplace_user_network = workplace_user_network.filter(type_of_interaction__in=selected_interactions)

    if selected_month_from:
        workplace_user_network = workplace_user_network.filter(from_date__month=selected_month_from)

    if selected_month_to:
        workplace_user_network = workplace_user_network.filter(to_date__month=selected_month_to)

    context = {
        'data': workplace_user_network,
        'selected_divisions': selected_divisions,
        'selected_interactions': selected_interactions,
        'selected_month_from': selected_month_from,
        'selected_month_to': selected_month_to,
    }
    return render(request, 'workplaceUserNetwork/index.html', context)

def create(request):
    users = User.objects.all()
    divisions = Division.objects.all()
    departments = Department.objects.all()
    interactions = Interaction.objects.all()

    if request.method == 'POST':
        form = WorkplaceUserNetworkForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data ke database
            return redirect('workplaceUserNetwork:index')
    else:
        form = WorkplaceUserNetworkForm()

    context = {
        'users': users,
        'divisions': divisions,
        'departments': departments,
        'interactions': interactions,
        'form': form,  # Pastikan form di-passing ke template
    }

    return render(request, 'workplaceUserNetwork/createUserNetwork.html', context)

def edit(request, id):
    divisions = Division.objects.all()
    departments = Department.objects.all()
    interactions = Interaction.objects.all()
    workplace_user_network = get_object_or_404(WorkplaceUserNetwork, id=id)

    if request.method == 'POST':
        form = WorkplaceUserNetworkForm(request.POST, instance=workplace_user_network)
        if form.is_valid():
            form.save()
            return redirect('workplaceUserNetwork:index')
    else:
        form = WorkplaceUserNetworkForm(instance=workplace_user_network)

    context = {
        'workplace_user_network': workplace_user_network,
        'form': form,
        'divisions': divisions,
        'departments': departments,
        'interactions': interactions,
    }
    return render(request, 'workplaceUserNetwork/editUserNetwork.html', context)

def update(request, id):
    divisions = Division.objects.all()
    departments = Department.objects.all()
    interactions = Interaction.objects.all()
    workplace_user_network = get_object_or_404(WorkplaceUserNetwork, id=id)

    if request.method == 'POST':
        form = WorkplaceUserNetworkForm(request.POST, instance=workplace_user_network)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('workplaceUserNetwork:edit', args=(workplace_user_network.id,)))
    else:
        form = WorkplaceUserNetworkForm(instance=workplace_user_network)

    context = {'workplace_user_network' : workplace_user_network, 'form' : form, 'division' : divisions, 'department' : departments, 'interaction' : interactions}
    return render(request, 'workplaceUserNetwork/editUserNetwork.html', context)

def detail(request, id):
    # Get the WorkplaceUserNetwork object by its id
    workplace_user_network = get_object_or_404(WorkplaceUserNetwork, id=id)

    # Render the detail template with the workplace_user_network context
    return render(request, 'workplaceUserNetwork/detailUserNetwork.html', {'workplace_user_network': workplace_user_network})

def delete(request, id):
    try:
        workplace_user_network = WorkplaceUserNetwork.objects.get(pk=id)
        workplace_user_network.delete()
    except WorkplaceUserNetwork.DoesNotExist:
        pass

    return redirect('workplaceUserNetwork:index')
