from django.contrib import admin

from .models import *

#data admin
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Student)
admin.site.register(Materi)
admin.site.register(VideoPembelajaran)