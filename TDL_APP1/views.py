from django.db.models.query import QuerySet
from django.shortcuts import render
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

from TDL_APP1.forms import ContentCreationForm
from TDL_APP1.models import Content_Article

def home(request):
    target_content_list = Content_Article.objects.all()
    return render(request, 'TDL_APP1/home.html', context={'target_content_list': target_content_list})

# 함수형 뷰로 표현한다면 더 길어졌을 것임.
class ContentCreateView(CreateView):
    model = Content_Article
    form_class = ContentCreationForm
    template_name = 'TDL_APP1/create.html'

    def get_success_url(self):
        return reverse('TDL_APP1:detail', kwargs={'pk':self.object.pk})

class ContentDetailView(DetailView):
    model = Content_Article
    context_object_name = 'target_content' # detail.html에서 user정보 보여줄 때 user라고 쓰면 다른 사람이 해당 사이트를 사용할 때 보여주는 정보가 해당 유저의 정보가 아니라 내 정보일 가능성이 있기 떄문에 다음과 같이 대상 유저를 가리키는 명칭을 target_user 등으로 바꿔준다. 바꾸면 앞의 우려를 예방할 수 있다. / (content_object_name을 따로 정의하지 않고 계속 [detail.html 등에서] user로 쓸 경우, 로그인한 사람의 pk가 아니라 로그인한 다른 사람의 pk로 detail.html 페이지에 접속했을 때 보려고 친 pk에 해당하는 유저의 정보가 아니라 로그인한 유저의 정보가 나올 가능성이 있기 때문)
    template_name = 'TDL_APP1/detail.html'

class ContentUpdateView(UpdateView):
    model = Content_Article
    context_object_name = 'target_content'
    form_class = ContentCreationForm  # Create할 때와 내용 비슷하기 때문
    template_name = 'TDL_APP1/update.html'

    def get_success_url(self):
        return reverse('TDL_APP1:detail', kwargs={'pk':self.object.pk})

class ContentDeleteView(DeleteView):
    model = Content_Article
    context_object_name = 'target_content'
    template_name = 'TDL_APP1/delete.html'
    success_url = reverse_lazy('TDL_APP1:home')

class ContentListView(ListView):
    model = Content_Article
    context_object_name = 'context_list'
    template_name = 'TDL_APP1/home.html'
    paginate_by = 5