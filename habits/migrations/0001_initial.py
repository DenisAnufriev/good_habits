# Generated by Django 5.1.4 on 2024-12-11 23:51

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        help_text="Укажите место выполнения",
                        max_length=100,
                        verbose_name="Место выполнения",
                    ),
                ),
                (
                    "time",
                    models.TimeField(
                        help_text="Укажите время выполнения",
                        verbose_name="Время выполнения",
                    ),
                ),
                (
                    "action",
                    models.TextField(
                        help_text="Укажите действие", verbose_name="Действие"
                    ),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=False,
                        help_text="Введите приятную привычку",
                        verbose_name="Приятная привычка",
                    ),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        help_text="Введите время",
                        verbose_name="Время выполнения (в секундах)",
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=True, verbose_name="Публичная привычка"
                    ),
                ),
                (
                    "frequency_type",
                    models.CharField(
                        choices=[("DAILY", "Ежедневно"), ("WEEKLY", "По дням недели")],
                        default="DAILY",
                        max_length=10,
                        verbose_name="Тип периодичности",
                    ),
                ),
                (
                    "weekdays",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(
                            choices=[
                                (1, "Понедельник"),
                                (2, "Вторник"),
                                (3, "Среда"),
                                (4, "Четверг"),
                                (5, "Пятница"),
                                (6, "Суббота"),
                                (7, "Воскресенье"),
                            ]
                        ),
                        blank=True,
                        help_text="Если выбрано 'По дням недели', укажите дни выполнения",
                        null=True,
                        size=None,
                        verbose_name="Дни недели",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        help_text="Укажите вознаграждение",
                        max_length=255,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"is_pleasant": True},
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
                "ordering": ("id",),
            },
        ),
    ]
