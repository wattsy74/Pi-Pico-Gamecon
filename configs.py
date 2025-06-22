import board
# color preset
RED = (255,  0,  0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 40, 0)
CYAN = (0, 250, 250)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
GREY = (30, 30, 30)
WHITE = (250, 250, 250) # better not to use
TEAL = (0, 255, 120)
PURPLE = (180, 0, 255)
MAGENTA = (255, 0, 20)
BLACK = (0, 0, 0) # black or off
GOLD = (255, 222, 30)
PINK = (242, 90, 255)
AQUA = (50, 255, 255)
JADE = (0, 255, 40)
AMBER = (255, 100, 0)

GREEN_FRET_COLOUR = GREEN
RED_FRET_COLOUR = RED
YELLOW_FRET_COLOUR = YELLOW
BLUE_FRET_COLOUR = BLUE
ORANGE_FRET_COLOUR = ORANGE
STRUM_UP_COLOUR = PURPLE
STRUM_DOWN_COLOUR = JADE

config = {
   # 4way Joystick pins
   # You can set NeoPixel LED index number with "~_led" parameter / comment out anything if you don't need LED
   "UP":board.GP2,
   #"UP_led": 0,
   "DOWN":board.GP3,
   #"DOWN_led": 0,
   "LEFT":board.GP4,
   #"LEFT_led": 0,
   "RIGHT":board.GP5,
   #"RIGHT_led": 0,
   # Buttons - up to 16
   # ['GREEN_FRET', 'RED_FRET', 'YELLOW_FRET', 'BLUE_FRET', 'ORANGE_FRET', 'STRUM_UP', 'STRUM_DOWN', 'TILT', 'SELECT', 'START', 'SB1', 'SB2', 'SB3', 'SB4', 'SB5', 'SB6']
   # You can set NeoPixel LED index number with "~_led" parameter :
   # comment out anything if you don't need
   "GREEN_FRET":board.GP6,
   "GREEN_FRET_led": 0,
   "RED_FRET":board.GP7,
   "RED_FRET_led": 1,
   "YELLOW_FRET":board.GP8,
   "YELLOW_FRET_led": 2,
   "BLUE_FRET":board.GP9,
   "BLUE_FRET_led": 3,
   "ORANGE_FRET":board.GP10,
   "ORANGE_FRET_led": 4,
   "STRUM_UP":board.GP11,
   "STRUM_UP_led": 5,
   "STRUM_DOWN":board.GP12,
   "STRUM_DOWN_led": 6,
   "TILT":board.GP13,
   #"TILT_led": 7,
   "SELECT":board.GP16,
   #"SELECT_led": 8,
   "START":board.GP17,
   #"START_led": 9,
   #"SB1":board.GP18,
   #"SB2":board.GP19,
   #"SB3":board.GP18,
   #"SB4":board.GP19,
   #"SB5":board.GP20,
   #"SB6":board.GP21,
   #"TURBO":board.GP20,
   #"MODE":board.GP21,
   # Pins for anlog input - should be ADC pin
   #"AnalogX":board.GP27,
   #"AnalogY":board.GP26,
   "WHAMMY":board.GP28,

   # NeoPixel - WS2812
   "neopixel_pin": board.GP0,
   # RGB LED Color, must set as many as LED lights you have
   "led_color": [GREEN_FRET_COLOUR, RED_FRET_COLOUR, YELLOW_FRET_COLOUR, BLUE_FRET_COLOUR, ORANGE_FRET_COLOUR, STRUM_UP_COLOUR, STRUM_DOWN_COLOUR ],
   # Default color for buttons with no assigned color
   "default_color":GREY,
   "led_brightness": 1, # 1 is maximum value
   "fadingstep" : 10, # Dimming speed - higher, faster
   "activetime" : 20, # Standby mode entry time(sec)

   # Defult DPAD mode - 'axis' or 'hat'
   "dpad_mode": "hat",
   # Turbo button speed (sec)
   "turbo_speed": 0.04,

}
