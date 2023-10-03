from django.db import models
from django.conf import settings

SCRAPE_SERVER_ANNOUNCEMENT: bool = getattr(settings, 'SCRAPE_SERVER_ANNOUNCEMENT')
    
class Announcement(models.Model):
    """
    Represents an abstract announcement.
    """
    author = models.CharField(
        max_length=100,
        verbose_name="Author",
        default="None")

    date = models.DateTimeField(
        verbose_name="Date",
        default="None")

    message = models.TextField(
        max_length=16383,
        verbose_name="Message",
        default="None")

    def __str__(self) -> str:
        return f'Announcement by {self.author} made on {self.date}'

    def get_author(self):
        return self.author

    def get_date(self):
        return self.date

    def get_message(self):
        return self.message

    class Meta:
        abstract = True

class GlobalAnnouncement(Announcement):
    """
    Announcements that have been made to the entire network.
    """
    class Meta:
        verbose_name = "Global Announcement"
        verbose_name_plural = "Global Announcements"

if SCRAPE_SERVER_ANNOUNCEMENT:
    class ServerAnnouncement(Announcement):
        """
        Announcements that have been made for a specific Minecraft server.
        """
        server = models.ForeignKey(
            'gameservers.Server', 
            default=0, 
            on_delete=models.CASCADE)

        def __str__(self) -> str:
            return f'Announcement by {self.author} for {self.server} made on {self.date}'

        def get_server(self):
            return self.server

        class Meta:
            verbose_name = "Server Announcement"
            verbose_name_plural = "Server Announcements"

class DiscordGuild(models.Model):
        """
        The Discord Community/Guild that the Discord Bot is linked to.
        """
        guild_name = models.CharField(
             max_length=200,
            verbose_name="Guild Name",
            default="None")
        
        guild_id = models.BigIntegerField(
            verbose_name="Guild ID",
            default="None")

        invite_link = models.URLField(
            blank=True,
            verbose_name="Discord Invite Link",
            help_text="The invite link to your Discord Server. This is automatically generated by the Discord Bot"
        )
        
        total_members = models.IntegerField(
            verbose_name="Total Members",
            default="None")

        online_members = models.IntegerField(
            verbose_name="Online Members",
            default="None")

        def __str__(self) -> str:
            return self.guild_name

        def get_guild_id(self):
            return self.guild_id

        def get_total_member_count(self):
            return self.total_members

        def get_online_member_count(self):
            return self.online_members

        class Meta:
            verbose_name = "Discord Guild"
            verbose_name_plural = "Discord Guild"


class DiscordBotTasks(models.Model):
        """
        List of tasks the Discord Bot can perform.
        """
        refresh_global_announcements = models.BooleanField(
            default=False)
        
        refresh_server_announcements = models.BooleanField(
            default=False)

        update_members = models.BooleanField(
            default=False,)

        def __str__(self) -> str:
            return f'DiscordBotTasks#{self.pk}'

        class Meta:
            verbose_name = "Discord Bot Tasks"
            verbose_name_plural = "Discord Bot Tasks"
            
            
class DiscordBotInternal(models.Model):
        """
        Interal tracking information used by the application to
        control the discord bot.
        """
        name = models.CharField(
            default="botinternal-stat",
            max_length=150
        )
        
        time_last_stopped = models.DateTimeField(
            default=None,
            null=True
        )

        def __str__(self) -> str:
            return f'DiscordBotInternal#{self.pk}'

        class Meta:
            verbose_name = "Discord Bot Internal"
            verbose_name_plural = "Discord Bot Internal"
