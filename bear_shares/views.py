from django.shortcuts import render


def index(request):
    return render(request, 'bear_shares/index.html')

def create_new_thread(request):
    return render(request, 'bear_shares/create_new_thread.html', {
        'content': ['asdfjkL:LASKDJALK:SDJ']
    })
