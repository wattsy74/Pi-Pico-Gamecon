import usb_hid
import usb_midi
import storage
import board
import digitalio
import supervisor

GAMEPAD_REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,  # Usage Page (Generic Desktop Ctrls)
    0x09, 0x05,  # Usage (Game Pad)
    0xA1, 0x01,  # Collection (Application)
    0x85, 0x05,  #   Report ID (5)
    0x05, 0x09,  #   Usage Page (Button)
    0x19, 0x01,  #   Usage Minimum (Button 1)
    0x29, 0x10,  #   Usage Maximum (Button 16)
    0x15, 0x00,  #   Logical Minimum (0)
    0x25, 0x01,  #   Logical Maximum (1)
    0x75, 0x01,  #   Report Size (1)
    0x95, 0x10,  #   Report Count (16)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0x05, 0x01,  #   Usage Page (Generic Desktop Ctrls)
    0x15, 0x00,  #   Logical Minimum (0)
    0x26, 0xFE, 0x00, #   Logical Maximum (254)
    0x09, 0x30,  #   Usage (X)
    0x09, 0x31,  #   Usage (Y)
    0x09, 0x32,  #   Usage (Z)
    0x09, 0x35,  #   Usage (Rz)
    0x75, 0x08,  #   Report Size (8)
    0x95, 0x04,  #   Report Count (4)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0x09, 0x39,  #   Usage (Hat switch)
    0x15, 0x00,  #   Logical Minimum (0)
    0x25, 0x07,  #   Logical Maximum (7)
    0x35, 0x00,  #   Physical Minimum (0)
    0x46, 0x3B, 0x01,  #    Physical Maximum(315)
    0x65, 0x14,  #   Unit (Eng Rot:Angular Pos)
    0x75, 0x04,  #   Report Size (4)
    0x95, 0x01,  #   Report Count (1)
    0x81, 0x42,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,Null State)
    0x65, 0x00,  #   Unit (None)
    0x95, 0x01,  #   Report Count (1)
    0x81, 0x01,  #   Input (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position)
    # PS3?
    0x06, 0x00, 0xff,  #   Usage Page (Vendor Specific)
    0x09, 0x20,  #   Unknown
    0x75, 0x08,  #   Report Size (8)
    0x95, 0x01,  #   Report Count (1)
    0xB1, 0x02,  #   Feature (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position,Non-volatile)
    0xC0,        # End Collection
))

gamepad = usb_hid.Device(
    report_descriptor=GAMEPAD_REPORT_DESCRIPTOR,
    usage_page=0x01,           # Generic Desktop Control
    usage=0x05,                # Gamepad
    report_ids=(5,),           # Descriptor uses report ID 5.
    in_report_lengths=(7,),    # This gamepad sends 7 bytes in its report.
    out_report_lengths=(0,),   # It does not receive any reports.
)

supervisor.set_usb_identification(manufacturer='BumbleGum', product='CH-Guitar', vid=0x6997, pid=0x0001)
usb_hid.set_interface_name("BumbleGum Guitars - NAME")
usb_hid.enable((gamepad,))
usb_midi.disable()

button = digitalio.DigitalInOut(board.GP6) # GREEN FRET
button.switch_to_input(pull=digitalio.Pull.UP)

if button.value:
    storage.disable_usb_drive()    # Hide drive
    usb_cdc.disable()              # REPL off
