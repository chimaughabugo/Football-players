class Player:
    """An attempt to model top football players"""

    def __init__(self, first_name, last_name, sex, position, language, club, country):
        """Initialize attributes ofPlayer"""
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.language = language
        self.position = position
        self.location = country
        self.club = club

    def player_data(self):
        """Put players details in a dictionary"""
        player_details = {
            'First name': self.first_name,
            'Last name': self.last_name,
            'sex': self.sex,
            'language': self.language,
            'location': self.location
        }
        #Simulate player details
        for k, v in player_details.items():
            print(f"{k}: {v}")

    def greet_player(self):
        """Print greeting to Player"""
        print(f'\nGood evening Mr. {self.last_name}.')

player_01 = Player('Ansu', 'Fati', 'Male', 'Forward', 'Spanish', 'Barcelona', 'Spain')
player_01.player_data()
player_01.greet_player()

player_02 = Player('Lionel', 'Messi', 'Male', 'Forward', 'Spanish', 'PSG', 'Argentina')
player_02.player_data()
player_02.greet_player()

player_03 = Player('Asisat', 'Oshoala', 'Female', 'Forward', 'English', 'Barcelona', 'Nigeria')
player_03.player_data()
player_03.greet_player()

player_04 = Player('Maco', 'Ter Stegen', 'Male', 'Goal Keeper', 'German', 'Barcelona', 'Germany')
player_04.player_data()
player_04.greet_player()