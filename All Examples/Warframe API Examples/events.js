// Listing of ongoing events
// Events, such as Fomorian Attacks are included here
// https://api.warframestat.us/pc/events

// API示例
[
  {
    "activation": "2020-07-25T00:38:36Z",
    "expiry": "2020-07-25T00:38:36Z",
    "maximumScore": 0,
    "currentScore": 0,
    "smallInterval": 0,
    "largeInterval": 0,
    "faction": "Orokin",
    "description": "string",
    "tooltip": "string",
    "node": "string",
    "concurrentNodes": [
      "string"
    ],
    "victimNode": "string",
    "scoreLocTag": "string",
    "rewards": [
      {
        "countedItems": [
          {
            "count": 0,
            "type": "string"
          }
        ],
        "thumbnail": "string",
        "color": 0,
        "credits": 0,
        "asString": "string",
        "items": [
          {}
        ],
        "itemString": "string"
      }
    ],
    "expired": true,
    "health": 0,
    "affiliatedWith": "Arbiters of Hexis",
    "jobs": [
      {
        "activation": "2020-07-25T00:38:36Z",
        "expiry": "2020-07-25T00:38:36Z",
        "rewardPool": [
          "string"
        ],
        "type": "string",
        "enemyLevels": [
          0
        ],
        "standingStages": [
          0
        ],
        "minMR": 0
      }
    ],
    "interimSteps": [
      {
        "goal": 0,
        "reward": {
          "countedItems": [
            {
              "count": 0,
              "type": "string"
            }
          ],
          "thumbnail": "string",
          "color": 0,
          "credits": 0,
          "asString": "string",
          "items": [
            {}
          ],
          "itemString": "string"
        },
        "message": {
          "sender": "string",
          "subject": "string",
          "message": "string",
          "senderIcon": "string",
          "attachments": [
            "string"
          ]
        },
        "winnerCount": 0
      }
    ],
    "progressSteps": {
      "type": "string",
      "progressAmt": 0
    },
    "progressTotal": 0,
    "showTotalAtEndOfMission": true,
    "isPersonal": true,
    "isCommunity": true,
    "regionDrops": [
      "string"
    ],
    "archwingDrops": [
      "string"
    ],
    "asString": "string",
    "metadata": {},
    "completionBonuses": [
      0
    ],
    "scoreVar": "string",
    "altExpiry": "2020-07-25T00:38:36Z",
    "altActivation": "2020-07-25T00:38:36Z",
    "nextAlt": {
      "expiry": "2020-07-25T00:38:36Z",
      "activation": "2020-07-25T00:38:36Z"
    }
  }
]


