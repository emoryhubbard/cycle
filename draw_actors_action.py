from action import Action

class DrawActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        all_actors = cast.get_all_actors()

        self._output_service.clear_buffer()
        for actor in all_actors:
            self._output_service.draw_actor(actor)
        self._output_service.flush_buffer()