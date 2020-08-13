// Get the current Void Trader Information
// Information on the current Void Trader offerings, or when he will arrive.
// https://api.warframestat.us/pc/voidTrader

// API示例
{
  "id": "string",
  "activation": "2019-08-24T14:15:22Z",
  "expiry": "2019-08-24T14:15:22Z",
  "character": "string",
  "location": "string",
  "inventory": [
    {
      "item": "string",
      "ducats": 0,
      "credits": 0
    }
  ],
  "psId": "string",
  "active": true,
  "startString": "string",
  "endString": "string"
}

// 实际示例
{
	'id': '5d1e07a0a38e4a4fdd7cefca', 
	'activation': '2020-07-31T13:00:00.000Z', 
	'startString': '3d 1m 3s', 
	'expiry': '2020-08-02T13:00:00.000Z', 
	'active': False, 
	'character': "Baro Ki'Teer", 
	'location': 'Strata Relay (Earth)', 
	'inventory': [], 
	'psId': '5d1e07a0a38e4a4fdd7cefca0', 
	'endString': '5d 1m 3s'
}