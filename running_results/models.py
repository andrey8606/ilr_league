from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

DISTANCES = [(1000, '1000'),
             (5000, '5000')]
GENDERS = [
    ('М', 'М'),
    ('Ж', 'Ж')
]
YEARS = [
    (2025, 2025),
    (2024, 2024),
    (2023, 2023),
    (2022, 2022),
    (2021, 2021),
    (2020, 2020),
    (2019, 2019),
    (2018, 2018),
    (2017, 2017),
    (2016, 2016),
]


class Result(models.Model):
    overall_place = models.IntegerField()
    place_in_group = models.IntegerField()
    name = models.CharField(max_length=200,
                            blank=False, null=False)
    distance = models.CharField(choices=DISTANCES,
                                default=1000, max_length=20)
    result = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=150, blank=False,
                            null=False)
    gender = models.CharField(choices=GENDERS, max_length=20)
    rank = models.CharField(default='none',
                            max_length=10)
    year = models.IntegerField(choices=YEARS)

    best_time = models.CharField(max_length=10)
    jan_result = models.CharField(max_length=10)
    feb_result = models.CharField(max_length=10)
    mar_result = models.CharField(max_length=10)
    apr_result = models.CharField(max_length=10)
    may_result = models.CharField(max_length=10)
    jun_result = models.CharField(max_length=10)
    jul_result = models.CharField(max_length=10)
    aug_result = models.CharField(max_length=10)
    sep_result = models.CharField(max_length=10)
    oct_result = models.CharField(max_length=10)
    nov_result = models.CharField(max_length=10)
    dec_result = models.CharField(max_length=10)

    jan_progress = models.IntegerField()
    feb_progress = models.IntegerField()
    mar_progress = models.IntegerField()
    apr_progress = models.IntegerField()
    may_progress = models.IntegerField()
    jun_progress = models.IntegerField()
    jul_progress = models.IntegerField()
    aug_progress = models.IntegerField()
    sep_progress = models.IntegerField()
    oct_progress = models.IntegerField()
    nov_progress = models.IntegerField()
    dec_progress = models.IntegerField()

    class Meta:
        ordering = ['overall_place', 'place_in_group']
        models.UniqueConstraint(fields=['name', 'year'],
                                name='unique_result')

    def __str__(self):
        return self.year + '-' + self.name
