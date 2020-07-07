#!/usr/bin/env python3

boards = [
    {
        "id": "project_sero",
        "name": "Project Sero (SAMD)",
        "preset": {
            "di": 7,
            "ci": 8,
            "protocol": "serial",
            "bridge": "serial1_inverted",
            "bridge_button": 1,
            "bridge_reset": 2,
            "bridge_pin0": 0,
        },
        "pins": {
            0: "0 (A2)",
            1: "1~ (A0)",
            2: "2 (A1)",
            3: "3 (A3) (RX)",
            4: "4 (A4) (TX)",
            7: "7 (DI)",
            8: "8 (CI)",
            19: "19 (SWCLK)",
            20: "20 (SWDIO)",
        },
        "menu": {
            "keyboard": True,
            "debug": True,
        },
    },{
        "id": "trinket_m0",
        "name": "Adafruit Trinket M0 (SAMD21)",
        "preset": {
            "di": 7,
            "ci": 8,
        },
        "pins": {
            0: "0 (A2)",
            1: "1~ (A0)",
            2: "2 (A1)",
            3: "3 (A3) (RX)",
            4: "4 (A4) (TX)",
            7: "7 (DI)",
            8: "8 (CI)",
            19: "19 (SWCLK)",
            20: "20 (SWDIO)",
        },
        "menu": {
            "keyboard": True,
            "protocol": True,
            "debug": True,
            "bridge": True,
            "bridge_button": True,
            "bridge_reset": True,
            "bridge_pin0": True,
        },
    }
]

menus = {
    "keyboardid": "USB Device ID",
    "protocol": "Protocol",
    "debug": "Debug",
    "ledpin": "Neopixel (WS2812b)",
    "dipin": "Dotstar (APA102) DI Pin",
    "cipin": "Dotstar (APA102) CI Pin",
    "bridge": "Serial Bridge",
    "bridgebutton": "Serial Bridge Enable Pin",
    "bridgerst": "Serial Bridge Reset Pin",
    "bridge0": "Serial Bridge GPIO-0 Pin",
}

defaults = {
    "upload": {
        "tool": "bossac",
        "protocol": "sam-ba",
        "maximum_size": "262144",
        "offset": "0x2000",
        "use_1200bps_touch": "true",
        "wait_for_upload_port": "true",
        "native_usb": "true",
    },
    "bootloader": {
        "tool": "openocd",
        "file": "trinketm0/bootloader-trinket_m0-v2.0.0-adafruit.5.bin",
    },
    "build": {
        "mcu": "cortex-m0plus",
        "f_cpu": "48000000L",
        "board": "TRINKET_M0",
        "core": "arduino",
        "extra_flags": "-DCRYSTALLESS -DADAFRUIT_TRINKET_M0 -D__SAMD21E18A__ -DARM_MATH_CM0PLUS {build.usb_flags}",
        "ldscript": "linker_scripts/gcc/flash_with_bootloader.ld",
        "openocdscript": "openocd_scripts/trinket_m0.cfg",
    },
}

keyboards = {
    "default" : {
        "usb_manufacturer": "Adafruit",
        "usb_product": "Trinket M0",
        "vid": "0x239A",
        "pid": "0x801E",
    },
    "apple" : {
        "usb_manufacturer": "Apple",
        "usb_product": "Aluminium Keyboard",
        "vid": "0x05ac",
        "pid": "0x0221",
    },
    "appleint" : {
        "usb_manufacturer": "Apple",
        "usb_product": "Internal Keyboard/Trackpad",
        "vid": "0x05ac",
        "pid": "0x0259",
    },
    "logitechhid" : {
        "usb_manufacturer": "Logitech",
        "usb_product": "USB Keyboard",
        "vid": "0x046d",
        "pid": "0xc316",
    },
    "logitechgaming" : {
        "usb_manufacturer": "Logitech",
        "usb_product": "G910 Keyboard",
        "vid": "0x046d",
        "pid": "0xc335",
    },
    "ms" : {
        "usb_manufacturer": "Microsoft",
        "usb_product": "USB Keyboard",
        "vid": "0x045e",
        "pid": "0xfff8",
    },
}

protocols = {
    "auto": {
        "name": "Auto (I2C & Serial)",
        "flags": "-DENABLE_I2C -DENABLE_SERIAL",
    },
    "i2c": {
        "name": "I2C",
        "flags": "-DENABLE_I2C",
    },
    "serial": {
        "name": "Serial",
        "flags": "-DENABLE_SERIAL",
    },
}

