import pynput

up = pynput.keyboard.Key.up
down = pynput.keyboard.Key.down
left = pynput.keyboard.Key.left
right = pynput.keyboard.Key.right

support_machineGun          = [down, left, down, up, right]
support_antiMaterialRifle   = [down, left, right, up, down]
support_stalwart            = [down, left, down, up, up, left]
support_expendableAntiTank  = [down, down, left, up, right]
support_recoillessRifle     = [down, left, right, right, left]
support_flmaethrower        = [down, left, up, down, up]
support_autocannon          = [down, left, down, up, up, right]
support_railgun             = [down, right, down, up, left, right]
support_spear               = [down, down, up, down, down]
support_grenadeLauncher     = [down, left, up, left, down]
support_laserCannon         = [down, left, up, left, down]
support_arcThrower          = [down, right, down, up, left, left]
support_quasarCannon        = [down, down, up, left, right]
support_heavyMachineGun     = [down, left, up, down, down]

backpack_jumpPack           = [down, up, up, down, up]
backpack_supplyPack         = [down, left, down, up, up, down]
backpack_ballisticShield    = [down, left, down, down, up, left]
backpack_guardDog           = [down, up, left, up, right, down]
backpack_rover              = [down, up, left, up ,right, right]
backpack_personalShield     = [down, up, left, right, left, right]

defensive_hmgEmplacment         = [down, up, left, right, right, left]
defensive_shieldGenerator       = [down, down, left, right, left, right]
defensive_teslaTower            = [down, up, right, up, left, down]
defensive_antiPersonnelMines    = [down, left, up, right]
defensive_incendiaryMines       = [down, left, left, down]

sentry_machineGun   = [down, up, right, right, up]
sentry_gatling      = [down, up, right, left]
sentry_mortar       = [down, up, right, right, down]
sentry_autocannon   = [down, up, right, up, left, up]
sentry_rocket       = [down, up, right, right, left]
sentry_emsMortar    = [down, up, right, down, right]

orbital_precisionStrike     = [right, right, up]
orbital_gatlingBarrage      = [right, down, left, up, up]
orbital_airburstStrike      = [right, right, right]
orbital_120mmBarrage        = [right, right, down, left, right, down]
orbital_380mmBarrage        = [right, down, up, up, left, down, down]
orbital_walkingBarrage      = [right, down, right, down, right, down]
orbital_laser               = [right, down, up, right, down]
orbital_railcannonStrike    = [right, up, down, down, right]
orbital_gasStrike           = [right, right, down, right]
orbital_emsStrike           = [right, right, left, down]
orbital_smokeStrike         = [right, right, down, up]

eagle_strafingRun       = [up, right, right]
eagle_airstrike         = [up, right, down, right]
eagle_clusterBomb       = [up, right, down, down, right]
eagle_napalmAirstrike   = [up, right, down, up]
eagle_smokeStrike       = [up, right, up, down]
eagle_110mmRocketPods   = [up, down, up, left]
eagle_500kgBomb         = [up, right, down, down, down]

mech_patriotExosuit     = [left, down, right, up, left, down, down]
mission_reinforce       = [up, down, right, left, up]
mission_resupply        = [down, down, up, right]
mission_hellbomb        = [down, up, left, down, up, right, down, up]
mission_artillery       = [right, up, up, down]

none = []