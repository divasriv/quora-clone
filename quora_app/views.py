from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, CreateView, ListView, DetailView, RedirectView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib import messages

class RegisterView(FormView):
    ''' View for user registration. '''
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Registration successful! You can now log in.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Registration failed. Please correct the errors below.")
        return super().form_invalid(form)

class LoginView(FormView):
    ''' View for user login. '''
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid login. Please try again. Note that both fields may be case-sensitive.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please enter a correct username and password. Note that both fields may be case-sensitive.")
        return super().form_invalid(form)

class LogoutView(RedirectView):
    ''' View for user logout. '''
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

class HomeView(LoginRequiredMixin, ListView):
    ''' View for the home page displaying questions. '''
    model = Question
    template_name = 'home.html'
    context_object_name = 'questions'

class QuestionCreateView(LoginRequiredMixin, CreateView):
    ''' View for creating a new question. '''
    model = Question
    form_class = QuestionForm
    template_name = 'post_question.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class QuestionDetailView(LoginRequiredMixin, DetailView):
    ''' View for displaying a question and its answers. '''
    model = Question
    template_name = 'question_detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = self.object.answers.all()
        context['form'] = AnswerForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = self.object
            answer.save()
            return redirect('question_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)

class LikeAnswerView(LoginRequiredMixin, RedirectView):
    ''' View for liking an answer. '''
    def get_redirect_url(self, *args, **kwargs):
        answer = get_object_or_404(Answer, id=kwargs['answer_id'])
        user = self.request.user
        if user in answer.likes.all():
            answer.likes.remove(user)
        else:
            answer.likes.add(user)
        return reverse_lazy('question_detail', kwargs={'pk': answer.question.id})
