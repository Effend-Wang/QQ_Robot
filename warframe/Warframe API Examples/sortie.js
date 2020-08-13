// Current Sortie Data
// Data about the missions for the current sortie
// https://api.warframestat.us/pc/sortie

// API示例
[
  {
    "id": "string",
    "activation": "2019-08-24T14:15:22Z",
    "expiry": "2019-08-24T14:15:22Z",
    "rewardPool": "string",
    "variants": [
      {
        "node": "string",
        "boss": "string",
        "missionType": "string",
        "planet": "string",
        "modifier": "string",
        "modifierDescription": "string"
      }
    ],
    "boss": "string",
    "faction": "string",
    "expired": true,
    "eta": "string"
  }
]

// 实际示例
{
	'id': '5f1da4fda92f3587dcbd9ac3', 
	'activation': '2020-07-26T16:00:00.000Z', 
	'startString': '-23h 57m 4s', 
	'expiry': '2020-07-27T16:00:00.000Z', 
	'active': True, 
	'rewardPool': 'Sortie Rewards', 
	'variants': [
		{
			'boss': 'Deprecated', 
			'planet': 'Deprecated', 
			'missionType': 'Defense', 
			'modifier': 'Environmental Hazard: Radiation Pockets', 
			'modifierDescription': 'Any damage received will impart radiation effects, and so will green clouds around the tileset.', 
			'node': 'Tycho (Lua)'
		}, 
		{
			'boss': 'Deprecated', 
			'planet': 'Deprecated', 
			'missionType': 'Sabotage', 
			'modifier': 'Eximus Stronghold', 
			'modifierDescription': 'Eximus units have a much higher spawn rate in this mission. Some of their auras stack.', 
			'node': 'Acheron (Pluto)'
		}, 
		{
			'boss': 'Deprecated', 
			'planet': 'Deprecated', 
			'missionType': 'Assassination', 
			'modifier': 'Enemy Elemental Enhancement: Corrosive', 
			'modifierDescription': 'Enemies deal increased Corrosive damage and also have increased Immunity to said damage type.', 
			'node': 'Iliad (Phobos)'
		}
	], 
	'boss': 'Nef Anyo', 
	'faction': 'Corpus', 
	'expired': False, 
	'eta': '2m 55s'
}