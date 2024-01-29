from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class BaseProduct(models.Model):
	title = models.CharField(verbose_name=_("Название"), unique=True, blank=False, max_length=200)

	price = models.DecimalField(
		verbose_name=_("Стоимость"),
		decimal_places=2,
		max_digits=13,
	)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


class SecondProduct(models.Model):
	title = models.CharField(verbose_name=_("Название"), unique=True, blank=False, max_length=200)
	url = models.URLField(verbose_name=_("Ссылка"), max_length=200)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


class Skill(models.Model):
	name = models.CharField(
		verbose_name=_("Навык"),
		max_length=200,
	)
	description = models.TextField(
		verbose_name=_("Описание навыка"),
	)
	skill_percent = models.PositiveIntegerField(
		verbose_name=_("Процент навыка"),
		validators=[
			MinValueValidator(limit_value=0, message=_("Минимальный процент навыка 0")),
			MaxValueValidator(limit_value=100, message=_("Максимальный процент навыка 100")),
		],
	)

	class Meta:
		ordering = ["name"]
		verbose_name = _("Навык")
		verbose_name_plural = _("Навыки")

	def __str__(self):
		return self.name


class Level(models.Model):
	profession = models.CharField(verbose_name=_("Профессия"), unique=True, blank=False, max_length=200)
	level = models.CharField(verbose_name=_("Грейт"), unique=True, blank=False, max_length=200)

	class Meta:
		ordering = ["profession"]
		verbose_name = _("Уровень профессии")
		verbose_name_plural = _("Уровни профессии")

	def __str__(self):
		return f"{self.profession} {self.level}"


class LevelSkill(models.Model):
	level_id = models.ForeignKey(
		Level,
		on_delete=models.CASCADE,
		related_name="level_skill",
		verbose_name=_("Уровень"),
	)
	skill_id = models.ManyToManyField(
		Skill,
		related_name="level_skill",
		verbose_name=_("Уровень"),
	)

	class Meta:
		ordering = ["level_id"]
		verbose_name = _("Навык профессии")
		verbose_name_plural = _("Навыки профессии")

	def __str__(self):
		return f"{self.level_id} {self.skill_id}"


class Theme(BaseProduct):
	class Meta:
		ordering = ["title"]
		verbose_name = _("Темы")
		verbose_name_plural = _("Темы")


class Modul(BaseProduct):
	length = models.IntegerField(
		verbose_name=_("Время обучения в часах"),
	)
	theme_id = models.ManyToManyField(
		Theme,
		related_name="modul",
		verbose_name=_("Темы"),
	)

	class Meta:
		ordering = ["title"]
		verbose_name = _("Модуль")
		verbose_name_plural = _("Модули")


class Course(BaseProduct):
	description = models.TextField(
		verbose_name=_("Описание"),
	)
	modul_id = models.ManyToManyField(
		Modul,
		related_name="course",
		verbose_name=_("Модуль"),
	)
	level_id = models.ForeignKey(
		Level,
		on_delete=models.CASCADE,
		related_name="course",
		verbose_name=_("Уровень"),
	)

	class Meta:
		ordering = ["title"]
		verbose_name = _("Курс")
		verbose_name_plural = _("Курсы")


class Pract(SecondProduct):
	level_id = models.ForeignKey(
		Level,
		on_delete=models.CASCADE,
		related_name="pract",
		verbose_name=_("Уровень"),
	)

	class Meta:
		ordering = ["title"]
		verbose_name = _("Практика")
		verbose_name_plural = _("Практики")


class Links(SecondProduct):
	level_id = models.ForeignKey(
		Level,
		on_delete=models.CASCADE,
		related_name="pub",
		verbose_name=_("Уровень"),
	)

	class Meta:
		ordering = ["title"]
		verbose_name = _("Статья")
		verbose_name_plural = _("Статьи")


class UserLevel(models.Model):
	user_id = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name="user_level",
		verbose_name=_("Пользователь"),
	)
	level_id = models.ForeignKey(
		Level,
		on_delete=models.CASCADE,
		related_name="user_level",
		verbose_name=_("Уровень профессии"),
	)
	skill_id = models.ManyToManyField(
		Skill,
		related_name="user_level",
		verbose_name=_("Навык"),
	)
	goal = models.BooleanField(verbose_name=_("Цель"), default=False)

	class Meta:
		ordering = ["user_id"]
		verbose_name = _("Направление пользователя")
		verbose_name_plural = _("Направления пользователя")

	def __str__(self):
		return f"{self.user_id} {self.level_id}"


class UserCourse(models.Model):
	user_id = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name="user_course",
		verbose_name=_("Пользователь"),
	)
	сourse_id = models.ManyToManyField(
		Course,
		related_name="user_course",
		verbose_name=_("Курсы"),
	)
	pract_id = models.ManyToManyField(
		Pract,
		related_name="user_course",
		verbose_name=_("Практика"),
	)
	links_id = models.ManyToManyField(
		Links,
		related_name="user_course",
		verbose_name=_("Ссылки"),
	)

	class Meta:
		ordering = ["id"]
		verbose_name = _("Рекомендация")
		verbose_name_plural = _("Рекомендации")

	def __str__(self):
		return f"{self.user_id} рекомендуются {self.сourse_id}," f"{self.pract_id}, {self.links_id}"
