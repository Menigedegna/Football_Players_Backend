"""
Command created to populate tables Players_Attribute_Backend project database .
"""

from django.core.management.base import BaseCommand
from Players_Attribute_Backend.models import Club, Country, Player
from Players_Attribute_Backend.data.fixed_data import FixedData
import json
from datetime import datetime

F_DATA = FixedData()


def clear_table(table):
    """Remove all items in a table"""
    table.objects.all().delete()


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def create_player(self, player: dict) -> None:
        """Create a player object in Player table with a dictionary"""
        country = player["Nationality"]
        # remove Nationality field
        del player["Nationality"]
        # save club of player
        club = player["Club"]
        # remove Club field
        del player["Club"]
        # format few fields to date format
        player["Club_Joining"] = datetime.strptime(player["Club_Joining"], "%m/%d/%Y")
        player['Contract_Expiry'] = datetime.strptime(str(player['Contract_Expiry']), "%Y")
        player['Birth_Date'] = datetime.strptime(player['Birth_Date'], "%m/%d/%Y")
        # format height field to integer
        player["Height"] = int(player["Height"].split('cm')[0])
        # format weight field to integer
        player["Weight"] = int(player["Weight"].split('kg')[0])
        # create players
        new_player = Player(**player)
        new_player.save()
        # search for country of player in Country table
        country_object = Country.objects.filter(name=country)
        # associate club and country objects to player object and save object
        new_player.Nationality.add(*country_object)
        # search for club of player in Club table
        club_object = Club.objects.filter(name=club)
        # associate club objects to player object
        new_player.Club.add(*club_object)
        # save player object
        new_player.save()
        message = "Player added to database: " + player["Name"]
        self.stdout.write(self.style.SUCCESS(message))



    def handle(self, *args, **options):
        """Populate database with data/soccer_small.json """

        # Code to populate Country table
        list_countries = F_DATA.data_country_list
        for country in list_countries:
            Country.objects.create(name=country)
        self.stdout.write(self.style.SUCCESS('Country table populated successfully'))

        # Code to populate Club table
        list_clubs = F_DATA.club_list
        for club in list_clubs:
            Club.objects.create(name=club)
        self.stdout.write(self.style.SUCCESS('Club table populated successfully'))

        # clear_table(Player)
        # Code to populate Players table
        with open('Players_Attribute_Backend/data/soccer_small.json') as f:
            data = json.load(f)

        # for each player in data:
        for item in data:
            self.create_player(item)
        self.stdout.write(self.style.SUCCESS('Player table populated successfully'))