// 实际示例
[
	{
		'id': '5c7cb0d00000000000000000', 
		'activation': '2020-07-24T16:00:00.000Z', 
		'startString': '-13h 48m 5s', 
		'expiry': '2020-08-07T16:00:00.000Z', 
		'active': True, 
		'maximumScore': 100, 
		'currentScore': 2, 
		'smallInterval': None, 
		'largeInterval': None, 
		'description': 'Thermia Fractures', 
		'tooltip': 'Seal fractures across the Orb Vallis', 
		'node': 'Orb Vallis (Venus)', 
		'concurrentNodes': [], 
		'scoreLocTag': 'Heat Fissures Event Score', 
		'rewards': [
			{
				'items': ['Opticor Vandal'], 
				'countedItems': [], 
				'credits': 0, 
				'asString': 'Opticor Vandal', 
				'itemString': 'Opticor Vandal', 
				'thumbnail': 'https://i.imgur.com/kPQcg5B.png', 
				'color': 6052435
			}, 
			{
				'items': [], 
				'countedItems': [], 
				'credits': 0, 
				'asString': '', 
				'itemString': '', 
				'thumbnail': 'https://i.imgur.com/JCKyUXJ.png', 
				'color': 15844367
			}
		], 
		'expired': False, 
		'health': 2, 
		'interimSteps': [
			{
				'goal': 5, 
				'reward': {
					'items': ['Buried Debts Emblem'], 
					'countedItems': [], 
					'credits': 0, 
					'asString': 'Buried Debts Emblem', 
					'itemString': 'Buried Debts Emblem', 
					'thumbnail': '', 
					'color': 5198940
				}, 
				'message': {

				}
			}, 
			{
				'goal': 25, 
				'reward': {
					'items': ['Amalgam Shotgun Spazz', 'Amalgam Serration'], 
					'countedItems': [], 
					'credits': 0, 
					'asString': 'Amalgam Shotgun Spazz + Amalgam Serration', 
					'itemString': 'Amalgam Shotgun Spazz + Amalgam Serration', 
					'thumbnail': '', 
					'color': 5198940
				}, 
				'message': {

				}
			}, 
			{
				'goal': 50, 
				'reward': {
					'items': ['Amalgam Barrel Diffusion', 'Amalgam Organ Shatter'], 
					'countedItems': [], 
					'credits': 0, 
					'asString': 'Amalgam Barrel Diffusion + Amalgam Organ Shatter', 
					'itemString': 'Amalgam Barrel Diffusion + Amalgam Organ Shatter', 
					'thumbnail': '', 
					'color': 5198940
				}, 
				'message': {

				}
			}, 
			{
				'goal': 75, 
				'reward': {
					'items': ['Buried Debts Sigil'], 
					'countedItems': [], 
					'credits': 0, 
					'asString': 'Buried Debts Sigil', 
					'itemString': 'Buried Debts Sigil', 
					'thumbnail': '', 
					'color': 5198940
				}, 
				'message': {

				}
			}
		], 
		'progressSteps': [], 
		'isPersonal': True, 
		'regionDrops': [], 
		'archwingDrops': [], 
		'asString': 'Thermia Fractures : undefined\nHeat Fissures Event Score : 100\nRewards:\nOpticor Vandal\n\nBattle on Orb Vallis (Venus)\n2% Remaining', 
		'metadata': {}, 
		'completionBonuses': [], 
		'scoreVar': 'FissuresClosed', 
		'altExpiry': '1970-01-01T00:00:00.000Z', 
		'altActivation': '1970-01-01T00:00:00.000Z', 
		'nextAlt': {
			'expiry': '1970-01-01T00:00:00.000Z', 
			'activation': '1970-01-01T00:00:00.000Z'
		}
	}, 
	{
		'id': '5f0f1398087e8145448bf904', 
		'activation': '2020-07-15T15:00:00.000Z', 
		'startString': '-9d 14h 48m 5s', 
		'expiry': '2020-07-27T15:00:00.000Z', 
		'active': True, 
		'maximumScore': 100, 
		'currentScore': 0, 
		'smallInterval': None, 
		'largeInterval': None, 
		'faction': 'Corpus', 
		'description': 'Tactical Alert: Dog Days', 
		'node': 'Earth', 
		'concurrentNodes': ['Earth', 'Earth', 'Earth'], 
		'rewards': [
			{
				'items': [], 
				'countedItems': [], 
				'credits': 0, 
				'asString': '', 
				'itemString': '', 
				'thumbnail': 'https://i.imgur.com/JCKyUXJ.png', 
				'color': 15844367
			}, 
			{
				'items': ['Noggle Statue - Hydroid Reprise'], 
				'countedItems': [], 
				'credits': 50000, 
				'asString': 'Noggle Statue - Hydroid Reprise + 50000cr', 
				'itemString': 'Noggle Statue - Hydroid Reprise', 
				'thumbnail': '', 
				'color': 5198940
			}, 
			{
				'items': ['Orokin Reactor', 'Stratos Emblem'], 
				'countedItems': [], 
				'credits': 0, 
				'asString': 'Orokin Reactor + Stratos Emblem', 
				'itemString': 'Orokin Reactor + Stratos Emblem', 
				'thumbnail': 'https://i.imgur.com/6Hm1BEq.png', 
				'color': 14140285
			}
		], 
		'expired': False, 
		'interimSteps': [
			{
				'goal': 25, 
				'reward': {
					'items': ['Redeemer Abysso Skin'], 
					'countedItems': [], 
					'credits': 50000, 
					'asString': 'Redeemer Abysso Skin + 50000cr', 
					'itemString': 'Redeemer Abysso Skin', 
					'thumbnail': 'https://raw.githubusercontent.com/Warframe-Community-Developers/warframe-worldstate-parser/master/resources/weapon_skin_thumb.png', 
					'color': 5196851
				}, 
				'message': {

				}
			}, 
			{
				'goal': 50, 
				'reward': {
					'items': ["Hydroid's Relay Scene"], 
					'countedItems': [], 
					'credits': 50000, 
					'asString': "Hydroid's Relay Scene + 50000cr", 
					'itemString': "Hydroid's Relay Scene", 
					'thumbnail': '', 
					'color': 5198940
				}, 
				'message': {

				}
			}
		], 
		'progressSteps': [], 
		'isPersonal': True, 
		'regionDrops': [], 
		'archwingDrops': [], 
		'asString': 'Tactical Alert: Dog Days : Corpus\nRewards:\n\nNoggle Statue - Hydroid Reprise + 50000cr\nOrokin Reactor + Stratos Emblem\nBattle on Earth', 
		'metadata': {}, 
		'completionBonuses': [], 
		'scoreVar': 'Team1Score', 
		'altExpiry': '1970-01-01T00:00:00.000Z', 
		'altActivation': '1970-01-01T00:00:00.000Z', 
		'nextAlt': {
			'expiry': '1970-01-01T00:00:00.000Z', 
			'activation': '1970-01-01T00:00:00.000Z'
		}
	}
]