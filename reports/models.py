import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Report(models.Model):
	class AchievementScoreChoices(models.TextChoices):
		VERY_GOOD	= "◎", _("◎")
		GOOD		= "◯", _("◯")
		SOSO		= "△", _("△")
		NG			= "✗", _( "✗")

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	on_date = models.DateField()
	daily_title = models.TextField(blank=True)
	daily_comment = models.TextField(blank=True)
	weekly_target = models.TextField(blank=True)
	achievement_score = models.CharField(
		choices=AchievementScoreChoices,
		blank=True)
	achievement_comment = models.TextField(blank=True)
	goods = models.TextField()
	mores = models.TextField()
	nexts = models.TextField()
	