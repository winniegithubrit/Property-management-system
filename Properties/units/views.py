from django.shortcuts import render,redirect,get_object_or_404
from .models import Property
from django.http import JsonResponse
from .forms import PropertyForm
from django.views.decorators.csrf import csrf_exempt
import json
def home_redirect(request):
    return render(request, 'home.html', {})

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties':properties})


def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'property_detail.html', {'property':property})


def create_new_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list') 
    else:
        form = PropertyForm() 

   
    return render(request, 'create_new_property.html', {'form': form})


def update_existing_property(request, pk):
    
    property = get_object_or_404(Property, pk=pk)
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list') 
    else:  
        form = PropertyForm(instance=property)  

    return render(request, 'update_existing_property.html', {'form': form})

@csrf_exempt  
def patch_property(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)  
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        form = PropertyForm(data, instance=property)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)



def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.method == 'POST':
        property.delete()
        return redirect('property_list')  

    return render(request, 'delete_property.html', {'property': property})





