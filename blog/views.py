from django.shortcuts import render

# Create your views here.
def post_list_1(request):
    return render(request, 'blog/post_list_1.html', {})

