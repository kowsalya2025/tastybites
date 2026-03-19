from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# ── HOME ──
def home(request):
    return render(request, 'foodapp/home.html', {
        'trending_posts': [],  # replace with your model query later
    })


# ── BLOGS ──
def blogs(request):
    return render(request, 'foodapp/blogs.html')


# ── RECIPES ──
def recipes(request):
    return render(request, 'foodapp/recipes.html')


# ── WRITE ──
@login_required(login_url='account')
def write(request):
    return render(request, 'foodapp/write.html')


# ── SEARCH ──
from django.shortcuts import render
from .models import Recipe

def search(request):

    query = request.GET.get('q')

    results = []

    if query:
        results = Recipe.objects.filter(title__icontains=query)

    return render(request, "foodapp/search.html", {
        "query": query,
        "results": results
    })



from django.shortcuts import redirect
from django.contrib import messages
from .models import Subscriber


def subscribe(request):

    if request.method == "POST":

        email = request.POST.get("email")

        if Subscriber.objects.filter(email=email).exists():
            messages.warning(request, "You are already subscribed!")

        else:
            Subscriber.objects.create(email=email)
            messages.success(request, "Subscribed successfully!")

    return redirect(request.META.get('HTTP_REFERER'))

# ── POST DETAIL ──
def post_detail(request, slug):
    return render(request, 'foodapp/post_detail.html', {'slug': slug})


# ── LOGIN ─

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

def account_view(request):
    login_form = AuthenticationForm()
    register_form = UserCreationForm()

    if request.method == 'POST':

        # 🔴 LOGIN
        if 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)

            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')

        # 🟢 REGISTER
        elif 'register' in request.POST:
            register_form = UserCreationForm(request.POST)

            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                messages.success(request, f'Account created! Welcome, {user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Please fix the errors below.')

    # ✅ Eye toggle fix
    login_form.fields['password'].widget.attrs.update({'id': 'password'})

    from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

def account_view(request):
    login_form = AuthenticationForm()
    register_form = UserCreationForm()

    if request.method == 'POST':

        # 🔴 LOGIN
        if 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)

            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')

        # 🟢 REGISTER
        elif 'register' in request.POST:
            register_form = UserCreationForm(request.POST)

            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                messages.success(request, f'Account created! Welcome, {user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Please fix the errors below.')

    # ✅ Eye toggle fix
    login_form.fields['password'].widget.attrs.update({'id': 'password'})

# LOGIN placeholders
    login_form.fields['username'].widget.attrs.update({
    'placeholder': 'Enter username or Email Id'
    })

    login_form.fields['password'].widget.attrs.update({
    'placeholder': 'Enter password'
    })

# REGISTER placeholders
    register_form.fields['username'].widget.attrs.update({
    'placeholder': 'Enter username or Email Id'
    })

    register_form.fields['password1'].widget.attrs.update({
    'placeholder': 'Create password'
    })

    register_form.fields['password2'].widget.attrs.update({
    'placeholder': 'Confirm password'
    })

    return render(request, 'foodapp/account.html', {
        'login_form': login_form,
        'register_form': register_form
    })

# ── LOGOUT ──
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')





# ── IMPORTS (TOP OF FILE) ──
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# ── PROFILE ──
@login_required(login_url='account')
def profile(request):
    return render(request, 'foodapp/write.html')


# ── WRITE BLOG ──
@login_required
def write(request):
    return render(request, 'foodapp/write_blog.html')


# ── CREATE BLOG ──
@login_required
def create_blog(request):
    if request.method == 'POST':
        title    = request.POST.get('title', '')
        desc     = request.POST.get('description', '')
        content  = request.POST.get('content', '')
        category = request.POST.get('category', '')
        tags     = request.POST.get('tags', '')
        cover    = request.FILES.get('cover_image')

        # Example save (uncomment when model exists)
        # Blog.objects.create(
        #     author=request.user,
        #     title=title,
        #     description=desc,
        #     content=content,
        #     category=category,
        #     tags=tags,
        #     cover_image=cover
        # )

        return JsonResponse({'success': True, 'redirect_url': '/'})

    return JsonResponse({'success': False, 'message': 'Invalid request'})