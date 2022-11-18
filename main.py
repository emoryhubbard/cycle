from cast import Cast
from player1 import Player1
from script import Script
from move_actors_action import MoveActorsAction
from draw_actors_action import DrawActorsAction
from control_actors_action import ControlActorsAction
from director import Director
from OutputService import OutputService
from InputService import InputService

from handle_collisions_action import handle_collision_actions

def main():

    cast = Cast()
    cast.add_actor("players", Player1())
    #add more actors here

    output_service = OutputService()
    input_service = InputService()

    script = Script()
    script.add_action("input", ControlActorsAction(input_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("output", DrawActorsAction(output_service))
    script.add_action("update", handle_collision_actions())
    #add more scripts here, like collisions

    director = Director(output_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()