from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

class CustomLoginView(auth_views.LoginView):
    template_name = 'info/login.html'
    
    def dispatch(self, request, *args, **kwargs):
        # If user is already logged in, redirect to home
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

def logout_view(request):
    """Custom logout view that accepts GET requests"""
    logout(request)
    return redirect('/accounts/login/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('', include('info.urls')),
    path('info/', include('info.urls')),
    path('api/', include('apis.urls')),
]
