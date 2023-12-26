"""
Script to explore data in soccer_small.json
Goal1: Establish models required for project and field data type and validation method
Goal2: infer what data is fixed / common for all players, to determine which information can be hard-coded as a list
or dictionary and are stored in fixed_data.py module.
"""

import json
from datetime import datetime
from fixed_data import FixedData

F_DATA = FixedData()

# read soccer_small.json
with open('Players_Attribute_Backend/data/soccer_small.json') as f:
    data = json.load(f)

print("Number of players: ", len(data))
# 55

# ----------------------------------------------------------------------------------------------------------------------
# # ALL ATTRIBUTES
# first_input = data[0]
# attributes = list(first_input.keys())
# print(attributes)
# # ['Name', 'Nationality', 'National_Position', 'National_Kit', 'Club', 'Club_Position', 'Club_Kit', 'Club_Joining', 'Contract_Expiry', 'Rating', 'Height', 'Weight', 'Preffered_Foot', 'Birth_Date', 'Age', 'Preffered_Position', 'Work_Rate', 'Weak_foot', 'Skill_Moves', 'Ball_Control', 'Dribbling', 'Marking', 'Sliding_Tackle', 'Standing_Tackle', 'Aggression', 'Reactions', 'Attacking_Position', 'Interceptions', 'Vision', 'Composure', 'Crossing', 'Short_Pass', 'Long_Pass', 'Acceleration', 'Speed', 'Stamina', 'Strength', 'Balance', 'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'Freekick_Accuracy', 'Penalties', 'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Kicking', 'GK_Handling', 'GK_Reflexes']
# # TODO: save attributes in fixed_data as attributes ... DONE
# ----------------------------------------------------------------------------------------------------------------------
# # COUNTRIES
# # There are fixed number of countries so list of countries should be hard coded
# # get countries names from data
# countries = [item['Nationality'] for item in data]
#
# # make sure the countries in data are included in FixedData.country_list
#
# country_included = [item in FixedData.country_list for item in countries]
# print('All countries are included: ', len(country_included) == sum(country_included))
# country_excluded = [country for country, checked in zip(countries, country_included) if checked == False]
# print('Countries not included are : ', country_excluded)

# # TODO: when populating db: use list of countries stored in fixed_data as data_country_list ... DONE
# ----------------------------------------------------------------------------------------------------------------------
# # NATIONAL POSITION & CLUB POSITION
# # Game positions should be limited, check if there is a difference between national and club positions
# # and create list of positions

# national_position = [item['National_Position'] for item in data]
# uniq_position = list(set(national_position))
# print('National positions are: ', uniq_position)
# club_position = [item['Club_Position'] for item in data]
# uniq_position_club = list(set(club_position))
# print('Club positions are: ', uniq_position_club)
# print('National and club position are the same: ', uniq_position == uniq_position_club)
# # TODO: two lists are different so both are saved separately as club_lista and nat_positions ... DONE
# ----------------------------------------------------------------------------------------------------------------------
# # CLUBS
# # Doesn't make sense to limit the number of clubs included in code because they can change over time
# # TODO: allow user to create clubs
# clubs = list(set([item['Club'] for item in data]))
# print(clubs)
# # TODO: when populating db: use a fixed list of clubs from data stored in fixed_data as club_list ... DONE

# ----------------------------------------------------------------------------------------------------------------------
# # NATIONAL_KIT & CLUB KIT
# # The kit is the whole uniform a soccer team wears from the jersey to the shorts down to the socks.
# # It is the number on the uniform associated with each player.
# club_kit = [item['Club_Kit'] for item in data]
# print(club_kit)
# # Numbers go from 1 to 33 for club kit.

# #nat_kit = [item['National_Kit'] for item in data]
# #print(nat_kit)
# # Numbers go from 1 to 21 and there are None values for national kits

