import os
import subprocess

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
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
        [mod], "t", lazy.spawn("alacritty")
    ),
    # Layout
    Key(
        [mod, "shift"], "n", lazy.next_layout(), desc="change layout next"
    ),

    # Switch To Window
    Key(
        [mod, "shift"], "Right", lazy.group.next_window(), desc="next window"
    ),
    Key(
        [mod, "shift"], "Left", lazy.group.prev_window(), desc="prev window"
    ),
    Key(
        [mod, "shift"], "Up", lazy.layout.increase_ratio(), desc="increase ratio"
    ),
    Key(
        [mod, "shift"], "Down", lazy.layout.decrease_ratio(), desc="decrease ratio"
    ),
    Key(
        [mod], "q", lazy.window.kill(), desc="Quit Window"
    ),
    Key(
        [mod], "l", lazy.run_extension(extension.WindowList(
            dmenu_bottom=True,
            background="#212d3c",
            foreground="#6cb0dc",
            item_format="{window}",
            selected_background="#4a739d",
            selected_foreground="#b3e0f6",
        ))
    )
]

groups = [
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
        layout="floating",
        label="IV"
    ),
    Group(
        "5",
        layout="floating",
        label="V"
    )
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Floating(
        border_focus="#8fd6f5",
        border_normal="#1c314f",
        border_width=3,
    ),
    layout.Max(),
]

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=10,
                ),
                widget.TextBox(
                    text="\uE0B6",
                    fontsize=25,
                    foreground="#313d5a",
                    padding=1
                ),
                widget.Net(
                    format="U {up} D {down}",
                    background="#313d5a",
                    foreground="#6cb0dc"
                ),
                widget.TextBox(
                    text='\uE0B4',
                    fontsize=25,
                    foreground="#313d5a",
                    padding=0
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.TextBox(
                    text="\uE0B6",
                    fontsize=25,
                    foreground="#313d5a",
                    padding=0
                ),
                widget.NvidiaSensors(
                    background="#313d5a",
                    foreground="#6cb0dc",
                    format="{temp}??C"
                ),
                widget.TextBox(
                    text='\uE0B4',
                    fontsize=25,
                    foreground="#313d5a",
                    padding=0
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.TextBox(
                    text="\uE0B6",
                    fontsize=25,
                    foreground="#313d5a",
                    padding=1
                ),
                widget.Memory(
                    background="#313d5a",
                    foreground="#6cb0dc",
                    measure_mem="G"
                ),
                widget.TextBox(
                    text='\uE0B4',
                    fontsize=25,
                    foreground="#313d5a",
                    padding=0
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.TextBox(
                    text="\uE0B6",
                    fontsize=25,
                    foreground="#3b5373",
                    padding=1
                ),
                widget.CPU(
                    background="#3b5373",
                    foreground="#6cb0dc",
                    format="{freq_current}GHz {load_percent}%"
                ),
                widget.TextBox(
                    text='\uE0B4',
                    fontsize=25,
                    foreground="#3b5373",
                    padding=0
                ),
                widget.Spacer(
                    length=500,
                ),
                widget.TextBox(
                    text="\uE0B6",
                    fontsize=25,
                    foreground="#212d3c",
                    padding=1
                ),
                widget.GroupBox(
                    active="#e7eefa",
                    background="#212d3c",
                    disable_drag=True,
                    inactive="#4a739d"
                ),
                widget.TextBox(
                    text='\uE0B4',
                    fontsize=25,
                    foreground="#212d3c",
                    padding=0
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.TextBox(
                    text="\uE0B6",
                    fontsize=25,
                    foreground="#212d3c",
                    padding=1
                ),
                widget.CurrentLayout(
                    background="#212d3c",
                    foreground="#6cb0dc"
                ),
                widget.TextBox(
                    text='\uE0B4',
                    fontsize=25,
                    foreground="#212d3c",
                    padding=0
                ),
                widget.Spacer(
                    length=350,
                ),
                widget.TextBox(
                    text="\uE0B6",
                    fontsize=25,
                    foreground="#212d3c",
                    padding=1
                ),
                widget.Clock(
                    background="#212d3c",
                    foreground="#6cb0dc",
                    format="%d/%m/%y %H:%M",
                    timezone=None
                ),
                widget.TextBox(
                    text='\uE0B4',
                    fontsize=25,
                    foreground="#212d3c",
                    padding=0
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.TextBox(
                    text="\uE0B6",
                    fontsize=25,
                    foreground="#525d72",
                    padding=1
                ),
                widget.PulseVolume(
                    background="#525d72",
                    foreground="#6cb0dc",
                    step=1,
                ),
                widget.TextBox(
                    text='\uE0B4',
                    fontsize=25,
                    foreground="#525d72",
                    padding=0
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.TextBox(
                    text="\uE0B6",
                    fontsize=25,
                    foreground="#313d5a",
                    padding=1
                ),
                widget.Systray(
                    background="#313d5a"
                ),
                widget.TextBox(
                    text='\uE0B4',
                    fontsize=25,
                    foreground="#313d5a",
                    padding=0
                ),

                widget.Spacer(
                    length=20,
                ),
                widget.Sep(
                    linewidth=5
                ),
            ],
            24,
            background="#2c2c2b",  # "#2c2c2b",
            foreground=["#A8A8A8", "#A8A8A8"],
            border_color="#2c2c2b",
            border_width=5,
            margin=5,
            opacity=0.75,
        ),
        # wallpaper="",
        # wallpaper_mode=""
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
