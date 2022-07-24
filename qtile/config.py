# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


# -- Start of Variables

mod = "mod4"
terminal = "alacritty"


# -- Start of Keybindings
keys = [
    Key([mod], "d", lazy.spawn("rofi -show combi"), desc="Rofi Menu"),
    Key([mod], "a", lazy.spawn("rofimoji -s neutral -a copy"), desc="Rofimoji"),
    Key([mod], 'w', lazy.next_screen(), desc='Next monitor'),
    Key([mod], 'e', lazy.next_screen(), desc='Previus monitor'),
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "j", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus up"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod], "l", lazy.layout.grow(), desc="Grow the Window"),
    Key([mod], "h", lazy.layout.shrink(),desc="Shrink the Window"),
    Key([mod], "n", lazy.layout.normalize(),desc="Normilize the Windw"),
    Key([mod], "o", lazy.layout.maximize(), desc="Maximize the Windw"),
    Key([mod, "shift"], "space", lazy.layout.flip(), desc="Flip the Monad-Layout"),
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "Return", lazy.spawn("alacritty -e vifm"),
        desc="Launch filebrowser"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"] ,"c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "l", lazy.spawn ("i3lock"), desc="lock the screen"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "0", lazy.spawn("xrandr --auto"),desc="xrandr Auto"),
    # Rofi Power Menu. Requires https://github.com/jluttine/rofi-power-menu
    Key([mod, "control"], "q",
        lazy.spawn("rofi -show power-menu -modi power-menu:rofi-power-menu"),
        desc="Rofi Power Menu"
    ),

    #XF86 Keys
    # Brightness Requires Brightnessctl
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%"),
        desc="Increase Screen Brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%- "),
        desc="Decrease Screen Brightness"),
    ## Volumen
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"),
        desc="Toggle Audio Mute"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-"),
        desc="Decrease Audio Volumen"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+"),
        desc="Increase Audio Volumen"),
    ## Audio Requires Playerctl
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"),desc="Play/Pause"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next Song"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previus Song"),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop"), desc="Stop Music"),


]


# -- Start of Workspaces
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# -- Start of Layouts

layouts = [
    layout.MonadTall(
        font = "Hack Nerd Font",
        fontsize = 12,
        margin = 8,
        border_focus = '#BF616A',
        ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# -- Start of Bars

widget_defaults = dict(
    font="Hack Nerd Font",
    fmt="{}",
    fontsize=14,
    padding=8,
    background="#2e3440",
)
extension_defaults = widget_defaults.copy()

screens = [
    # Monitor 0
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    hide_unused=True),
                widget.WindowCount(
                    foreground="#A3BE8C"),
                widget.Prompt(),
                widget.WindowName(
                    max_chars=25),
                widget.Notify(
                    background="#B48EAD",
                    default_timeout=5,
                    max_chars=25),
                widget.CPU(
                    background="#81A1C1"),
                widget.Memory(
                    background="#8FBCBB"),
                widget.Wttr(
                    location={'Düsseldorf':'Düsseldorf'},
                    format="%t(%f) | %C | %h",
                    background="#A3BE8C"
                ),
                widget.ThermalSensor(
                    show_tag=True,
                    fmt="CPU Temp:{}",
                    tag_sensor="Package id 0",
                    background="#EBCB8B"
                    ),
                widget.Clock(
                    format="%Y-%m-%d | %H:%M:%S",
                    background="#D08770"
                    ),
                widget.QuickExit(
                    default_text='[🔥]',
                    background="#BF616A"),
                widget.Volume(
                    emoji=True),
                widget.Systray(),
            ],
            30,
            opacity=0.90
        ),
    ),
    # Secondary Screen (xrandr --listmonitors)
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    hide_unused=True),
                widget.WindowCount(
                    foreground="#A3BE8C"),
                widget.Prompt(),
                widget.WindowName(
                    max_chars=25),
                widget.Notify(
                    background="#B48EAD",
                    default_timeout=25,
                    max_chars=25),
                widget.CPU(
                    background="#81A1C1"),
                widget.Memory(
                    background="#8FBCBB"),
                widget.Wttr(
                    location={'Düsseldorf':'Düsseldorf'},
                    format="%t(%f) | %C | %h",
                    background="#A3BE8C"
                ),
                widget.ThermalSensor(
                    show_tag=True,
                    fmt="CPU Temp:{}",
                    tag_sensor="Package id 0",
                    background="#EBCB8B"
                    ),
                widget.Clock(
                    format="%Y-%m-%d | %H:%M:%S",
                    background="#D08770"
                    ),
            ],
            30,
            opacity=0.90
        ),
    ),
]

# -- Start of Other
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
