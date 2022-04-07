from django.urls import path
from jobs import views

urlpatterns = [
    path("joblist/", views.joblist, name="joblist"),
    path("job/<int:job_id>/", views.detail, name="detail"),
    #提交简历
    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),

    # 首页自动跳转到 职位列表
    # url(r"^$", views.joblist, name="name"),
    path("", views.joblist, name="name"),
]


