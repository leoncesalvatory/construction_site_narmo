from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import ContactForm
from django.core.mail import send_mail

def home(request):
    company = CompanyInfo.objects.first()
    services = Service.objects.all()[:4]
    
    # Footer data
    recent_news = NewsPost.objects.order_by('-date')[:3]
    recent_projects = Project.objects.order_by('-id')[:9]
    
    return render(request, 'core/templates/home.html', {
        'company': company,
        'services': services,
        'recent_news': recent_news,
        'recent_projects': recent_projects,
    })

def about(request):
    company = CompanyInfo.objects.first()
    certifications = Certification.objects.all()
    team = TeamMember.objects.all()
    
    # Footer data
    recent_news = NewsPost.objects.order_by('-date')[:3]
    recent_projects = Project.objects.order_by('-id')[:9]
    
    return render(request, 'core/templates/about.html', {
        'company': company,
        'certifications': certifications,
        'team': team,
        'recent_news': recent_news,
        'recent_projects': recent_projects,
    })

def services(request):
    company = CompanyInfo.objects.first()
    services = Service.objects.all()
    
    # Footer data
    recent_news = NewsPost.objects.order_by('-date')[:3]
    recent_projects = Project.objects.order_by('-id')[:9]
    
    return render(request, 'core/templates/services.html', {
        'company': company,
        'services': services,
        'recent_news': recent_news,
        'recent_projects': recent_projects,
    })

def projects(request):
    company = CompanyInfo.objects.first()
    projects = Project.objects.all()
    
    # Footer data
    recent_news = NewsPost.objects.order_by('-date')[:3]
    recent_projects = Project.objects.order_by('-id')[:9]
    
    return render(request, 'core/templates/projects.html', {
        'company': company,
        'projects': projects,
        'recent_news': recent_news,
        'recent_projects': recent_projects,
    })

def news_careers(request):
    company = CompanyInfo.objects.first()
    news = NewsPost.objects.order_by('-date')[:10]
    jobs = JobPosting.objects.all()
    
    # Footer data
    recent_news = NewsPost.objects.order_by('-date')[:3]
    recent_projects = Project.objects.order_by('-id')[:9]
    
    return render(request, 'core/templates/news_careers.html', {
        'company': company,
        'news': news,
        'jobs': jobs,
        'recent_news': recent_news,
        'recent_projects': recent_projects,
    })

def contact(request):
    company = CompanyInfo.objects.first()
    contact_info = ContactInfo.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                send_mail(
                    'Contact Inquiry from Website',
                    f"Name: {form.cleaned_data['name']}\nPhone: {form.cleaned_data['phone']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}",
                    form.cleaned_data['email'],
                    ['leonce@narmo.co.tz'],
                )
                messages.success(request, 'Thank you! Your message has been sent successfully.')
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
            form = ContactForm()  # Reset form
    else:
        form = ContactForm()
    
    # Footer data
    recent_news = NewsPost.objects.order_by('-date')[:3]
    recent_projects = Project.objects.order_by('-id')[:9]
    
    return render(request, 'core/templates/contact.html', {
        'company': company,
        'contact_info': contact_info,
        'form': form,
        'recent_news': recent_news,
        'recent_projects': recent_projects,
    })