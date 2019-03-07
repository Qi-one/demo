from django.conf.urls import url


from users import views

urlpatterns = [
    # 配置子路由
    url(r'^index/', views.index),
]