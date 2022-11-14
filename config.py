import os
import subprocess
from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "l", lazy.widget["keyboardlayout"].next_keyboard(), desc="Keyboard layout"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),   
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "Escape", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "Escape", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "mod1"], "Right", lazy.window.toscreen(1)),
    Key([mod, "mod1"], "Left", lazy.window.toscreen(0)),
    Key([mod], "r", lazy.spawn("rofi -show drun")),
]

layouts = [
    layout.Max(),
    layout.Stack(),
    layout.MonadWide(),
    layout.Tile(),
]

widget_defaults = dict(
    font="sans",
    fontsize=14,
    padding=4,
)
extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        wallpaper='~/.config/qtile/BG2.png',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.Clock(format="%H:%M",background='#8a508f44'),
                widget.Prompt(background='#00202e44'),
                widget.TaskList(background='#003f5c44'),
                widget.Systray(background='#2c487544'),
                widget.PulseVolume(emoji=True,background='#bc509044'),
                widget.KeyboardLayout(configured_keyboards=['fr','us'],background='#ff636144'),
                widget.LaunchBar(background="#ff853144",text_only=True,progs=[
                    ('\uf011','shutdown -P now','Poweroff computer'),('\uf2f1','shutdown -r now','Reboot computer'),('\uf08b','qshell:self.qtile.shutdown()','Log out from Qtile')]),
            ],
            32,
            margin=[0,15,0,15],
            background='#00000088',
        ),
    ),
    Screen(
        wallpaper='~/.config/qtile/BG2.png',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.Clock(format="%H:%M",background='#8a508f44'),
                widget.Prompt(background='#00202e44'),
                widget.TaskList(background='#003f5c44'),
                widget.Systray(background='#2c487544'),
                widget.PulseVolume(emoji=True,background='#bc509044'),
                widget.KeyboardLayout(configured_keyboards=['fr','us'],background='#ff636144'),
                widget.LaunchBar(background="#ff853144",text_only=True,progs=[
                    ('\uf011','shutdown -P now','Poweroff computer'),('\uf2f1','shutdown -r now','Reboot computer'),('\uf08b','qshell:self.qtile.shutdown()','Log out from Qtile')]),
            ],
            32,
            margin=[0,15,0,15],
            background='#00000088',
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

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
