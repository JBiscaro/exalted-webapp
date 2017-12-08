from django.shortcuts import render, redirect
from calculator.forms import CharmForm
from calculator.models import Charm


# Create your views here.
def index(request):
    number = 'Whatup?\nThis is on a new line?'

    charms = Charm.objects.all()

    return render(request, 'index.html', {
        'charms': charms,
        'number': number,
    })


def charm_detail(request, slug):
    charm = Charm.objects.get(slug=slug)

    return render(request, 'charms/charm_detail.html', {'charm': charm})


def edit_charm(request, slug):
    charm = Charm.objects.get(slug=slug)
    form_class = CharmForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=charm)
        if form.is_valid():
            form.save()
            return redirect('charm_detail', slug=charm.slug)
    else:
        form = form_class(instance=charm)

    return render(
        request,
        'charms/edit_charm.html',
        {
            'charm': charm,
            'form': form
        }
    )

#   <p>{{ number }}</p>
# add the preceding code (or variation) in appropriate html file

# TODO: find a way to dynamically add text to page, with line breaks,
# as more options are selected
