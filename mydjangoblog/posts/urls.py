from django.urls import path
from . import views as posts_views
from django.views.generic import ListView, DetailView
from .models import Post

# lista dei post | homepage del blog
# post singoli del blog
# sezione contatti

urlpatterns = [
        path('', ListView.as_view(
            queryset = Post.objects.all().order_by("-data"),
            template_name = "lista_post.html",
            paginate_by = 3), name="lista"),

        path('<id>/<slug>/', DetailView.as_view(
            model = Post,
            template_name = "post_singolo.html"), name="singolo"),

        path('contatti/', posts_views.contatti, name="contatti"),
]