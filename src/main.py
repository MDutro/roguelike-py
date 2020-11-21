import tcod
from actions import EscapeAction, MovementAction
from player_inputs import EventHandler

def main() -> None:
    screen_width, screen_height = 80, 60

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "./img/dejavu16x16_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()
    # create console
    console = tcod.Console(screen_width, screen_height)
    # create the actual window
    with tcod.context.new(
        # screen_width,
        # screen_height,
        columns = console.width,
        rows = console.height,
        tileset = tileset,
        title = "Dungeon of Doom!!!",
        vsync = True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")
            # print stuff to the console/screen
            context.present(root_console)
            # clear the console so you don't leave a trail as you move around
            root_console.clear()

            for event in tcod.event.wait():                
                action = event_handler.dispatch(event)

                if action is None:
                    continue
                
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()
    

if __name__ == "__main__":
    main()