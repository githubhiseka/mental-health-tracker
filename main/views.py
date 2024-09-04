from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306244942',
        'name': 'Abhiseka Susanto',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)