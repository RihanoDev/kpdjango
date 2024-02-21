from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from message.models import Message
from message.forms import MessageForm
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):
    message_list = Message.objects.all()
    messages = [{'created_at': message.created_at, 'updated_at': message.updated_at, 'id': message.id, 'nim': message.nim, 'name': message.name, 'content': message.content} for message in message_list]

    # Check if the request is an AJAX request or accepts JSON
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
        # If AJAX request or accepts JSON, return JSON response
        return JsonResponse({'message_list': messages})
    else:
        # If not AJAX request and does not accept JSON, render the HTML template
        context = {'message_list': message_list}
        return render(request, 'message/index.html', context)

@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = MessageForm(data)
        if form.is_valid():
            message = form.save()
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
                # If AJAX request or accepts JSON, return JSON response
                return JsonResponse({'id': message.id, 'content': message.content})
            else:
                # If not AJAX request and does not accept JSON, redirect to the index page
                return redirect('message:index')
        else:
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
                # If AJAX request and the form is invalid, return JSON error response
                return JsonResponse({'error': 'Invalid form data', 'errors': form.errors})
            else:
                # If not AJAX request and does not accept JSON, render the HTML form with the invalid form data
                context = {'form': form}
                return render(request, 'message/addMessage.html', context)
    else:
        # If it's a GET request, render the HTML form
        form = MessageForm()
        context = {'form': form}
        return render(request, 'message/addMessage.html', context)
    
@csrf_exempt
def detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
        # If AJAX request or accepts JSON, return JSON response
        data = {'id': message.id, 'content': message.content}
        return JsonResponse(data)
    else:
        # If not AJAX request and does not accept JSON, render the HTML template
        context = {'message': message}
        return render(request, 'message/detailMessage.html', context)

@csrf_exempt
def edit(request, id):
    message = get_object_or_404(Message, id=id)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            message = form.save()
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
                # If AJAX request or accepts JSON, return JSON response
                return JsonResponse({'id': message.id, 'content': message.content})
            else:
                # If not AJAX request and does not accept JSON, redirect to the index page
                return redirect('message:edit', id=message.id)
        else:
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
                # If AJAX request and the form is invalid, return JSON error response
                return JsonResponse({'error': 'Invalid form data'})
            else:
                # If not AJAX request and does not accept JSON, render the HTML form with the invalid form data
                form = MessageForm(instance=message)
                context = {'message': message, 'form': form}
                return render(request, 'message/editMessage.html', context)
    else:
        # If it's a GET request, render the HTML form
        form = MessageForm(instance=message)
        context = {'message': message, 'form': form}
        return render(request, 'message/editMessage.html', context)

@csrf_exempt
def update(request, id):
    message = get_object_or_404(Message, id=id)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            message = form.save()
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
                # If AJAX request or accepts JSON, return JSON response
                return JsonResponse({'id': message.id, 'content': message.content})
            else:
                # If not AJAX request and does not accept JSON, redirect to the detail page
                return redirect('message:detail', pk=message.pk)
        else:
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
                # If AJAX request and the form is invalid, return JSON error response
                return JsonResponse({'error': 'Invalid form data'})
            else:
                # If not AJAX request and does not accept JSON, render the HTML form with the invalid form data
                form = MessageForm(instance=message)
                context = {'message': message, 'form': form}
                return render(request, 'message/editMessage.html', context)
    else:
        form = MessageForm(instance=message)
        context = {'message': message, 'form': form}
        return render(request, 'message/editMessage.html', context)
    
@csrf_exempt
def delete(request, id):
    try:
        message = Message.objects.get(pk=id)
        message.delete()
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
            # If AJAX request or accepts JSON, return JSON response
            return JsonResponse({'message': 'Message deleted successfully'})
        else:
            # If not AJAX request and does not accept JSON, redirect to the index page
            return redirect('message:index')
    except Message.DoesNotExist:
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
            # If AJAX request and the message does not exist, return JSON error response
            return JsonResponse({'error': 'Message does not exist'})
