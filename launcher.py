from simple_term_menu import TerminalMenu 
from pathlib import Path 
import subprocess

def SNES_menu():
    rom_folder = Path("roms/snes")
    roms = list(rom_folder.glob("*.sfc"))
    roms+= list(rom_folder.glob("*.smc"))

    options = [rom.name for rom in roms]
    options.append("Back")

    menu = TerminalMenu(options)
    index = menu.show()

    if index is None:
        return
    selection = options[index]

    if selection == "Back":
        return
    rom_path = rom_folder / selection
    subprocess.run(["retroarch", "-L", "/usr/lib/aarch64-linux-gnu/libretro/snes9x_libretro.so", str(rom_path)])

def gameboy_menu():
    rom_folder = Path("roms/gb")
    roms = list(rom_folder.glob("*.gb"))

    options = [rom.name for rom in roms]
    options.append("Back")

    menu = TerminalMenu(options)
    index = menu.show()

    if index is None:
        return

    selection = options[index]

    if selection == "Back":
        return 

    rom_path = rom_folder / selection
    subprocess.run(["retroarch", "-L", "/usr/lib/aarch64-linux-gnu/libretro/gambatte_libretro.so", [str(rom_path)]])

def gameboycolor_menu():
    rom_folder = Path("roms/gbc")
    roms = list(rom_folder.glob("*.gbc"))

    options = [rom.name for rom in roms]
    options.append("Back")

    menu = TerminalMenu(options)
    index = menu.show()

    if index is None:
        return

    selection = options[index]

    if selection == "Back":
        return 

    rom_path = rom_folder / selection
    subprocess.run(["retroarch", "-L", "/usr/lib/aarch64-linux-gnu/libretro/gambatte_libretro.so", [str(rom_path)]])

def gameboyadvanced_menu():
    rom_folder = Path("roms/gba")
    roms = list(rom_folder.glob("*.gba"))

    options = [rom.name for rom in roms]
    options.append("Back")

    menu = TerminalMenu(options)
    index = menu.show()

    if index is None:
        return

    selection = options[index]
    
    if selection == "Back":
        return 
    
    rom_path = rom_folder / selection 
    subprocess.run(["retroarch", "-L", "/usr/lib/aarch64-linux-gnu/libretro/mgba_libretro.so", str(rom_path)])


def games_menu():
    options = [
        "Game Boy",
        "Game Boy Color",
        "Game Boy Advance",
        "SNES",
        "Back"
    ]

    menu = TerminalMenu(options)
    index = menu.show()

    if index is None:
        return

    selection = options[index]

    if selection == "Game Boy":
        gameboy_menu()
    elif selection == "Game Boy Color":
        gameboycolor_menu()
    elif selection == "Game Boy Advance":
        gameboyadvanced_menu()
    elif selection == "SNES":
        SNES_menu()
    elif selection == "Back":
        return


def launcher():
    while True:
        options = [
            "Games",
            "System",
            "Network",
            "Tools",
            "Exit"
        ]


        menu = TerminalMenu(options)
        print("Starting Menu")
        menu_entry = menu.show()

        if menu_entry is None:
            return

        selection = options[menu_entry]

        if selection == "Games":
            games_menu()
        elif selection == "System":
            pass
        elif selection == "Network":
            pass
        elif selection == "Tools":
            pass
        elif selection == "Exit":
            return

launcher()