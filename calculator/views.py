from django.shortcuts import render, redirect
from calculator.models import Charm, Selection


# Create your views here.
def index(request):
    charms = Charm.objects.all()

    return render(request, 'index.html', {
        'charms': charms,
    })


def edit_charm(request, slug):
    charm = Charm.objects.get(slug=slug)

    return render(
        request,
        'charms/edit_charm.html',
        {
            'charm': charm,
        }
    )


def results(request):
    charms = Charm.objects.filter(selection=1)
    total_motes = 0
    total_will = 0
    total_anima = 0
    total_bashing = 0
    total_lethal = 0
    total_initiative = 0

    for charm in charms:
        total_motes = total_motes + charm.mote_cost
        total_will = total_will + charm.willpower_cost
        total_anima = total_anima + charm.anima_cost
        total_bashing = total_bashing + charm.bashing_cost
        total_lethal = total_lethal + charm.lethal_cost
        total_initiative = total_initiative + charm.initiative_cost

    return render(
        request,
        'charms/results.html',
        {
            'charms': charms,
            'total_motes': total_motes,
            'total_will': total_will,
            'total_anima': total_anima,
            'total_bashing': total_bashing,
            'total_lethal': total_lethal,
            'total_initiative': total_initiative,
        }
    )


def selected_charms(request):
    charms = Charm.objects.all()

    return render(
        request,
        'charms/selected_charms.html',
        {'charms': charms}
    )


def reset(request):
    charms = Charm.objects.all()

    for charm in charms:
        charm.selection = None
        charm.save()

    return redirect('home')


def activate_charm(request, slug):
    next = request.GET.get('next')

    charm = Charm.objects.get(slug=slug)
    charm.selection = Selection.objects.first()
    charm.save()

    # TODO: redirect back to previous page
    # return redirect('home')
    return redirect(next)


def deactivate_charm(request, slug):
    next = request.GET.get('next')

    charm = Charm.objects.get(slug=slug)
    charm.selection = None
    charm.save()

    # TODO: redirect back to previous page
    # return redirect('home')
    return redirect(next)
#


def brawl(request):
    ability = 'brawl'

    return ability_selection(request, ability)


def athletics(request):
    ability = 'athletics'

    return ability_selection(request, ability)


def occult(request):
    ability = 'occult'

    return ability_selection(request, ability)


def resistance(request):
    ability = 'resistance'

    return ability_selection(request, ability)


def evocations(request):
    ability = 'evocations'

    return ability_selection(request, ability)


def ability_selection(request, ability):
    charms = Charm.objects.filter(ability=ability)

    return render(
        request,
        'charms/ability.html',
        {
            'charms': charms,
            'ability': ability
        }
    )

#   <p>{{ number }}</p>
# add the preceding code (or variation) in appropriate html file

# TODO: find a way to dynamically add text to page, with line breaks,
# as more options are selected
