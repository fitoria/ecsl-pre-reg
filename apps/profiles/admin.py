from django.contrib import admin
from models import UserProfile

admin.site.register(UserProfile,
        list_display = ['user', 'edad', 'telefono', 'pais', 
            'gul', 'website'],
        list_filter = ['pais', 'gul'],
        ordering = ['user', 'pais'],
        search_fields = ['user', 'pais'],
        )
