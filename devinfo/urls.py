from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),
    path('api/', include('api.urls')),

    path('reset_password/', auth_view.PasswordResetView.as_view(template_name="reset-password.html"), name='reset_password'),
    path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(template_name="reset-password-sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name="new-password-form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(template_name="reset-password-complete.html"), name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
