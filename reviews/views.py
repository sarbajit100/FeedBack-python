from django.http import HttpResponseRedirect 
from django.shortcuts import render 
from .form import ReviewForm
from django.views.generic.base import TemplateView
from django.views import View
# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {"form":form})
    def post(self, request):
        form = ReviewForm(request.POST, )
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank_you")
        return render(request, "reviews/review.html", {"form":form})

class ThankYouView(TemplateView):
    # def get(self, request):
    #     return render(request, "reviews/thankyou.html")
    template_name = "reviews/thankyou.html"


    
    
