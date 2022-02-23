############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(code='musk', first_harvest='1998', color='green', is_seedless=True, is_bestseller=True, name='Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)
    
    cas = MelonType(code='cas', first_harvest='2003', color='orange', is_seedless=False, is_bestseller=False, name='Casaba')
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)
    
    cren = MelonType(code='cren', first_harvest='1996', color='green', is_seedless=False, is_bestseller=False, name='Crenshaw')
    cren.add_pairing('prosciutto')
    all_melon_types.append(cren)
    
    yw = MelonType(code='yw', first_harvest='2013', color='yellow', is_seedless=False, is_bestseller=True, name='Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print()



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons_by_id = {}
    for melon in melon_types:
        if melon.code not in melons_by_id:
            melons_by_id[melon.code] = melon

    return melons_by_id


# melon_types = make_melon_types()

# print_pairing_info(melon_types)

# melons_lookup = make_melon_type_lookup(melon_types)

# print(melons_lookup)


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        """Initialize a melon instance"""
        
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        """Determine if the melon can be sold"""

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons_by_id = make_melon_type_lookup(melon_types)
    melons = []
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2,'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2,'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3,'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35,'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35,'Micheal')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35,'Micheal')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4,'Micheal')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4,'Micheal')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3,'Sheila')
    
    melons.extend(
        [
            melon_1,
            melon_2,
            melon_3,
            melon_4,
            melon_5,
            melon_6,
            melon_7,
            melon_8,
            melon_9
        ]
    )
    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() == True:
            sellable = "CAN BE SOLD"
        else:
            sellable = "NOT SELLABLE"
        print(f'Havested by {melon.harvester} from Field {melon.field}. {sellable}')


# melons = make_melons(melon_types)

# get_sellability_report(melons)
