from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'base/home.html')
def requestappointment(request):
    return render(request, 'base/requestappointment.html')
def patientcare(request):
    return render(request, 'base/patientcare.html')



class blogHomeView(ListView):
    model=Post
    template_name='base/blog.html'
    context_object_name = 'blog_posts'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_posts'] = Post.objects.order_by('-created')[:6]
        return context
class ArticlesView(ListView):
    model=Post
    template_name='base/articles.html'
    context_object_name = 'all_articles'
    ordering = ['-created']
    paginate_by = 2
    
class blogDetailsView(DetailView):
    model=Post
    template_name='base/blog_details.html'    
def blog(request):
    return render(request, 'base/blog.html')
def aboutus(request):
    return render(request, 'base/aboutus.html')

