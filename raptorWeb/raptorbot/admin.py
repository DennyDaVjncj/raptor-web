from django.contrib import admin

from raptorWeb.raptorbot.models import DiscordGuild, GlobalAnnouncement, ServerAnnouncement

admin.site.register(DiscordGuild)
admin.site.register(GlobalAnnouncement)
admin.site.register(ServerAnnouncement)