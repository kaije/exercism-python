SECONDS_PER_EARTH_YEAR = 31557600


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def age_in_seconds(self, orbital_period):
        age = self.seconds / (SECONDS_PER_EARTH_YEAR * orbital_period)
        return round(age, 2)

    def on_mercury(self):
        return self.age_in_seconds(0.2408467)

    def on_venus(self):
        return self.age_in_seconds(0.61519726)

    def on_earth(self):
        return self.age_in_seconds(1)

    def on_mars(self):
        return self.age_in_seconds(1.8808158)

    def on_jupiter(self):
        return self.age_in_seconds(11.862615)

    def on_saturn(self):
        return self.age_in_seconds(29.447498)

    def on_uranus(self):
        return self.age_in_seconds(84.016846)

    def on_neptune(self):
        return self.age_in_seconds(164.79132)
