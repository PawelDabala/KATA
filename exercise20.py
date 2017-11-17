class PokeScan:

    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def info(self):

        dic_name = {'Squirtle':'water', 'Charmander':'fire', 'Bulbasaur':'grass'}
        dic_type = {'water':'wet', 'fire':'fiery', 'grass':'grassy' }

        type_lavel = ""
        if self.level <= 20:
            type_lavel = 'weak'
        elif 20 < self.level <=50:
            type_lavel = 'fairy'
        else:
            type_lavel = 'strong'

        return '{}, a {} and {} Pokemon.'.format(self.name, dic_type[self.pkmntype], type_lavel )




p1 = PokeScan('Squirtle', 100, 'water')
print(p1.info())