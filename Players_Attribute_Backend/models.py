"""
Models created for Players_Attribute_Backend project.
"""

from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .data import fixed_data as fd
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.template.defaultfilters import slugify


F_DATA = fd.FixedData()
class Country(models.Model):
    """Country model the players belong to"""
    name = models.CharField(max_length=200, choices=F_DATA.country_list, default="None")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns list of countries"""
        return reverse('countries_list')


class Club(models.Model):
    """Club model the players belong to"""
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns list of clubs"""
        return reverse('club_list')

def validate_positions(value:str) -> None:
    """This function checks if "Preffered_Position" is a combination of valid positions"""
    club_positions = [item[1] for item in F_DATA.club_positions]
    nat_positions = [item[1] for item in F_DATA.national_positions]
    all_positions = club_positions + nat_positions
    combinations = value.split('/')
    check_if_present = [item.strip() in all_positions for item in combinations]
    if len(check_if_present) != sum(check_if_present):
        raise ValidationError(
            _('%(value) should be a combination of valid positions separated by /')
        )


def validate_work(value:str) -> None:
    """ This function checks if "work_rate" is a combination of valid levels """
    levels = ['High', 'Medium', 'Low']
    combinations = value.split('/')
    check_if_present = [item.strip() in levels for item in combinations]
    if len(check_if_present) != sum(check_if_present):
        raise ValidationError(
            _('%(value) should be a combination of valid work levels (High, Medium, Low) separated by /')
        )


class Player(models.Model):
    """Player model the players belong to"""
    Name = models.CharField(max_length=200)
    slug = models.SlugField()
    Nationality = models.ManyToManyField(Country, help_text='Select the nationality for player', related_name='players')
    National_Position = models.CharField(max_length=20, choices=F_DATA.national_positions, default=None)
    National_Kit = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(99)])
    Club = models.ManyToManyField(Club, help_text='Select the club for player', related_name='players')
    Club_Position = models.CharField(max_length=20, choices=F_DATA.club_positions, default=None)
    Club_Kit = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(99)])
    Club_Joining = models.DateTimeField(auto_now_add=False)
    Contract_Expiry = models.DateTimeField(auto_now_add=False)
    Rating = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Height = models.IntegerField(null=False,
                                 help_text="Set player's height in cm",
                                 validators=[MinValueValidator(120), MaxValueValidator(300)])
    Weight = models.IntegerField(null=False,
                                     help_text="Set player's weight in kg",
                                     validators=[MinValueValidator(60), MaxValueValidator(160)])
    Preffered_Foot = models.CharField(max_length=20, choices=F_DATA.preferred_foot, default=None)
    Birth_Date = models.DateTimeField(auto_now_add=False)
    Age = models.IntegerField(null=False, validators=[MinValueValidator(15), MaxValueValidator(50)])
    Preffered_Position = models.CharField(max_length=20, validators=[validate_positions])
    Work_Rate = models.CharField(max_length=20, validators=[validate_work])
    Weak_foot = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    Skill_Moves = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    Ball_Control = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Dribbling = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Marking = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Sliding_Tackle = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Standing_Tackle = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Aggression = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Reactions = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Attacking_Position = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Interceptions = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Vision = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Composure = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Crossing = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Short_Pass = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Long_Pass = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Acceleration = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Speed = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Stamina = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Strength = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Balance = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Agility = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Jumping = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Heading = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Shot_Power = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Finishing = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Long_Shots = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Curve = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Freekick_Accuracy = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Penalties = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Volleys = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    GK_Positioning = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    GK_Diving = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    GK_Kicking = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    GK_Handling = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    GK_Reflexes = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])

    class Meta:
        ordering = ['Name']

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Name)
        super(Player, self).save(*args, **kwargs)