debugs = {
    "serial": {
        "name": "Serial (115200b, newline)",
        "flags": "-DENABLE_DEBUG -DDEBUG_PORT=Serial -DDEBUG_BAUD=115200",
    },
    "disabled": {
        "name": "Disabled",
        "flags": "",
    },
}

bridges = {
    "disabled": {
        "name": "Disabled",
        "flags": "",
    },
    "serial1": {
        "name": "Serial1",
        "flags": "-DBRIDGE_ENABLE -DBRIDGE_PORT=Serial1",
    },
    "serial1_inverted": {
        "name": "Serial1 (inverted logic)",
        "flags": "-DBRIDGE_ENABLE -DBRIDGE_PORT=Serial1 -DBRIDGE_0_INVERTED",
    },
}

# Menus
def menu_names():
    print("########## Generated boards.txt ##########")
    print()

    for i in menus:
        print(f"menu.{i}={menus[i]}")
    print()

# Board Flags
def board_flags(id, name):
    print(f"########## {name} ##########")
    print()
    print(f"{id}.name={name}")
    print()

    print(f"{id}.build.variant={id}")

    for i in defaults:
        category = defaults[i]
        for j in category:
            print(f"{id}.{i}.{j}={category[j]}")
        print()
    print()

# Keyboard
def keyboard_menu(id):
    print("# Keyboard ID #")

    for i in keyboards:
        keyboard = keyboards[i]
        print(f"{id}.menu.keyboardid.{i}={keyboard['usb_manufacturer']} {keyboard['usb_product']}")
        print(f"{id}.menu.keyboardid.{i}.build.vid={keyboard['vid']}")
        print(f"{id}.menu.keyboardid.{i}.build.pid={keyboard['pid']}")
        print(f"{id}.menu.keyboardid.{i}.build.usb_product=\"{keyboard['usb_product']}\"")
        print(f"{id}.menu.keyboardid.{i}.build.usb_manufacturer=\"{keyboard['usb_manufacturer']}\"")
        print()

def keyboard_preset(id, value):
    print("# Keyboard ID #")

    keyboard = keyboards[value]
    print(f"{id}.build.vid={keyboard['vid']}")
    print(f"{id}.build.pid={keyboard['pid']}")
    print(f"{id}.build.usb_product={keyboard['usb_product']}")
    print(f"{id}.build.usb_manufacturer={keyboard['usb_manufacturer']}")
    print()

# Protocol
def protocol_menu(id):
    print("# Protocol #")

    for i in protocols:
        protocol = protocols[i]
        print(f"{id}.menu.protocol.{i}={protocol['name']}")
        print(f"{id}.menu.protocol.{i}.build.protocol_flags={protocol['flags']}")
        print()

def protocol_preset(id, value):
    print("# Protocol #")

    protocol = protocols[value]
    print(f"{id}.build.protocol_flags={protocol['flags']}")
    print()

# Debug
def debug_menu(id):
    print("# Debug #")

    for i in debugs:
        debug = debugs[i]
        print(f"{id}.menu.debug.{i}={debug['name']}")
        print(f"{id}.menu.debug.{i}.build.debug_flags={debug['flags']}")
        print()

def debug_preset(id, value):
    print("# Debug #")

    debug = debugs[value]
    print(f"{id}.build.debug_flags={debug['flags']}")
    print()

# Helper function for pin menus
def pin_menu(id, pins, category, flag, value, exceptions):
    print(f"{id}.menu.{category}.disabled=Disabled")

    for pin in pins:
        if pin not in exceptions:
            print(f"{id}.menu.{category}.{pin}={pins[pin]}")
            print(f"{id}.menu.{category}.{pin}.build.{flag}={value}={pin}")
    print()

def pin_preset(id, flag, value, preset):
    print(f"{id}.build.{flag}={value}={preset}")
    print()

# LED Neopixel
def led_menu(id, pins):
    print("# LED #")
    pin_menu(id, pins, "ledpin", "led_pin", "-DNEOPIXEL -DNEOPIXEL_NUM=1 -DLED_PIN", [])

def led_preset(id, value):
    print("# LED #")
    pin_preset(id, "led_pin", "-DNEOPIXEL -DNEOPIXEL_NUM=1 -DLED_PIN", value)

