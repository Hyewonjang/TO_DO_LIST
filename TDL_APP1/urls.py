from django.urls import path

from TDL_APP1.views import ContentListView, home, ContentCreateView, ContentDetailView, ContentUpdateView, ContentDeleteView

app_name = "TDL_APP1"

urlpatterns = [
    path('home/', home, name='home'),
    path('create/', ContentCreateView.as_view(), name='create'), # class view를 불려오려면 함수 view와 달리 뒤에 .as_view()를 붙여야 한다.
    path('detail/<int:pk>', ContentDetailView.as_view(), name='detail'),  # class view를 불려오려면 함수 view와 달리 뒤에 .as_view()를 붙여야 한다.
    path('update/<int:pk>', ContentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ContentDeleteView.as_view(), name='delete'),
]