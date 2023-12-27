# API Documentation
## Base URL

```

https://mariamawit.pythonanywhere.com/api

```
## Authentication
Authentication is not required.

## Endpoints
### 1. Players

**URL**: '/'<br>
**Method**: GET<br>
**Description**: This endpoint returns list of players with all their attrbutes.<br>
**Parameters**: None<br>
**Example Request**:<br>

```

curl -X GET https://mariamawit.pythonanywhere.com/api/

```
**Response**:<br>
- HTTP Status Code: 200 OK
- Body:
  ```
  [
    {
        "Name": "Alexis Sánchez",
        "Nationality": [
            "Chile"
        ],
        "National_Position": "LW",
        "National_Kit": 7,
        "Club": [
            "Arsenal"
        ],
        "Club_Position": "ST",
        "Club_Kit": 7,
        "Club_Joining": "2014-07-10T00:00:00Z",
        "Contract_Expiry": "2018-01-01T00:00:00Z",
        "Rating": 88,
        "Height": 169,
        "Weight": 62,
        "Preffered_Foot": "Right",
        "Birth_Date": "1988-12-19T00:00:00Z",
        "Age": 28,
        "Preffered_Position": "ST/RM",
        "Work_Rate": "High / High",
        "Weak_foot": 3,
        "Skill_Moves": 4,
        "Ball_Control": 86,
        "Dribbling": 89,
        "Marking": 30,
        "Sliding_Tackle": 35,
        "Standing_Tackle": 39,
        "Aggression": 80,
        "Reactions": 87,
        "Attacking_Position": 86,
        "Interceptions": 42,
        "Vision": 82,
        "Composure": 82,
        "Crossing": 80,
        "Short_Pass": 80,
        "Long_Pass": 73,
        "Acceleration": 88,
        "Speed": 84,
        "Stamina": 85,
        "Strength": 72,
        "Balance": 87,
        "Agility": 90,
        "Jumping": 85,
        "Heading": 70,
        "Shot_Power": 84,
        "Finishing": 85,
        "Long_Shots": 81,
        "Curve": 78,
        "Freekick_Accuracy": 78,
        "Penalties": 77,
        "Volleys": 83,
        "GK_Positioning": 12,
        "GK_Diving": 10,
        "GK_Kicking": 15,
        "GK_Handling": 10,
        "GK_Reflexes": 13
    }, ...
  ]
  ```

### 2. Player's detail view

**URL**: '/players/{name}/'<br>
**Method**: GET<br>
**Description**: This endpoint returns requested player's attributes.<br>
**Parameters**: <br>
- name:<br>
  Type: **string**<br>
  Required: Yes<br>
  Description:<br>
  {name} should be lowercase in the following format: firstName-lastName<br>. Remove any special characters. The example code below returns the attributes for Alexis Sánchez.
**Example Request**:<br>

```

curl -X GET https://mariamawit.pythonanywhere.com/api/players/alexis-sanchez/

```
**Response**:<br>
- HTTP Status Code: 200 OK
- Body:
  ```
  [
    {
        "Name": "Alexis Sánchez",
        "Nationality": [
            "Chile"
        ],
        "National_Position": "LW",
        "National_Kit": 7,
        "Club": [
            "Arsenal"
        ],
        "Club_Position": "ST",
        "Club_Kit": 7,
        "Club_Joining": "2014-07-10T00:00:00Z",
        "Contract_Expiry": "2018-01-01T00:00:00Z",
        "Rating": 88,
        "Height": 169,
        "Weight": 62,
        "Preffered_Foot": "Right",
        "Birth_Date": "1988-12-19T00:00:00Z",
        "Age": 28,
        "Preffered_Position": "ST/RM",
        "Work_Rate": "High / High",
        "Weak_foot": 3,
        "Skill_Moves": 4,
        "Ball_Control": 86,
        "Dribbling": 89,
        "Marking": 30,
        "Sliding_Tackle": 35,
        "Standing_Tackle": 39,
        "Aggression": 80,
        "Reactions": 87,
        "Attacking_Position": 86,
        "Interceptions": 42,
        "Vision": 82,
        "Composure": 82,
        "Crossing": 80,
        "Short_Pass": 80,
        "Long_Pass": 73,
        "Acceleration": 88,
        "Speed": 84,
        "Stamina": 85,
        "Strength": 72,
        "Balance": 87,
        "Agility": 90,
        "Jumping": 85,
        "Heading": 70,
        "Shot_Power": 84,
        "Finishing": 85,
        "Long_Shots": 81,
        "Curve": 78,
        "Freekick_Accuracy": 78,
        "Penalties": 77,
        "Volleys": 83,
        "GK_Positioning": 12,
        "GK_Diving": 10,
        "GK_Kicking": 15,
        "GK_Handling": 10,
        "GK_Reflexes": 13
    }
  ]
  ```
  
