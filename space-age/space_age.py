"""
   - Earth: orbital period 365.25 Earth days, or 31557600 seconds
   - Mercury: orbital period 0.2408467 Earth years
   - Venus: orbital period 0.61519726 Earth years
   - Mars: orbital period 1.8808158 Earth years
   - Jupiter: orbital period 11.862615 Earth years
   - Saturn: orbital period 29.447498 Earth years
   - Uranus: orbital period 84.016846 Earth years
   - Neptune: orbital period 164.79132 Earth years
"""


class SpaceAge(object):
    YEAR_ON_EARTH = 31557600.0
    YEAR_ON_MERCURY = YEAR_ON_EARTH * 0.2408467
    YEAR_ON_VENUS = YEAR_ON_EARTH * 0.61519726
    YEAR_ON_MARS = YEAR_ON_EARTH * 1.8808158
    YEAR_ON_JUPITER = YEAR_ON_EARTH * 11.862615
    YEAR_ON_SATURN = YEAR_ON_EARTH * 29.447498
    YEAR_ON_URANUS = YEAR_ON_EARTH * 84.016846
    YEAR_ON_NEPTUNE = YEAR_ON_EARTH * 164.79132

    def __init__(self, seconds):
        self.seconds = seconds

    # I wonder if there is some meta-programming trick
    # like Ruby's method_missing so that I could put these
    # in a dictionary or somesuch and not repeat the same
    # method over and over just with a small CONST difference
    def on_earth(self):
        return round(self.seconds / self.YEAR_ON_EARTH, 2)

    def on_mercury(self):
        return round(self.seconds / self.YEAR_ON_MERCURY, 2)

    def on_venus(self):
        return round(self.seconds / self.YEAR_ON_VENUS, 2)

    def on_mars(self):
        return round(self.seconds / self.YEAR_ON_MARS, 2)

    def on_jupiter(self):
        return round(self.seconds / self.YEAR_ON_JUPITER, 2)

    def on_saturn(self):
        return round(self.seconds / self.YEAR_ON_SATURN, 2)

    def on_uranus(self):
        return round(self.seconds / self.YEAR_ON_URANUS, 2)

    def on_neptune(self):
        return round(self.seconds / self.YEAR_ON_NEPTUNE, 2)
