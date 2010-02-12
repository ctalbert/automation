# Create your views here.

def create(request):
    if request.method == "GET":
       products = Product.get({})
       return render_to_response('testcases/create.html', {'products' : products})