**Error Handling**: <br>
If player is not found in our database
- **HTTP Status Code**: 404 Not Found
- **Body**
```

  {"error": "Player not found"}

```

### 3. Football clubs

**URL**: '/clubs/'<br>
**Method**: GET<br>
**Description**: This endpoint returns list of clubs with list of players.<br>
**Parameters**: None<br>
**Example Request**:<br>

```

curl -X GET https://mariamawit.pythonanywhere.com/api/clubs/

```
**Response**:<br>
- HTTP Status Code: 200 OK
- Body:
  ```
  [
    {
        "name": "Arsenal",
        "players": [
            "Alexis Sánchez",
            "Mesut Özil",
            "Petr Čech"
        ]
    }, ...
  ]

### 4. Countries

**URL**: '/countries/'<br>
**Method**: GET<br>
**Description**: This endpoint returns list of countries with list of players.<br>
**Parameters**: None<br>
**Example Request**:<br>

```

curl -X GET https://mariamawit.pythonanywhere.com/api/countries/

```
**Response**:<br>
- HTTP Status Code: 200 OK
- Body:
  ```
  [
    {
        "name": "Argentina",
        "players": [
            "Gonzalo Higuaín",
            "Lionel Messi",
            "Paulo Dybala",
            "Sergio Agüero",
            "Ángel Di María"
        ]
    }, ...
  ]
  ```
  
### 5. Attributes

**URL**: '/attributes/'<br>
**Method**: GET<br>
**Description**: This endpoint returns list of attributes.<br>
**Parameters**: None<br>
**Example Request**:<br>

```

curl -X GET https://mariamawit.pythonanywhere.com/api/attributes/

```
**Response**:<br>
- HTTP Status Code: 200 OK
- Body:
  ```
  [
    "Name",
    "Nationality",
    "National_Position",
    "National_Kit",
    "Club",
    "Club_Position",
    "Club_Kit",
    "Club_Joining",
    "Contract_Expiry",
    "Rating",
    "Height",
    "Weight",
    "Preffered_Foot",
    "Birth_Date",
    "Age",
    "Preffered_Position",
    "Work_Rate",
    "Weak_foot",
    "Skill_Moves",
    "Ball_Control",
    "Dribbling",
    "Marking",
    "Sliding_Tackle",
    "Standing_Tackle",
    "Aggression",
    "Reactions",
    "Attacking_Position",
    "Interceptions",
    "Vision",
    "Composure",
    "Crossing",
    "Short_Pass",
    "Long_Pass",
    "Acceleration",
    "Speed",
    "Stamina",
    "Strength",
    "Balance",
    "Agility",
    "Jumping",
    "Heading",
    "Shot_Power",
    "Finishing",
    "Long_Shots",
    "Curve",
    "Freekick_Accuracy",
    "Penalties",
    "Volleys",
    "GK_Positioning",
    "GK_Diving",
    "GK_Kicking",
    "GK_Handling",
    "GK_Reflexes"
  ]
  ```

**Error Responses**:
- **400 Bad Request**: The request is malformed or missing required parameters.
- **500 Internal Server Error**: An unexpected error occurred on the server.
- **404 Resource Not Found**: The resource you requested is not found.
