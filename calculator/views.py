from django.shortcuts import render


# Create your views here.
def index(request):
    # use something like commented code to put variables on webpage
    number = 'Whatup?\nThis is on a new line?'

    return render(request, 'index.html', {'number': number})
    # return render(request, 'index.html')

#   <p>{{ number }}</p>
# add something like the preceding code in appropriate html file

# TODO: find a way to dynamically add text to page, with line breaks,
# as more options are selected
