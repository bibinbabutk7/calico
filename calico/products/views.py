from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def banner(request):
    return render(request,'blank_layout.html')

def list_products(request):
    """_summary_
    
    Args:
        request (_type_): _description_
        
    Returns:
        _type_: _description_
        
    """



    return render(request,'product.html')

def detail_products(request):
    return render(request,'product.html')