# # Wikipedia:  Players may now wear any number (as long as it is unique within their squad) between 1 and 99.
# # TODO: In Players model set these two fields as integers and set min=1 and max= 99 ... DONE
# ----------------------------------------------------------------------------------------------------------------------
# # CLUB JOINING & CONTRACT_EXPIRY & BIRTH_DATE
# # This attributes are dates.
# # TODO: So when populating db, this attribute should be converted to date format with the following method ... DONE
# date = datetime.strptime(data[0]['Club_Joining'], "%m/%d/%Y")
# print(data[0]['Club_Joining'])
# print(date)
# date = datetime.strptime(str(data[0]['Contract_Expiry']), "%Y")
# print(data[0]['Contract_Expiry'])
# print(date)
# date = datetime.strptime(data[0]['Birth_Date'], "%m/%d/%Y")
# print(data[0]['Club_Joining'])
# print(date)
# ----------------------------------------------------------------------------------------------------------------------
# # RATING
# ratings = [item['Rating'] for item in data]
# print(ratings)
# integer range from 86-94
# # TODO: In Players model set these field type min=1, max=100 ...DONE
# ----------------------------------------------------------------------------------------------------------------------
# # HEIGHT
# height = [item['Height'] for item in data]
# print(height)
# # unit is always cm.
# # TODO: So when populating db, this attribute should be converted to integer format with the following method DONE
# height_values = [int(item.split('cm')[0]) for item in height]
# print(height_values)
# ----------------------------------------------------------------------------------------------------------------------
# # WEIGHT
# weight = [item['Weight'] for item in data]
# print(weight)
# # unit is always kg.
# # TODO: So when populating db, this attribute should be converted to integer format with the following method DONE
# weight_values = [int(item.split('kg')[0]) for item in weight]
# print(weight_values)

# ----------------------------------------------------------------------------------------------------------------------
# # PREFERRED FOOT
# weight = [item['Preffered_Foot'] for item in data]
# print(list(set(weight)))
# # There is a typo in attribute name. This attribute value is either Right or Left.
# # TODO: create list preferred_foot in fixed_data ...DONE

# ----------------------------------------------------------------------------------------------------------------------
# # AGE
# age = [item['Age'] for item in data]
# print(age)
# # integers from 24-39 (in model I will set the range from 15-50)
# # TODO: In Players model set this field type to integer,  min=15, max=50 ...DONE
# ----------------------------------------------------------------------------------------------------------------------
# # PREFFERED_POSITION
# preferred_position = [item['Preffered_Position'] for item in data]
# print(preferred_position)
# # method to check if each item is a combination of national and club positions.
# # this method will be used as validator for model
# club_positions = [item[1] for item in CLUB_POSITIONS]
# nat_positions = [item[1] for item in NATIONAL_POSITIONS]
# all_positions = club_positions + nat_positions
# first_input = preferred_position[0]
# combinations = first_input.split('/')
# check_if_present = [item in all_positions for item in combinations]
# print(check_if_present)
# # TODO: In Players model, field type string, create a validation method for this field ...DONE
# ----------------------------------------------------------------------------------------------------------------------
# # WORK_RATE
# work_rate = [item['Work_Rate'] for item in data]
# # print(work_rate)
# # is a combination of High Medium and Low
# first_input = work_rate[0]
# combinations = first_input.split('/')
# print(combinations)
# clean_combination = [item.strip() for item in combinations]
# print(clean_combination)
# # TODO: In Players model, field type string, create a validation method for this field ...DONE
# ----------------------------------------------------------------------------------------------------------------------
# # WEAK_FOOT & SKILL_MOVES
# weak_foot = [item['Weak_foot'] for item in data]
# print(weak_foot)
# # star rating system for weak foot. Integers go from 1-5
# # TODO: In Players model set this field type to integer,  min=1, max=5 ...DONE
# ----------------------------------------------------------------------------------------------------------------------
# # BALL_CONTROL THROUGH GK_REFLEXES
# ball_control = [item['GK_Reflexes'] for item in data]
# print(ball_control)
# # These fields' values are integers go from 1-100
# # TODO: In Players model set this field type to integer,  min=1, max=100 ...DONE
