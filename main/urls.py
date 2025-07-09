from django.urls import path
from . import views

urlpatterns = [
    # ✅ Auth Pages
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ✅ Static Pages
    path('about/', views.about, name='about'),
    path('frontend/', views.frontend, name='frontend'),
    path('backend/', views.backend, name='backend'),

    # ✅ Frontend Overview Pages
    path('frontend/html/', views.html, name='html'),
    path('frontend/css/', views.css, name='css'),
    path('frontend/javascript/', views.javascript, name='javascript'),
    path('frontend/react/', views.react_main, name='react'),
    path('frontend/uiux/', views.uiux, name='uiux'),

    # ✅ HTML Subpages
    path('html/intro/', views.html_intro, name='html-intro'),
    path('html/structure/', views.html_structure, name='html-structure'),
    path('html/headings/', views.html_headings, name='html-headings'),
    path('html/links-images/', views.html_links_images, name='html-links-images'),
    path('html/lists/', views.html_lists, name='html-lists'),

    # ✅ CSS Subpages
    path('frontend/css-intro/', views.css_intro, name='css-intro'),
    path('frontend/css-selectors/', views.css_selectors, name='css-selectors'),
    path('frontend/css-colors/', views.css_colors, name='css-colors'),
    path('frontend/css-boxmodel/', views.css_boxmodel, name='css-boxmodel'),
    path('frontend/css-flexbox/', views.css_flexbox, name='css-flexbox'),

    # ✅ JavaScript Subpages
    path('javascript/intro/', views.js_intro, name='js-intro'),
    path('javascript/variables/', views.js_variables, name='js-variables'),
    path('javascript/functions/', views.js_functions, name='js-functions'),
    path('javascript/events/', views.js_events, name='js-events'),
    path('javascript/conditions/', views.js_conditions, name='js-conditions'),

    # ✅ React Subpages
    path('react/', views.react_main, name='react'),
    path('react/intro/', views.react_intro, name='react_intro'),
    path('react/jsx/', views.react_jsx, name='react_jsx'),
    path('react/props/', views.react_props, name='react_props'),
    path('react/hooks/', views.react_hooks, name='react_hooks'),
    path('react/router/', views.react_router, name='react_router'),

    # ✅ UI/UX Subpages
    path('uiux/intro/', views.uiux_intro, name='uiux-intro'),
    path('uiux/principles/', views.uiux_principles, name='uiux-principles'),
    path('uiux/wireframes/', views.uiux_wireframes, name='uiux-wireframes'),
    path('uiux/research/', views.uiux_research, name='uiux-research'),
    path('uiux/accessibility/', views.uiux_accessibility, name='uiux-accessibility'),

    # ✅ Backend Tutorial Main Pages
    path('python/', views.python_main, name='python'),
    path('django/', views.django, name='django'),
    path('restapi/', views.restapi, name='restapi'),
    path('database/', views.database, name='database'),
    path('git/', views.git, name='git'),

    # ✅ Python Subpages
    path('python/intro/', views.python_intro, name='python-intro'),
    path('python/variables/', views.python_variables, name='python-variables'),
    path('python/flow/', views.python_flow, name='python-flow'),
    path('python/functions/', views.python_functions, name='python-functions'),
    path('python/oop/', views.python_oop, name='python-oop'),

    # ✅ Django Subpages
    path('django-intro/', views.django_intro, name='django-intro'),
    path('django-structure/', views.django_structure, name='django-structure'),
    path('django-models/', views.django_models, name='django-models'),
    path('django-views/', views.django_views, name='django-views'),
    path('django-forms/', views.django_forms, name='django-forms'),
    
    
    path('restapi-intro/', views.restapi_intro, name='restapi-intro'),
    path('restapi-principles/', views.restapi_principles, name='restapi-principles'),
    path('restapi-methods/', views.restapi_methods, name='restapi-methods'),
    path('restapi-postman/', views.restapi_postman, name='restapi-postman'),
    path('restapi-drf/', views.restapi_drf, name='restapi-drf'),

    path('database/sql/', views.database_sql, name='database-sql'),
    path('database/design/', views.database_design, name='database-design'),
    path('database/postgresql/', views.database_postgresql, name='database-postgresql'),
    path('database/orm/', views.database_orm, name='database-orm'),
    path('database/sqlite/', views.database_sqlite, name='database-sqlite'),

    path('git/basics/', views.git_basics, name='git-basics'),
    path('git/branching/', views.git_branching, name='git-branching'),
    path('git/remote/', views.git_remote, name='git-remote'),
    path('git/merge-rebase/', views.git_merge_rebase, name='git-merge-rebase'),
    path('git/collaboration/', views.git_collaboration, name='git-collaboration'),



]
