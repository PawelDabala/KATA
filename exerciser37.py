# Write a function that will randomly upper and lower characters in a string - randomCase() (random_case() for Python).
#
# A few examples:
#
# randomCase("Lorem ipsum dolor sit amet, consectetur adipiscing elit") == "lOReM ipSum DOloR SiT AmeT, cOnsEcTEtuR aDiPiSciNG eLIt"
#
# randomCase("Donec eleifend cursus lobortis") == "DONeC ElEifEnD CuRsuS LoBoRTIs"
# Note: this function will work within the basic ASCII character set to make this kata easier - so no need to make the function multibyte safe.
from random import randint


def random_case(x):
    split_list = list(x)
    temps = []
    for i in split_list:
        ran = randint(0, 1)
        if ran:
            temps.append(i.upper())
        else:
            temps.append(i.lower())

    return "".join(temps)

print(random_case("Lorem ipsum dolor sit amet, consectetur adipiscing elit"))


import random

def random_case(x):
    return "".join([random.choice([c.lower(), c.upper()]) for c in x])