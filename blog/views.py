from django.shortcuts import render

# render puts together the template
def post_list(request):
    return render(request, 'blog/post_list.html', {})
