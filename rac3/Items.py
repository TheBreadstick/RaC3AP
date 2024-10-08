from BaseClasses import Item, ItemClassification
from .Types import ItemData, RaC3Item, weapon_type_to_shortened_name, WeaponType, EventData
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import RaC3World


def create_itempool(world: "RaC3World") -> List[Item]:
    itempool: List[Item] = []

    for name in item_table.keys():
        item_type: ItemClassification = item_table.get(name).classification
        item_amount: int = item_table.get(name).count

        itempool += create_multiple_items(world, name, item_amount, item_type)

    victory = create_item(world, "Dr. Nefarious Defeated!")
    world.multiworld.get_location("Dr. Nefarious Defeated!", world.player).place_locked_item(victory)

    itempool += create_junk_items(world, get_total_locations(world) - len(itempool) - 1)
    return itempool

def create_multiple_items(world: "RaC3World", name: str, count: int = 1,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [RaC3Item(name, item_type, data.ap_code, world.player)]

    return itemlist

def create_item(world: "RaC3World", name: str) -> Item:
    data = item_table[name]
    return RaC3Item(name, data.classification, data.ap_code, world.player)

def create_junk_items(world: "RaC3World", count: int) -> List[Item]:
    junk_pool: List[Item] = []
    # For now, all junk has equal weights
    for i in range(count):
        junk_pool.append(world.create_item(world.random.choices(list(junk_items.keys()), k=1)[0]))
    return junk_pool


weapon_items = {
    "Shock Blaster": ItemData(50001400, ItemClassification.progression, 1),
    "Nitro Launcher": ItemData(50001401, ItemClassification.progression, 1),
    "N60 Storm": ItemData(50001402, ItemClassification.progression, 1),
    "Plasma Whip": ItemData(50001403, ItemClassification.progression, 1),
    "Infector": ItemData(50001404, ItemClassification.progression, 1),
    "SUCC Cannon": ItemData(50001405, ItemClassification.progression, 1),
    "Spitting Hydra": ItemData(50001406, ItemClassification.progression, 1),
    "Agents of Doom": ItemData(50001407, ItemClassification.progression, 1),
    "Flux Rifle": ItemData(50001408, ItemClassification.progression, 1),
    "Annihilator": ItemData(50001409, ItemClassification.progression, 1),
    "Holo-Shield Glove": ItemData(50001410, ItemClassification.progression, 1),
    "Disk-Blade Gun": ItemData(50001411, ItemClassification.progression, 1),
    "Rift Inducer": ItemData(50001412, ItemClassification.progression, 1),
    "Qwack-O-Ray": ItemData(50001413, ItemClassification.progression, 1),
    "RY3N0": ItemData(50001414, ItemClassification.progression, 1),
    "Mega-Turret Glove": ItemData(50001415, ItemClassification.progression, 1),
    "Lava Gun": ItemData(50001416, ItemClassification.progression, 1),
    "Shield Charger": ItemData(50001417, ItemClassification.progression, 1),
    "Bouncer": ItemData(50001418, ItemClassification.progression, 1),
    "Plasma Coil": ItemData(50001419, ItemClassification.progression, 1)
}

progressive_weapons = {
    "Progressive Shock Blaster": ItemData(50001420, ItemClassification.useful, 4),
    "Progressive Nitro Launcher": ItemData(50001421, ItemClassification.useful, 4),
    "Progressive N60 Storm": ItemData(50001422, ItemClassification.useful, 4),
    "Progressive Plasma Whip": ItemData(50001423, ItemClassification.useful, 4),
    "Progressive Infector": ItemData(50001424, ItemClassification.useful, 4),
    "Progressive SUCC Cannon": ItemData(50001425, ItemClassification.useful, 4),
    "Progressive Spitting Hydra": ItemData(50001426, ItemClassification.useful, 4),
    "Progressive Agents of Doom": ItemData(50001427, ItemClassification.useful, 4),
    "Progressive Flux Rifle": ItemData(50001428, ItemClassification.useful, 4),
    "Progressive Annihilator": ItemData(50001429, ItemClassification.useful, 4),
    "Progressive Holo-Shield Glove": ItemData(50001430, ItemClassification.useful, 4),
    "Progressive Disk-Blade Gun": ItemData(50001431, ItemClassification.useful, 4),
    "Progressive Rift Inducer": ItemData(50001432, ItemClassification.useful, 4),
    "Progressive Qwack-O-Ray": ItemData(50001433, ItemClassification.useful, 4),
    "Progressive RY3N0": ItemData(50001434, ItemClassification.useful, 4),
    "Progressive Mega-Turret Glove": ItemData(50001435, ItemClassification.useful, 4),
    "Progressive Lava Gun": ItemData(50001436, ItemClassification.useful, 4),
    "Progressive Shield Charger": ItemData(50001437, ItemClassification.useful, 4),
    "Progressive Bouncer": ItemData(50001438, ItemClassification.useful, 4),
    "Progressive Plasma Coil": ItemData(50001439, ItemClassification.useful, 4)
}
gadget_items = {
    "Hacker" :ItemData(50001440, ItemClassification.progression, 1),
    "Hypershot": ItemData(50001441, ItemClassification.progression, 1),
    "Refractor": ItemData(50001442, ItemClassification.progression, 1),
    "Tyhrra-Guise": ItemData(50001443, ItemClassification.progression, 1),
    "Grav-Boots": ItemData(50001444, ItemClassification.progression, 1),
    "Bolt Grabber V2": ItemData(50001445, ItemClassification.useful, 1),
    "Map-O-Matic": ItemData(50001446, ItemClassification.useful, 1),
    "Nano Pak": ItemData(50001447, ItemClassification.useful, 1),
    "Warp Pad": ItemData(50001448, ItemClassification.progression, 1),
    "Gadgetron PDU": ItemData(50001449, ItemClassification.useful, 1)

}

post_planets = {
    "Infobot: Marcadia": ItemData(50001452, ItemClassification.progression, 1), # Post Starship Phoenix Visit 1
    "Infobot: Annihilation Nation": ItemData(50001453, ItemClassification.progression, 1), # Post Starship Phoenix Visit 2 + Qwark Vidcomic 1
    "Infobot: Aquatos": ItemData(50001454, ItemClassification.progression, 1), # Post Starship Phoenix Visit 3
    "Infobot: Tyhrranosis": ItemData(50001455, ItemClassification.progression, 1), # Post Starship Phoenix Visit 4
    "Infobot: Daxx": ItemData(50001456, ItemClassification.progression, 1), # Post Starship Phoenix Visit 5
    "Infobot: Obani Gemini": ItemData(50001457, ItemClassification.progression, 1), # Post Starship Phoenix Visit 6 + Qwark Vidcomic 3
    "Infobot: Rilgar": ItemData(50001458, ItemClassification.progression, 1), # Post Obani Gemini
    "Infobot: Holostar Studios": ItemData(50001459, ItemClassification.progression, 1), # Post Rilgar + Annihilation Nation Challenges
    "Infobot: Obani Draco": ItemData(50001460, ItemClassification.progression, 1), # Post Holostar Studios
    "Infobot: Zeldrin Starport": ItemData(50001461, ItemClassification.progression, 1), # Post Obani Draco
    "Infobot: Metropolis": ItemData(50001462, ItemClassification.progression, 1), # Post Zeldrin Starport + Qwark Vidcomic 4
    "Infobot: Zeldrin": ItemData(50001463, ItemClassification.progression, 1), # Post Starship Phoenix Visit 7
    "Infobot: Aridia": ItemData(50001464, ItemClassification.progression, 1), # Post Zeldrin
    "Infobot: Qwarks Hideout": ItemData(50001465, ItemClassification.progression, 1), # Post Starship Phoenix Visit 8 + Qwark Vidcomic 5
    "Infobot: Koros": ItemData(50001466, ItemClassification.progression, 1), # Post Starship Phoenix Visit 9
    "Infobot: Mylon": ItemData(50001467, ItemClassification.progression, 1), # Post-Koros
}
qwark_vidcomics = {
    "Qwark Vidcomic 1": ItemData(50001468, ItemClassification.progression, 1),
    "Qwark Vidcomic 2": ItemData(50001469, ItemClassification.progression, 1),
    "Qwark Vidcomic 3": ItemData(50001470, ItemClassification.progression, 1),
    "Qwark Vidcomic 4": ItemData(50001471, ItemClassification.progression, 1),
    "Qwark Vidcomic 5": ItemData(50001472, ItemClassification.progression, 1),
}


progressive_armor = {
    "Progressive Armor": ItemData(50001480, ItemClassification.useful, 4)
}


t_bolts = {
    "Titanium Bolt": ItemData(50001490, ItemClassification.filler, 35)
}

junk_items = {
    "Bolts": ItemData(50001491, ItemClassification.filler, 0),
    "Weapon EXP": ItemData(50001492, ItemClassification.filler, 0)
}

victory_item = {
    "Dr. Nefarious Defeated!": ItemData(50001481, ItemClassification.progression, 0)
}


item_table ={
    **weapon_items,
    **progressive_weapons,
    **gadget_items,
    **post_planets,
    **qwark_vidcomics,
    **progressive_armor,
    **t_bolts,
    **junk_items,
    **victory_item

}