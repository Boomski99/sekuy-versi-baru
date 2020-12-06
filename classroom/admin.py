from django.contrib import admin

from .models import *

#data admin
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Materi)
admin.site.register(VideoPembelajaran)
admin.site.register(User)