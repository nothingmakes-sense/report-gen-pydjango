from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.GenerateReportsView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Patient URLs
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
    path('patients/create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('patients/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient_update'),
    path('patients/<int:pk>/delete/', views.PatientDeleteView.as_view(), name='patient_delete'),
    
    # Provider URLs
    path('providers/', views.ProviderListView.as_view(), name='provider_list'),
    path('providers/create/', views.ProviderCreateView.as_view(), name='provider_create'),
    path('providers/<int:pk>/update/', views.ProviderUpdateView.as_view(), name='provider_update'),
    path('providers/<int:pk>/delete/', views.ProviderDeleteView.as_view(), name='provider_delete'),
    # Add existing URLs here

    path('reports/', views.ReportListView.as_view(), name='report_list'),
    path('reports/<int:pk>/delete/', views.ReportDeleteView.as_view(), name='report_delete'),
    path('get_report_preview/<int:report_id>/', views.get_report_preview, name='get_report_preview'),
    
    # path('', views.patient_list, name='patient_list'),
    # path('patient/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('generate_reports/', views.GenerateReportsView.as_view(), name='generate_reports'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('create_user/', views.CreateUserView.as_view(), name='create_user'),
    path('delete_user/<int:pk>/', views.UserDeleteView.as_view(), name='delete_user'),
]