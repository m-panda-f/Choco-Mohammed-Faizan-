from django.shortcuts import render, redirect, get_object_or_404
from .models import Flvr, Ingr, Fdbk

# Home view
def home(request):
    return render(request, 'home.html')

def delete_flvr(request, flvr_id):
    flvr = get_object_or_404(Flvr, id=flvr_id)
    flvr.delete()
    return redirect('flavors')

def delete_ingr(request, ingr_id):
    ingr = get_object_or_404(Ingr, id=ingr_id)
    ingr.delete()
    return redirect('ingredients')

# Flavor views
def flavors(request):
    if request.method == 'POST':
        flvr_name = request.POST.get('flvr_name')
        szn = request.POST.get('szn')
        if flvr_name and szn:
            Flvr.objects.create(flvr_name=flvr_name, szn=szn)
    all_flavors = Flvr.objects.all()
    return render(request, 'flavors.html', {'all_flavors': all_flavors})

# Ingredient views
def ingredients(request):
    if request.method == 'POST':
        ingr_name = request.POST.get('ingr_name')
        qty = request.POST.get('qty')
        if ingr_name and qty:
            Ingr.objects.create(ingr_name=ingr_name, qty=int(qty))
    all_ingredients = Ingr.objects.all()
    return render(request, 'ingredients.html', {'all_ingredients': all_ingredients})

# Feedback views
def feedback(request):
    if request.method == 'POST':
        cust_name = request.POST.get('cust_name', 'Anon')
        flvr_sugg = request.POST.get('flvr_sugg')
        alrgy_warn = request.POST.get('alrgy_warn', '')
        if flvr_sugg:
            Fdbk.objects.create(cust_name=cust_name, flvr_sugg=flvr_sugg, alrgy_warn=alrgy_warn)
    all_feedback = Fdbk.objects.all()
    return render(request, 'feedback.html', {'all_feedback': all_feedback})