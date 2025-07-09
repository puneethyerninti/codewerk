from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# =============================
# ✅ General Views
# =============================
@login_required(login_url='login')
def home(request):
    return render(request, 'main/index.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=email).exists():
            messages.error(request, 'User already exists!')
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')

    return render(request, 'main/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You’ve been logged out successfully!")
    return redirect('login')

# =============================
# ✅ Static Pages
# =============================
def about(request): return render(request, 'main/about.html')
def frontend(request): return render(request, 'main/frontend.html')
def backend(request): return render(request, 'main/backend.html')

# =============================
# ✅ Frontend Tutorials
# =============================
# HTML
def html(request): return render(request, 'main/html.html')
def html_intro(request): return render(request, 'main/html-intro.html')
def html_structure(request): return render(request, 'main/html-structure.html')
def html_headings(request): return render(request, 'main/html-headings.html')
def html_links_images(request): return render(request, 'main/html-links-images.html')
def html_lists(request): return render(request, 'main/html-lists.html')

# CSS
def css(request): return render(request, 'main/css.html')
def css_intro(request): return render(request, 'main/css-intro.html')
def css_selectors(request): return render(request, 'main/css-selectors.html')
def css_colors(request): return render(request, 'main/css-colors.html')
def css_boxmodel(request): return render(request, 'main/css-boxmodel.html')
def css_flexbox(request): return render(request, 'main/css-flexbox.html')

# JavaScript
def javascript(request): return render(request, 'main/javascript.html')
def js_intro(request): return render(request, 'main/js-intro.html')
def js_variables(request): return render(request, 'main/js-variables.html')
def js_functions(request): return render(request, 'main/js-functions.html')
def js_events(request): return render(request, 'main/js-events.html')
def js_conditions(request): return render(request, 'main/js-conditions.html')

# React
def react_main(request): return render(request, 'main/react.html')
def react_intro(request): return render(request, 'main/react-intro.html')
def react_jsx(request): return render(request, 'main/react-jsx.html')
def react_props(request): return render(request, 'main/react-props.html')
def react_hooks(request): return render(request, 'main/react-hooks.html')
def react_router(request): return render(request, 'main/react-router.html')

# UI/UX
def uiux(request): return render(request, 'main/uiux.html')
def uiux_intro(request): return render(request, 'main/uiux-intro.html')
def uiux_principles(request): return render(request, 'main/uiux-principles.html')
def uiux_wireframes(request): return render(request, 'main/uiux-wireframes.html')
def uiux_research(request): return render(request, 'main/uiux-research.html')
def uiux_accessibility(request): return render(request, 'main/uiux-accessibility.html')

# =============================
# ✅ Backend Tutorials
# =============================
# Python
def python_main(request): return render(request, 'main/python.html')
def python_intro(request): return render(request, 'main/python-intro.html')
def python_variables(request): return render(request, 'main/python-variables.html')
def python_flow(request): return render(request, 'main/python-flow.html')
def python_functions(request): return render(request, 'main/python-functions.html')
def python_oop(request): return render(request, 'main/python-oop.html')

# Django
def django(request): return render(request, 'main/django.html')
def django_intro(request): return render(request, 'main/django-intro.html')
def django_structure(request): return render(request, 'main/django-structure.html')
def django_models(request): return render(request, 'main/django-models.html')
def django_views(request): return render(request, 'main/django-views.html')
def django_forms(request): return render(request, 'main/django-forms.html')

# Others
def restapi(request): return render(request, 'main/restapi.html')
def database(request): return render(request, 'main/database.html')
def git(request): return render(request, 'main/git.html')

def django_intro(request):
    return render(request, 'main/django-intro.html')

def django_structure(request):
    return render(request, 'main/django-structure.html')

def django_models(request):
    return render(request, 'main/django-models.html')

def django_views(request):
    return render(request, 'main/django-views.html')

def django_forms(request):
    return render(request, 'main/django-forms.html')

def restapi_intro(request): return render(request, 'main/restapi-intro.html')
def restapi_principles(request): return render(request, 'main/restapi-principles.html')
def restapi_methods(request): return render(request, 'main/restapi-methods.html')
def restapi_postman(request): return render(request, 'main/restapi-postman.html')
def restapi_drf(request): return render(request, 'main/restapi-drf.html')

def database_sql(request):
    return render(request, 'main/database-sql.html')

def database_design(request):
    return render(request, 'main/database-design.html')

def database_postgresql(request):
    return render(request, 'main/database-postgresql.html')

def database_orm(request):
    return render(request, 'main/database-orm.html')

def database_sqlite(request):
    return render(request, 'main/database-sqlite.html')

def git_basics(request):
    return render(request, 'main/git-basics.html')

def git_branching(request):
    return render(request, 'main/git-branching.html')

def git_remote(request):
    return render(request, 'main/git-remote.html')

def git_merge_rebase(request):
    return render(request, 'main/git-merge-rebase.html')

def git_collaboration(request):
    return render(request, 'main/git-collaboration.html')