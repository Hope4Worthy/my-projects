import pynput

up = pynput.keyboard.Key.up
down = pynput.keyboard.Key.down
left = pynput.keyboard.Key.left
right = pynput.keyboard.Key.right

support = [
  [down, up, up, left, right, "airburstRocketLauncher"],
  [down, left, right, up, down, "antiMaterialRifle"],
  [down, right, down, up, left, left, "arcThrower"],
  [down, left, down, up, up, right, "autocannon"],
  [down, left, up, down, right, "commando"],
  [down, right, up, left, right, "deEscalator"],
  [down, left, right, right, down, "defoliationTool"],
  [down, left, up, left, right, "epoch"],
  [down, down, left, up, right, "expendableAntiTank"],
  [down, down, left, up, left, "expendableNapalm"],
  [down, left, up, down, up, "flamethrower"],
  [down, left, up, left, down, "grenadeLauncher"],
  [down, left, up, down, down, "heavyMachineGun"],
  [down, left, up, left, down, "laserCannon"],
  [down, left, down, up, right, "machineGun"],
  [down, left, right, down, up, up, "maxigun"],
  [down, left, right, right, up, "oneTrueFlag"],
  [down, down, up, left, right, "quasarCannon"],
  [down, right, down, up, left, right, "railgun"],
  [down, left, right, right, left, "recoillessRifle"],
  [down, up, right, down, down, "soloSilo"],
  [down, down, up, down, down, "spear"],
  [down, right, down, left, up, right, "spearGun"],
  [down, left, down, up, up, left, "stalwart"],
  [down, left, up, down, left, "sterilizer"],
  [down, down, up, down, right, "waspLauncher"]
]

backpack = [
  [down, left, down, down, up, left, "ballisticShield"],
  [down, right, up, up, right, up, "c4Pack"],
  [down, up, left, right, up, up, "directionalShield"],
  [down, up, left, up, right, down, "guardDog"],
  [down, up, left, up, right, up, "guardDogDogBreath"],
  [down, up, left, up, left, left, "guardDogHotDog"],
  [down, up, left, up, right, left, "guardDogK9"],
  [down, up, left, up, right, right, "guardDogRover"],
  [down, up, up, down, left, right, "hoverPack"],
  [down, up, up, down, up, "jumpPack"],
  [down, up, left, right, left, right, "personalShield"],
  [down, right, up, up, up, "portableHellbomb"],
  [down, left, down, up, up, down, "supplyPack"],
  [down, left, right, down, left, right, "warpPack"]
]

defensive = [
  [down, up, left, right, right, right, "antiTankEmplacement"],
  [down, right, down, left, right, "grenadierBattlement"],
  [down, up, left, right, right, left, "hmgEmplacment"],
  [down, down, left, right, left, right, "shieldGenerator"]
]

sentry = [
  [down, up, right, up, left, up, "autocannon"],
  [down, up, right, down, right, "emsMortar"],
  [down, up, right, down, up, up, "flame"],
  [down, up, right, left, "gatling"],
  [down, up, right, down, up, right, "laser"],
  [down, up, right, right, up, "machineGun"],
  [down, up, right, right, down, "mortar"],
  [down, up, right, right, left, "rocket"],
  [down, up, right, up, left, down, "teslaTower"]
]

mine = [
  [down, left, up, right, "antiPersonnel"],
  [down, left, up, up, "antiTank"],
  [down, left, left, right, "gas"],
  [down, left, left, down, "incindiary"]
]

orbital = [
  [right, right, down, left, right, down, "120mmBarrage"],
  [right, down, up, up, left, down, down, "380mmBarrage"],
  [right, right, right, "airburstStrike"],
  [right, right, left, down, "emsStrike"],
  [right, right, down, right, "gasStrike"],
  [right, down, left, up, up, "gatlingBarrage"],
  [right, down, up, right, down, "laser"],
  [right, right, down, left, right, up, "napalm"],
  [right, right, up, "precisionStrike"],
  [right, up, down, down, right, "railcannonStrike"],
  [right, right, down, up, "smokeStrike"],
  [right, down, right, down, right, down, "walkingBarrage"]
]

eagle = [
  [up, down, up, left, "110mmRocketPods"],
  [up, right, down, down, down, "500kgBomb"],
  [up, right, down, right, "airstrike"],
  [up, right, down, down, right, "clusterBomb"],
  [up, right, down, up, "napalmAirstrike"],
  [up, right, up, down, "smokeStrike"],
  [up, right, right, "strafingRun"]
]

vehicle = [
  [left, down, right, up, left, down, up, "emancipatorExosuit"],
  [left, down, right, down, right, down, up, "fastReconVehicle"],
  [left, down, right, up, left, down, down, "patriotExosuit"]
]


mission_reinforce       = [up, down, right, left, up, "reinforce"]
mission_resupply        = [down, down, up, right, "resupply"]

GROUPS = {
    "support": support,
    "backpack": backpack,
    "defensive": defensive,
    "sentry": sentry,
    "mine": mine,
    "orbital": orbital,
    "eagle": eagle,
    "vehicle": vehicle
}

# Predefined loadouts
loadouts = {
    "Bots": [
        ("eagle", "airstrike"),
        ("orbital", "railcannonStrike"),
        ("support", "railgun"),
        ("backpack", "personalShield")
    ],
    "Bugs": [
        ("eagle", "airstrike"),
        ("orbital", "railcannonStrike"),
        ("orbital", "precisionStrike"),
        ("backpack", "personalShield")
    ],
    "Defense": [
        ("sentry", "autocannon"),
        ("orbital", "railcannonStrike"),
        ("support", "quasarCannon"),
        ("backpack", "personalShield")
    ]
}


none = []

def find_strat(group, name):
    for sub_array in group_array:
        if sub_array and sub_array[-1] == name:
            return sub_array
    return None

def get_names(group_name):
    return [s[-1] for s in GROUPS[group_name]]