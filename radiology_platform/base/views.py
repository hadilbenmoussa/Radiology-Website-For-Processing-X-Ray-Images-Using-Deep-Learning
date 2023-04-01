from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.contrib import messages
from .models import Post,Subscribers
from.forms import SubscribersForm



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

def newsletterView(request):
    if request.method=='POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            existing_subscriber = get_object_or_none(Subscribers, email=email)
            if existing_subscriber:
                messages.success(request,'Already Subscribed')
            else:
                messages.success(request,'Subscription Successful')
                form.save()
                return redirect('/newsletter')    
                
      
    else :
        form=SubscribersForm()
   
    context = {
        'form' : form,
    }
    return render(request, 'base/newsletter.html',context)
def aboutus(request):
    return render(request, 'base/aboutus.html')

def get_object_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None
