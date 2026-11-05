from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import UserForm

def index(request):
    return render(request, "index.html")

def niews(request):
    return render(request, "niews.html")

def product(request):
    return render(request, "product.html")

def products(request):
    categories = Category.objects.all()
    products = Product.objects.select_related("category").all()

    current_category = request.GET.get("category")

    if current_category:
        products = products.filter(category__name=current_category)

    return render(request, "products.html", {
        "categories": categories,
        "products": products,
        "current_category": current_category,
    })

def blog(request):
    return render(request, "blog.html")

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        myname = request.POST.get("name")
        step = request.POST.get("step")
        info = {"myname": myname, "step": step}
        return render(request, 'result.html', {'info': info})
    else:
        return render(request, 'form.html')

def form_model(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('form_model')
    else:
        userform = UserForm()
    return render(request, "form_model.html", {"form": userform})


def success(request):
    return render(request, "success.html")