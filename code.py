# Get settings from TOML file.
# https://github.com/elpekenin/circuitpython_toml
import toml
SETTINGS_FN = "settings.toml"
config = None
with open(SETTINGS_FN, "r") as config_f:
    config = toml.load(config_f)
BOARD_ID = config["board_id"]
print(f"Got board ID: {BOARD_ID}")

# Run the code for the board that we are on.
board = None
if BOARD_ID == "main":
    from board_main import MainBoard
    board = MainBoard()
elif BOARD_ID == "remote":
    from board_remote import RemoteBoard
    board = RemoteBoard()
elif BOARD_ID == "safety":
    from board_safety import SafetyBoard
    board = SafetyBoard()

else:
    raise ValueError(f"Unknown board ID from {SETTINGS_FN}: {BOARD_ID}")

board.main_loop()

print("If this line prints, the board's main_loop() has finished.")
