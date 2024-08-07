from typing import Self

from game.byte_2025.character import Character, CharacterType
from game.common.enums import ObjectType, CountryType
from game.common.game_object import GameObject


class TeamManager(GameObject):
    """
    `TeamManager class notes:`

    TeamManager (replacing the Avatar class) inherits from GameObject

    Values:
        Team - list of characters (max of three) with a default generic team
        Score - an int for the current score of this team with a default set to 0

    Methods:
        speed_sort() - returns sorted list of team by fastest to slowest speed
        filter_by_type(character_type) - returns list of characters of the specified CharacterType
    """

    ''' 
    The team default has a warning "Default argument value is mutable".
    This is due to the list being mutable and if the Character() default is changed in the future, 
    the default for team in the TeamManager class is also changed. This, for the most part, can be 
    ignored, but reminder to exercise caution when adjusting the Character class for this reason.
    '''

    def __init__(self, team: list[Character] = [Character(), Character(), Character()],
                 country: CountryType = CountryType.URODA):
        super().__init__()
        self.object_type: ObjectType = ObjectType.TEAMMANAGER
        self.team: list[Character] = team
        self.country = country
        self.score: int = 0

    # Getters and Setters
    @property
    def team(self) -> list[Character]:
        return self.__team

    @team.setter
    def team(self, team: list[Character]) -> None:
        if team is None or not isinstance(team, list):
            raise ValueError(
                f'{self.__class__.__name__}.team must be a list[Character]. It is a(n) {team.__class__.__name__} '
                f'and has the value of {team}.')
        for i in team:
            if i is None or not isinstance(i, Character):
                raise ValueError(
                    f'{self.__class__.__name__}.team must be a list[Character]. It contains a(n) '
                    f'{i.__class__.__name__} with the value {i}.')
        if len(team) > 3:
            raise ValueError(f'{self.__class__.__name__}.team must be a list[Character] with a length of three or '
                             f'less. It has a length of {len(team)}.')
        self.__team: list[Character] = team

    @property
    def object_type(self) -> ObjectType:
        return self.__object_type

    @object_type.setter
    def object_type(self, object_type: ObjectType) -> None:
        if object_type is None or not isinstance(object_type, ObjectType):
            raise ValueError(
                f'{self.__class__.__name__}.object_type must be an ObjectType. It is a(n) '
                f'{object_type.__class__.__name__} and has the value of {object_type}.')
        self.__object_type: ObjectType = object_type

    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, score: int) -> None:
        if score is None or not isinstance(score, int):
            raise ValueError(f'{self.__class__.__name__}.score must be an int. It is a(n) {score.__class__.__name__} '
                             f'and has the value of {score}.')
        self.__score: int = score

    # Method to sort team based on character speed, fastest to slowest (descending order)
    def speed_sort(self) -> None:
        """
        Sorts the team by the speed stat in descending order.
        """
        self.team = sorted(self.team, key=lambda character: character.speed, reverse=True)

    # Method to filter the team by a character type
    def filter_by_type(self, character_type: CharacterType) -> list[Character]:
        """
        Returns characters from this team that have the specified character_type.
        """
        return [character for character in self.team if character.character_type is character_type]

    def get_active_character(self) -> Character:
        """
        Returns the first character in the team that hasn't taken its turn.
        """
        for character in self.team:
            if not character.took_action:
                return character

    # To and From Json
    def to_json(self) -> dict:
        data: dict = super().to_json()
        data['team'] = self.team
        data['country'] = self.country
        data['score'] = self.score
        return data

    def from_json(self, data: dict) -> Self:
        super().from_json(data)
        self.team = data['team']
        self.country = data['country']
        self.score = data['score']
        return self
