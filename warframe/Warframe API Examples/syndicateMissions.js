// Listing of Syndicate mission nodes
// Cycling through different nodes each day, these are a general listing of the nodes that each syndicate will use for the day.
// https://api.warframestat.us/pc/syndicateMissions

// API示例
[
  {
    "nodes": ["string"],
    "eta": "string",
    "jobs": [
      {
        "activation": "2020-07-25T00:38:36Z",
        "expiry": "2020-07-25T00:38:36Z",
        "rewardPool": ["string"],
        "type": "string",
        "enemyLevels": [0],
        "standingStages": [0],
        "minMR": 0
      }
    ],
    "syndicate": "Arbiters of Hexis",
    "id": "string",
    "expiry": "2020-07-25T00:38:36Z",
    "activation": "2020-07-25T00:38:36Z"
  }
]

// 实际示例
[
  {
    'id': '1595646185389CetusSyndicate', 
    'activation': '2020-07-25T00:33:06.515Z', 
    'startString': '-2h 28m 1s', 
    'expiry': '2020-07-25T03:03:05.389Z', 
    'active': True, 
    'syndicate': 'Ostrons', 
    'nodes': [], 
    'jobs': [
      {
        'id': 'AttritionBountyExt1595646185389', 
        'rewardPool': ['Redirection', '100X Oxium', '1,500 Credits Cache', '50 Endo', '15X Iradite', 'Gara Chassis BP', 'Point Blank', 'Streamline', '2X Morphics'], 
        'type': 'Cull the Enemy', 
        'enemyLevels': [5, 15], 
        'standingStages': [390, 390, 390], 
        'minMR': 0
      }, 
      {
        'id': 'RescueBountyResc1595646185389', 
        'rewardPool': ['Steel Fiber', '200X Oxium', '2,500 Credits Cache', '100 Endo', 'Gara Systems BP', 'Charged Chamber', 'Burning Wasp', 'Lith K4 Relic', '2X Control Module'], 
        'type': 'Search and Rescue', 
        'enemyLevels': [10, 30], 
        'standingStages': [650, 650, 650], 
        'minMR': 1
      }, 
      {
        'id': 'ReclamationBountyTheft1595646185389', 
        'rewardPool': ['Gladiator Aegis', 'Madurai Lens', 'Cetus Wisp', '200 Endo', 'Gara Neuroptics BP', 'Augur Accord', 'Revenant Systems BP', 'Meso D5 Relic', 'Vigilante Supplies'], 
        'type': 'Reclaim the Stolen Artifact', 
        'enemyLevels': [20, 40], 
        'standingStages': [650, 650, 650, 960], 
        'minMR': 2
      }, 
      {
        'id': 'AssassinateBountyCap1595646185389', 
        'rewardPool': ['Gladiator Rush', 'Unairu Lens', 'Madurai Lens', '300 Endo', 'Cetus Wisp', 'Augur Reach', 'Revenant Chassis BP', 'Neo N12 Relic', 'Vigilante Offense'], 
        'type': 'Capture the New Grineer Commander', 
        'enemyLevels': [30, 50], 
        'standingStages': [630, 630, 630, 630, 1230], 
        'minMR': 3
      }, 
      {
        'id': 'CaptureBountyCapTwo1595646185389', 
        'rewardPool': ['5X Breath Of The Eidolon', '400 Endo', '2X Cetus Wisp', '300X Kuva', 'Axi S7 Relic', 'Furax Wraith Left Gauntlet', 'Carving Mantis', 'Eidolon Lens BP', 'Revenant Neuroptics BP'], 
        'type': 'Spy Catcher',
        'enemyLevels': [40, 60], 
        'standingStages': [680, 680, 680, 680, 1340], 
        'minMR': 5
      }, 
      {
        'id': 'AttritionBountySab1595646185389', 
        'rewardPool': ['5X Breath Of The Eidolon', '400 Endo', '2X Cetus Wisp', '300X Kuva', 'Axi S7 Relic', 'Furax Wraith Left Gauntlet', 'Carving Mantis', 'Eidolon Lens BP', 'Revenant Neuroptics BP'], 
        'type': 'Sabotage the Enemy Supply Lines', 
        'enemyLevels': [100, 100], 
        'standingStages': [840, 840, 840, 840, 1660], 
        'minMR': 10
      }
    ], 
    'eta': '1m 57s'
  }, 
  {
    'id': '1595646185389SolarisSyndicate', 
    'activation': '2020-07-25T00:33:06.515Z', 
    'startString': '-2h 28m 1s', 
    'expiry': '2020-07-25T03:03:05.389Z', 
    'active': True, 
    'syndicate': 'Solaris United', 
    'nodes': [], 
    'jobs': [
      {
        'id': 'VenusChaosJobExcavation1595646185389', 
        'rewardPool': ['100X Oxium', '1,500 Credits Cache', '50 Endo', '5X Mytocardia Spore', '2X Training Debt-Bond', 'Garuda Chassis BP', '5X Tepa Nodule', '3,000 Credits Cache', 'Lith K4 Relic'], 
        'type': 'Bury Them', 
        'enemyLevels': [5, 15], 
        'standingStages': [480, 480, 480], 
        'minMR': 0
      }, 
      {
        'id': 'VenusIntelJobResource1595646185389', 
        'rewardPool': ['15X Mytocardia Spore', '200X Oxium', '2,500 Credits Cache', '100 Endo', '2X Shelter Debt-Bond', 'Garuda Systems BP', '5X Tepa Nodule', 'Lith K4 Relic', 'Synth Charge'], 
        'type': 'Operational Intelligence', 
        'enemyLevels': [10, 30], 
        'standingStages': [700, 700, 700], 
        'minMR': 1
      }, 
      {
        'id': 'VenusPreservationJobResource1595646185389', 
        'rewardPool': ['Madurai Lens', '200 Endo', '300X Circuits', '2X Medical Debt-Bond', 'Garuda Neuroptics BP', 'Meso D5 Relic', 'Synth Deconstruct'], 
        'type': 'Trash Their Traps', 
        'enemyLevels': [20, 40], 
        'standingStages': [640, 640, 640, 940], 
        'minMR': 2
      }, 
      {
        'id': 'VenusCullJobAssassinate1595646185389', 
        'rewardPool': ['Vazarin Lens', '300 Endo', '2X Fieldron', '2X Advances Debt-Bond', 'Neo N12 Relic', 'Tellurium', 'Synth Fiber'], 
        'type': 'Network Collapse', 
        'enemyLevels': [30, 50], 
        'standingStages': [620, 620, 620, 620, 1220], 
        'minMR': 3
      }, 
      {
        'id': 'VenusWetworkJobSpy1595646185389', 
        'rewardPool': ['400 Endo', '2X Familial Debt-Bond', '10,000 Credits Cache', 'Axi S7 Relic', '500X Kuva', 'Synth Reflex'], 
        'type': 'Falling Star', 
        'enemyLevels': [40, 60], 
        'standingStages': [740, 740, 740, 740, 1450], 
        'minMR': 5
      }, 
      {
        'id': 'VenusHelpingJobCaches1595646185389', 
        'rewardPool': ['400 Endo', '2X Familial Debt-Bond', '10,000 Credits Cache', 'Axi S7 Relic', '500X Kuva', 'Synth Reflex'], 
        'type': 'Seems Legit', 
        'enemyLevels': [100, 100], 
        'standingStages': [840, 840, 840, 840, 1660], 
        'minMR': 10
      }
    ], 
    'eta': '1m 57s'
  }, 
  {
    'id': '1595692740000ArbitersSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'Arbiters of Hexis', 
    'nodes': ['Terminus (Mercury)', 'Kiliken (Venus)', 'Sharpless (Phobos)', 'Eurasia (Earth)', 'Ultor (Mars)', 'Marid (Sedna)', 'Nuovo (Ceres)'], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000AssassinsSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'Assassins', 
    'nodes': ['E Gate (Venus)', 'Pantheon (Mercury)', 'Abaddon (Europa)', 'War (Mars)', 'Galatea (Neptune)', 'Ukko (Void)', 'Lex (Ceres)'], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000CephalonSudaSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'Cephalon Suda', 
    'nodes': ['Venera (Venus)', 'Vallis (Mars)', 'Ose (Europa)', 'Amalthea (Jupiter)', 'Everest (Earth)', 'Naeglar (Eris)', 'Numa (Saturn)'], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000EventSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'Operations Syndicate', 
    'nodes': [], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000NewLokaSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'New Loka', 
    'nodes': ['Cervantes (Earth)', 'Tharsis (Mars)', 'Helene (Saturn)', 'Carme (Jupiter)', 'Unda (Venus)', 'Kiste (Ceres)', 'Umbriel (Uranus)'], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000PerrinSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'Perrin Sequence', 
    'nodes': ['Mariana (Earth)', 'Odin (Mercury)', 'Enceladus (Saturn)', 'Olympus (Mars)', 'Cytherean (Venus)', 'Ani (Void)', 'Valefor (Europa)'], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000QuillsSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'Quills', 
    'nodes': [], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000RadioLegion2Syndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'RadioLegion2Syndicate', 
    'nodes': [], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000RadioLegion3Syndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'RadioLegion3Syndicate', 
    'nodes': [], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000RadioLegionIntermission2Syndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'RadioLegionIntermission2Syndicate', 
    'nodes': [], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000RadioLegionIntermissionSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'RadioLegionIntermissionSyndicate', 
    'nodes': [], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000RadioLegionSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'RadioLegionSyndicate', 
    'nodes': [], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000RedVeilSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'Red Veil', 
    'nodes': ['Ishtar (Venus)', 'Gaia (Earth)', 'Valac (Europa)', 'Shklovsky (Phobos)', 'Boethius (Mercury)', 'Nereid (Neptune)', 'Oceanum (Pluto)'], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000SteelMeridianSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'Steel Meridian', 
    'nodes': ['Linea (Venus)', 'Elion (Mercury)', 'Pallas (Ceres)', 'Cambria (Earth)', 'Cassini (Saturn)', 'Adrastea (Jupiter)', 'Cerberus (Pluto)'], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000VentKidsSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'Vent Kids', 
    'nodes': [], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }, 
  {
    'id': '1595692740000VoxSyndicate', 
    'activation': '2020-07-24T15:59:01.158Z', 
    'startString': '-11h 2m 6s', 
    'expiry': '2020-07-25T15:59:00.000Z', 
    'active': True, 
    'syndicate': 'Vox Solaris', 
    'nodes': [], 
    'jobs': [], 
    'eta': '12h 57m 52s'
  }
]