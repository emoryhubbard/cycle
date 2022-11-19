import constants
from action import Action
from point import Point
from InputService import InputService

class ControlActorsAction(Action):

    def __init__(self, input_service):
        self._input_service = input_service

    def execute(self, cast):
        p1_direction = None #p1 hasn't pressed key
        p2_direction = None #p2 hasn't pressed key.

        if self._input_service.is_key_down('a'):
            p1_direction = Point(-constants.CELL_SIZE, 0)

        if self._input_service.is_key_down('d'):
            p1_direction = Point(constants.CELL_SIZE, 0)

        if self._input_service.is_key_down('w'):
            p1_direction = Point(0, -constants.CELL_SIZE)

        if self._input_service.is_key_down('s'):
            p1_direction = Point(0, constants.CELL_SIZE)

        #if p1_direction isn't None, p1 pressed the key
        player1 = cast.get_first_actor("players")
        if p1_direction != None:
            player1.turn_bike(p1_direction)

        if self._input_service.is_key_down('j'):
            p2_direction = Point(-constants.CELL_SIZE, 0)

        if self._input_service.is_key_down('l'):
            p2_direction = Point(constants.CELL_SIZE, 0)

        if self._input_service.is_key_down('i'):
            p2_direction = Point(0, -constants.CELL_SIZE)

        if self._input_service.is_key_down('k'):
            p2_direction = Point(0, constants.CELL_SIZE)
        #if p2_direction isn't None, p2 pressed the key
        player2 = cast.get_secound_actor("players")
        if p2_direction != None:
            player2.turn_bike(p2_direction)