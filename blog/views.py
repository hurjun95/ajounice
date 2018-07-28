from django.http import Http404
from django.shortcuts import render , get_object_or_404
from .models import post
# Create your views here.

def post_list(request):
    qs = post.objects.all()

    q= request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains=q)
    
    return render(request, 'blog/post_list.html',{
        'post_list': qs,
        'q' : q
    })

def post_detail(request, id):
    #try:
         #post1 = post.objects.get(id=id)
    #except post.DoesNotExist:
        #raise Http404

    post1=get_object_or_404(post, id=id)

    return render(request, 'blog/post_detail.html',{'post':post1,})
