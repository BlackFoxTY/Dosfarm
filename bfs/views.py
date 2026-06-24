from django.shortcuts import render

# Create your views here.

def bfs(request):
    return render(request, 'bfs/bfs.html', {
        'breadcrumb_title': 'Технология BFS',
        'breadcrumb_title_url': '/bfs/',
    })