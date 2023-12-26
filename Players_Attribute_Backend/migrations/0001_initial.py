# Generated by Django 5.0 on 2023-12-20 16:57

import Players_Attribute_Backend.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(0, 'Afghanistan'), (1, 'Aland Islands'), (2, 'Albania'), (3, 'Algeria'), (4, 'American Samoa'), (5, 'Andorra'), (6, 'Angola'), (7, 'Anguilla'), (8, 'Antarctica'), (9, 'Antigua and Barbuda'), (10, 'Argentina'), (11, 'Armenia'), (12, 'Aruba'), (13, 'Australia'), (14, 'Austria'), (15, 'Azerbaijan'), (16, 'Bahamas'), (17, 'Bahrain'), (18, 'Bangladesh'), (19, 'Barbados'), (20, 'Belarus'), (21, 'Belgium'), (22, 'Belize'), (23, 'Benin'), (24, 'Bermuda'), (25, 'Bhutan'), (26, 'Bolivia'), (27, 'Bonaire, Sint Eustatius and Saba'), (28, 'Bosnia and Herzegovina'), (29, 'Botswana'), (30, 'Bouvet Island'), (31, 'Brazil'), (32, 'British Indian Ocean Territory'), (33, 'Brunei Darussalam'), (34, 'Bulgaria'), (35, 'Burkina Faso'), (36, 'Burundi'), (37, 'Cabo Verde'), (38, 'Cambodia'), (39, 'Cameroon'), (40, 'Canada'), (41, 'Cayman Islands'), (42, 'Central African Republic'), (43, 'Chad'), (44, 'Chile'), (45, 'China'), (46, 'Christmas Island'), (47, 'Cocos Islands'), (48, 'Colombia'), (49, 'Comoros'), (50, 'Democratic Republic of the Congo'), (51, 'Republic of the Congo'), (52, 'Cook Islands'), (53, 'Costa Rica'), (54, 'Croatia'), (55, 'Cuba'), (56, 'Curaçao'), (57, 'Cyprus'), (58, 'Czech Republic'), (59, "Côte d'Ivoire"), (60, 'Denmark'), (61, 'Djibouti'), (62, 'Dominica'), (63, 'Dominican Republic'), (64, 'Ecuador'), (65, 'Egypt'), (66, 'El Salvador'), (67, 'Equatorial Guinea'), (68, 'Eritrea'), (69, 'Estonia'), (70, 'Eswatini'), (71, 'Ethiopia'), (72, 'Falkland Islands'), (73, 'Faroe Islands'), (74, 'Fiji'), (75, 'Finland'), (76, 'France'), (77, 'French Guiana'), (78, 'French Polynesia'), (79, 'French Southern Territories'), (80, 'Gabon'), (81, 'Gambia'), (82, 'Georgia'), (83, 'Germany'), (84, 'Ghana'), (85, 'Gibraltar'), (86, 'Greece'), (87, 'Greenland'), (88, 'Grenada'), (89, 'Guadeloupe'), (90, 'Guam'), (91, 'Guatemala'), (92, 'Guernsey'), (93, 'Guinea'), (94, 'Guinea-Bissau'), (95, 'Guyana'), (96, 'Haiti'), (97, 'Heard Island and McDonald Islands'), (98, 'Holy See'), (99, 'Honduras'), (100, 'Hong Kong'), (101, 'Hungary'), (102, 'Iceland'), (103, 'India'), (104, 'Indonesia'), (105, 'Iran'), (106, 'Iraq'), (107, 'Ireland'), (108, 'Isle of Man'), (109, 'Israel'), (110, 'Italy'), (111, 'Jamaica'), (112, 'Japan'), (113, 'Jersey'), (114, 'Jordan'), (115, 'Kazakhstan'), (116, 'Kenya'), (117, 'Kiribati'), (118, "The Democratic People's Republic of Korea"), (119, 'The Republic of Korea'), (120, 'Kuwait'), (121, 'Kyrgyzstan'), (122, "Lao People's Democratic Republic"), (123, 'Latvia'), (124, 'Lebanon'), (125, 'Lesotho'), (126, 'Liberia'), (127, 'Libya'), (128, 'Liechtenstein'), (129, 'Lithuania'), (130, 'Luxembourg'), (131, 'Macao'), (132, 'Madagascar'), (133, 'Malawi'), (134, 'Malaysia'), (135, 'Maldives'), (136, 'Mali'), (137, 'Malta'), (138, 'Marshall Islands'), (139, 'Martinique'), (140, 'Mauritania'), (141, 'Mauritius'), (142, 'Mayotte'), (143, 'Mexico'), (144, 'Federated States of Micronesia'), (145, 'The Republic of Moldova'), (146, 'Monaco'), (147, 'Mongolia'), (148, 'Montenegro'), (149, 'Montserrat'), (150, 'Morocco'), (151, 'Mozambique'), (152, 'Myanmar'), (153, 'Namibia'), (154, 'Nauru'), (155, 'Nepal'), (156, 'Netherlands'), (157, 'New Caledonia'), (158, 'New Zealand'), (159, 'Nicaragua'), (160, 'Niger (the)'), (161, 'Nigeria'), (162, 'Niue'), (163, 'Norfolk Island'), (164, 'Northern Mariana Islands'), (165, 'Norway'), (166, 'Oman'), (167, 'Pakistan'), (168, 'Palau'), (169, 'Palestine'), (170, 'Panama'), (171, 'Papua New Guinea'), (172, 'Paraguay'), (173, 'Peru'), (174, 'Philippines'), (175, 'Pitcairn'), (176, 'Poland'), (177, 'Portugal'), (178, 'Puerto Rico'), (179, 'Qatar'), (180, 'Republic of North Macedonia'), (181, 'Romania'), (182, 'Russian Federation'), (183, 'Rwanda'), (184, 'Réunion'), (185, 'Saint Barthélemy'), (186, 'Saint Helena, Ascension and Tristan da Cunha'), (187, 'Saint Kitts and Nevis'), (188, 'Saint Lucia'), (189, 'Saint Martin (French part)'), (190, 'Saint Pierre and Miquelon'), (191, 'Saint Vincent and the Grenadines'), (192, 'Samoa'), (193, 'San Marino'), (194, 'Sao Tome and Principe'), (195, 'Saudi Arabia'), (196, 'Senegal'), (197, 'Serbia'), (198, 'Seychelles'), (199, 'Sierra Leone'), (200, 'Singapore'), (201, 'Sint Maarten'), (202, 'Slovakia'), (203, 'Slovenia'), (204, 'Solomon Islands'), (205, 'Somalia'), (206, 'South Africa'), (207, 'South Georgia and the South Sandwich Islands'), (208, 'South Sudan'), (209, 'Spain'), (210, 'Sri Lanka'), (211, 'Sudan'), (212, 'Suriname'), (213, 'Svalbard and Jan Mayen'), (214, 'Sweden'), (215, 'Switzerland'), (216, 'Syrian Arab Republic'), (217, 'Taiwan (Province of China)'), (218, 'Tajikistan'), (219, 'United Republic of Tanzania'), (220, 'Thailand'), (221, 'Timor-Leste'), (222, 'Togo'), (223, 'Tokelau'), (224, 'Tonga'), (225, 'Trinidad and Tobago'), (226, 'Tunisia'), (227, 'Turkey'), (228, 'Turkmenistan'), (229, 'Turks and Caicos Islands'), (230, 'Tuvalu'), (231, 'Uganda'), (232, 'Ukraine'), (233, 'United Arab Emirates'), (234, 'United Kingdom of Great Britain and Northern Ireland'), (235, 'United States Minor Outlying Islands'), (236, 'United States of America'), (237, 'Uruguay'), (238, 'Uzbekistan'), (239, 'Vanuatu'), (240, 'Venezuela'), (241, 'Viet Nam'), (242, 'Virgin Islands (British)'), (243, 'Virgin Islands (U.S.)'), (244, 'Wales'), (245, 'Wallis and Futuna'), (246, 'Western Sahara'), (247, 'Yemen'), (248, 'Zambia'), (249, 'Zimbabwe')], default=0)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('national_position', models.IntegerField(choices=[(0, ''), (1, 'RCB'), (2, 'LAM'), (3, 'LF'), (4, 'CB'), (5, 'LW'), (6, 'RCM'), (7, 'LS'), (8, 'RW'), (9, 'LCB'), (10, 'CAM'), (11, 'ST'), (12, 'LCM'), (13, 'GK'), (14, 'RM'), (15, 'LDM'), (16, 'LM'), (17, 'RS'), (18, 'CDM'), (19, 'LB'), (20, 'Sub')], default=0)),
                ('national_kit', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('club_position', models.IntegerField(choices=[(0, 'RM'), (1, 'RW'), (2, 'LCB'), (3, 'RS'), (4, 'CDM'), (5, 'CAM'), (6, 'RCB'), (7, 'ST'), (8, 'LB'), (9, 'Sub'), (10, 'LCM'), (11, 'RB'), (12, 'GK'), (13, 'LW'), (14, 'LDM'), (15, 'RCM'), (16, 'RDM'), (17, 'LM')], default=0)),
                ('club_kit', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('club_joining', models.DateTimeField()),
                ('contract_expiry', models.DateTimeField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('height', models.IntegerField(help_text="Set player's height in cm", validators=[django.core.validators.MinValueValidator(120), django.core.validators.MaxValueValidator(300)])),
                ('weight', models.IntegerField(help_text="Set player's weight in kg", validators=[django.core.validators.MinValueValidator(60), django.core.validators.MaxValueValidator(160)])),
                ('preferred_foot', models.IntegerField(choices=[(0, 'Right'), (1, 'Left')], default=0)),
                ('birth_date', models.DateTimeField()),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(50)])),
                ('preferred_position', models.CharField(max_length=20, validators=[Players_Attribute_Backend.models.validate_positions])),
                ('work_rate', models.CharField(max_length=20, validators=[Players_Attribute_Backend.models.validate_work])),
                ('weak_foot', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('skill_moves', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Ball_Control', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('dribbling', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('marking', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('sliding_tackle', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('standing_tackle', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('aggression', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('reactions', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('attacking_position', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('interceptions', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('vision', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('composure', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('crossing', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('short_pass', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('long_pass', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('acceleration', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('speed', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('stamina', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('strength', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('balance', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('agility', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('heading', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('shot_power', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('finishing', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('long_shots', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('curve', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('freekick_accuracy', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('penalties', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('volleys', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('gk_positioning', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('gk_diving', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('gk_kicking', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('gk_handling', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('gk_reflexes', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('club', models.ManyToManyField(help_text='Select the club for player', related_name='players', to='Players_Attribute_Backend.club')),
                ('nationality', models.ManyToManyField(help_text='Select the nationality for player', related_name='players', to='Players_Attribute_Backend.country')),
            ],
        ),
    ]