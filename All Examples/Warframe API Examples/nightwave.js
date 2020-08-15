// Get the current Nightwave state.
// The Current cycle and challenges of Nightwave, a battle-pass-esque rotation and challenge system
// https://api.warframestat.us/pc/nightwave

// API示例
{
  "id": "string",
  "activation": "2019-08-24T14:15:22Z",
  "expiry": "2019-08-24T14:15:22Z",
  "params": {},
  "rewardTypes": [
    "string"
  ],
  "season": 0,
  "tag": "string",
  "phase": 0,
  "possibleChallenges": [
    {
      "id": "string",
      "activation": "2019-08-24T14:15:22Z",
      "expiry": "2019-08-24T14:15:22Z",
      "isDaily": true,
      "isElite": true,
      "title": "string",
      "desc": "string",
      "reputation": 0
    }
  ],
  "activeChallenges": [
    {
      "id": "string",
      "activation": "2019-08-24T14:15:22Z",
      "expiry": "2019-08-24T14:15:22Z",
      "isDaily": true,
      "isElite": true,
      "title": "string",
      "desc": "string",
      "reputation": 0
    }
  ]
}

// 实际示例
{
	'id': 'nightwave1598832000000', 
	'activation': '2020-05-11T00:00:00.000Z', 
	'startString': '-77d 14h 17m 19s', 
	'expiry': '2020-08-31T00:00:00.000Z', 
	'active': True, 
	'season': 4, 
	'tag': 'Radio Legion3 Syndicate', 
	'phase': 2, 
	'params': {
		'ctc': 5
	}, 
	'possibleChallenges': [], 
	'activeChallenges': [
		{
			'id': '1595894400000seasondailyplayemote', 
			'activation': '2020-07-25T00:00:00.000Z', 
			'startString': '-2d 14h 17m 19s', 
			'expiry': '2020-07-28T00:00:00.000Z', 
			'active': True, 
			'isDaily': True, 
			'isElite': False, 
			'desc': 'Play 1 Emote', 
			'title': 'Expressive', 
			'reputation': 1000
		}, 
		{
			'id': '1595980800000seasondailykillenemieswithheadshots', 
			'activation': '2020-07-26T00:00:00.000Z', 
			'startString': '-1d 14h 17m 19s', 
			'expiry': '2020-07-29T00:00:00.000Z', 
			'active': True, 
			'isDaily': True, 
			'isElite': False, 
			'desc': 'Kill 40 Enemies with Headshots', 
			'title': 'Marksman', 
			'reputation': 1000
		}, 
		{
			'id': '1596067200000seasondailykillenemieswithmagnetic', 
			'activation': '2020-07-27T00:00:00.000Z', 
			'startString': '-14h 17m 19s', 
			'expiry': '2020-07-30T00:00:00.000Z', 
			'active': True, 
			'isDaily': True, 
			'isElite': False, 
			'desc': 'Kill 150 Enemies with Magnetic damage', 
			'title': 'Attractive', 
			'reputation': 1000
		}, 
		{
			'id': '1596412800000seasonweeklycatchrarevenusfish', 
			'activation': '2020-07-27T00:00:00.000Z', 
			'startString': '-14h 17m 19s', 
			'expiry': '2020-08-03T00:00:00.000Z', 
			'active': True, 
			'isElite': False, 
			'desc': 'Catch 6 Rare Servofish in the Orb Vallis', 
			'title': 'Venus Fisher', 
			'reputation': 4500
		}, 
		{
			'id': '1596412800000seasonweeklysanctuaryonslaught', 
			'activation': '2020-07-27T00:00:00.000Z', 
			'startString': '-14h 17m 19s', 
			'expiry': '2020-08-03T00:00:00.000Z', 
			'active': True, 
			'isElite': False, 
			'desc': 'Complete 8 waves of Sanctuary Onslaught', 
			'title': 'Test Subject', 
			'reputation': 4500
		}, 
		{
			'id': '1596412800000seasonweeklyunlockrelics', 
			'activation': '2020-07-27T00:00:00.000Z', 
			'startString': '-14h 17m 19s', 
			'expiry': '2020-08-03T00:00:00.000Z', 
			'active': True, 
			'isElite': False, 
			'desc': 'Unlock 3 Relics', 
			'title': 'Unlock Relics', 
			'reputation': 4500
		}, 
		{
			'id': '1596412800000seasonweeklycompletesortie', 
			'activation': '2020-07-27T00:00:00.000Z', 
			'startString': '-14h 17m 19s', 
			'expiry': '2020-08-03T00:00:00.000Z', 
			'active': True, 
			'isElite': False, 
			'desc': 'Complete 1 Sorties', 
			'title': 'Sortie Specialist', 
			'reputation': 4500
		}, 
		{
			'id': '1596412800000seasonweeklycompleterescue', 
			'activation': '2020-07-27T00:00:00.000Z', 
			'startString': '-14h 17m 19s', 
			'expiry': '2020-08-03T00:00:00.000Z', 
			'active': True, 
			'isElite': False, 
			'desc': 'Complete 3 Rescue missions', 
			'title': 'Rescuer', 
			'reputation': 4500
		}, 
		{
			'id': '1596412800000seasonweeklyhardrailjackmissions', 
			'activation': '2020-07-27T00:00:00.000Z', 
			'startString': '-14h 17m 19s', 
			'expiry': '2020-08-03T00:00:00.000Z', 
			'active': True, 
			'isElite': True, 
			'desc': 'Complete 8 Railjack Missions', 
			'title': 'Elite Explorer', 
			'reputation': 7000
		}, 
		{
			'id': '1596412800000seasonweeklyhardfriendsdefense', 
			'activation': '2020-07-27T00:00:00.000Z', 
			'startString': '-14h 17m 19s', 
			'expiry': '2020-08-03T00:00:00.000Z', 
			'active': True, 
			'isElite': True, 
			'desc': 'Complete a Defense mission reaching at least Wave 20', 
			'title': 'Defense', 
			'reputation': 7000
		}
	], 
	'rewardTypes': ['credits']
}