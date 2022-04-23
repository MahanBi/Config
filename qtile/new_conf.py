from libqtile import widget, bar, drawer, layout
from libqtile.config import Group, Drag, DropDown, Bar, Key, KeyChord, EzKey, Screen, Click
from libqtile.utils import guess_terminal
from libqtile.lazy import lazy
from libqtile.extension import window_list, dmenu, command_set
mod = "mod4"
terminal = guess_terminal()

groups = (
    Group(
        "1",
        layout="max",
        label="I"
    ),
    Group(
        "2",
        layout="max",
        label="II"
    ),
    Group(
        "3",
        layout="max",
        label="III"
    ),
    Group(
        "4",
        layout="columns",
        label="IV"
    ),
    Group(
        "5",
        layout="columns",
        label="V"
    )

)

keys = (
           # Restart, Shutdown, Reload
           Key(
               [mod, "control"], "a", lazy.shutdown(), desc="shutdown"
           ),
           Key(
               [mod, "control"], "s", lazy.restart(), desc="restart"
           ),
           Key(
               [mod, "control"], "d", lazy.reload_config(), desc="reload"
           ),
           # Open Application
           Key(
               [mod], "a", lazy.spawn("rofi -show drun"), desc="open rofi as drun"
           ),
           Key(
               [mod], "b", lazy.spawn("firefox")
           ),
           Key(
               [mod], "t", lazy.spawn("alacritty")
           ),

       ) + tuple((Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"got to group {i.name}") and
                  Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc=f"Move Window to group {i.name}")
                  for i in groups))

layouts = (
    layout.Max(),
    layout.Columns()
)

screens = (
    Screen(
        top=bar.Bar(
            [widget.CurrentLayout()],
            24
        ),
    )
)
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
auto_fullscreen = True
wl_input_rules = None
auto_minimize = True
wmname = "LG3D"
