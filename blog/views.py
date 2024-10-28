from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/blogpost_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return BlogPost.objects.filter(published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blogpost_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=["views"])
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "blog/blogpost_form.html"
    fields = ["title", "content", "preview_image", "published"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view"] = {"title": "Create New Blog Post"}
        return context

    def get_success_url(self):
        return reverse("blog:blogpost_detail", kwargs={"pk": self.object.pk})


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog/blogpost_form.html"
    fields = ["title", "content", "preview_image", "published"]

    def get_success_url(self):
        return reverse("blog:blogpost_detail", args=[self.object.pk])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/blogpost_confirm_delete.html"
    success_url = reverse_lazy("blog:blogpost_list")
