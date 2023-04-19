from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, JobIssue, Note
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required()
def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'home.html', context)

@login_required()
def job_issue(request, pk):
    category = get_object_or_404(Category, pk=pk)
    categories = Category.objects.all()
    job_issues = JobIssue.objects.filter(category=category)
    query = request.GET.get('q')
    if query:
        job_issues = job_issues.filter(Q(title__icontains=query) | Q(description__icontains=query))
        context = {'category': category, 'categories': categories, 'job_issues': job_issues}
    else:
        context = {'category': category, 'categories': categories, 'job_issues': job_issues}
    return render(request, 'job_issue.html', context)

@login_required()
def create_job_issue(request, pk):
    category = Category.objects.get(id=pk)
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        job_issue = JobIssue.objects.create(category=category, title=title, description=description)
        notes = request.FILES.getlist('attachment')
        for note in notes:
            Note.objects.create(job_issue=job_issue, attachment=note)
        return redirect('job_issue', pk=pk)
    return render(request, 'create_job_issue.html', {'category': category, 'categories': categories})

@login_required()
def delete_job_issue(request, pk, job_pk):
    job_issue = JobIssue.objects.get(id=job_pk)
    job_issue.delete()
    return redirect('job_issue', pk=pk)

@login_required()
def edit_job_issue(request, pk, job_pk):
    job_issue = JobIssue.objects.get(id=job_pk)
    categories = Category.objects.all()
    if request.method == 'POST':
        job_issue.title = request.POST.get('title')
        job_issue.description = request.POST.get('description')
        job_issue.save()
        notes = request.FILES.getlist('attachment')
        for note in notes:
            Note.objects.create(job_issue=job_issue, attachment=note)
        return redirect('job_issue', pk=pk)
    return render(request, 'edit_job_issue.html', {'job_issue': job_issue, 'categories': categories})

@login_required()
def delete_note(request, pk, job_pk, note_pk):
    note = Note.objects.get(id=note_pk)
    note.delete()
    return redirect('edit_job_issue', pk=pk, job_pk=job_pk)
