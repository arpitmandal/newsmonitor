from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Sources
from story.models import Story
from django.utils import timezone
from django.template import loader
from .forms import SourceForm

class IndexView(generic.ListView):
    """View to the Index Page - Sources Page"""
    model =  Sources,Story
    template_name = 'source/index.html'
    context_object_name = 'latest_title_list'
    def get_queryset(self):
        return Sources.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
    """Show details of each Title"""
    model = Sources
    template_name = 'source/source.html'

def source_new(request):
    p= SourceForm(request.POST or None)
    if p.is_valid():
        p.save()
        return HttpResponseRedirect('http://localhost:8000')
    context= {'form':p}
    return render(request, 'source/form.html', context)

def source_del(request,id):
    obj = get_object_or_404(Sources, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('http://localhost:8000')
    context ={
        "obj":obj
    }
    return render(request, "source/delete.html",context)