from django.contrib import admin

# Register your models here.
from .models import Boxing
admin.site.register(Boxing)

from .models import Wrestling
admin.site.register(Wrestling)

from .models import Athletics
admin.site.register(Athletics)

from .models import Weightlifting
admin.site.register(Weightlifting)

from .models import Cycling
admin.site.register(Cycling)

from .models import Team_sports
admin.site.register(Team_sports)
