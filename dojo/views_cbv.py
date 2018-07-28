from django.http import JsonResponse, HttpResponse
from django.views.generic import View ,TemplateView

class PostListView1(View):
    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)
    pass
post_list1 = PostListView1.as_view() 


class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'
    pass
post_list2 = PostListView2.as_view


class PostListView3(object):
    pass

class ExcelDownloadView(object):
    pass            