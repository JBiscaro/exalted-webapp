from django.shortcuts import render


# Create your views here.
def index(request):
    # use something like commented code to put variables on webpage
    # number = 6

    # return render(request, 'index.html', {'number': number})
    return render(request, 'index.html')

#   <p>{{ number }}</p>
# add something like the preceding code in appropriate html file