# LED Dotstar DI
def di_menu(id, pins):
    print("# Dotstar DI #")
    pin_menu(id, pins, "dipin", "di_pin", "-DDOTSTAR -DDOTSTAR_NUM=1 -DDOTSTAR_DI", [])

def di_preset(id, value):
    print("# Dotstar DI #")
    pin_preset(id, "di_pin", "-DDOTSTAR -DDOTSTAR_NUM=1 -DDOTSTAR_DI", value)

# LED Dotstar CI
def ci_menu(id, pins):
    print("# Dotstar CI #")
    pin_menu(id, pins, "cipin", "ci_pin", "-DDOTSTAR_CI", [])

def ci_preset(id, value):
    print("# Dotstar CI #")
    pin_preset(id, "ci_pin", "-DDOTSTAR_CI", value)

# Serial Bridge
def bridge_menu(id):
    print("# Serial Bridge #")
    
    for i in bridges:
        bridge = bridges[i]
        print(f"{id}.menu.bridge.{i}={bridge['name']}")
        print(f"{id}.menu.bridge.{i}.build.bridge_flags={bridge['flags']}")
        print()

def bridge_preset(id, value):
    print("# Serial Bridge #")
    
    bridge = bridges[value]
    print(f"{id}.build.bridge_flags={bridge['flags']}")
    print()

# Serial Bridge Button
def bridge_button_menu(id, pins):
    pin_menu(id, pins, "bridgebutton", "bridge_button", "-DBRIDGE_SWITCH", [])

def bridge_button_preset(id, value):
    pin_preset(id, "bridge_button", "-DBRIDGE_SWITCH", value)

# Serial Bridge Reset
def bridge_reset_menu(id, pins):
    pin_menu(id, pins, "bridgerst", "bridge_rst", "-DBRIDGE_RST", [])

def bridge_reset_preset(id, value):
    pin_preset(id, "bridge_rst", "-DBRIDGE_RST", value)

# Serial Bridge GPIO-0
def bridge_pin0_menu(id, pins):
    pin_menu(id, pins, "bridge0", "bridge_0", "-DBRIDGE_0", [])

def bridge_pin0_preset(id, value):
    pin_preset(id, "bridge_0", "-DBRIDGE_0", value)
    
menu_names()

for board in boards:
    board_flags(board['id'],board['name'])

    # Presets
    if "keyboard" in board["preset"]:
        keyboard_preset(board['id'], board["preset"]["keyboard"])

    if "protocol" in board["preset"]:
        protocol_preset(board['id'], board["preset"]["protocol"])
    
    if "debug" in board["preset"]:
        debug_preset(board['id'], board["preset"]["debug"])

    if "led" in board["preset"]:
        led_preset(board['id'], board["preset"]["led"])

    if "di" in board["preset"]:
        di_preset(board['id'], board["preset"]["di"])

    if "ci" in board["preset"]:
        ci_preset(board['id'], board["preset"]["ci"])

    if "bridge" in board["preset"]:
        bridge_preset(board['id'], board["preset"]["bridge"])
    
    if "bridge_button" in board["preset"]:
        bridge_button_preset(board['id'], board["preset"]["bridge_button"])

    if "bridge_reset" in board["preset"]:
        bridge_reset_preset(board['id'], board["preset"]["bridge_reset"])

    if "bridge_pin0" in board["preset"]:
        bridge_pin0_preset(board['id'], board["preset"]["bridge_pin0"])

    # Menus
    if "keyboard" in board["menu"]:
        keyboard_menu(board['id'])

    if "protocol" in board["menu"]:
        protocol_menu(board['id'])

    if "debug" in board["menu"]:
        debug_menu(board['id'])

    if "led" in board["menu"]:
        led_menu(board['id'], board["pins"])

    if "di" in board["menu"]:
        di_menu(board['id'], board["pins"])

    if "ci" in board["menu"]:
        led_menu(board['id'], board["pins"])

    if "bridge" in board["menu"]:
        bridge_menu(board['id'])

    if "bridge_button" in board["menu"]:
        bridge_button_menu(board['id'], board["pins"])

    if "bridge_reset" in board["menu"]:
        bridge_reset_menu(board['id'], board["pins"])

    if "bridge_pin0" in board["menu"]:
        bridge_pin0_menu(board['id'], board["pins"])