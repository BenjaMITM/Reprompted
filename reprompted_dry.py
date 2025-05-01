# Reprompted
from reprompted.lib.shared import Reprompted

# Main Object
Reprompted = Reprompted()

def do_reprompted(string):
    # Reset vars
    Reprompted.shortcode_user_vars = {}

    Reprompted.log(Reprompted.process_string(string),False,"RESULT")

    # CLEANUP ROUTINES
    Reprompted.log("Entering cleanup routine...", False)
    for i in Reprompted.cleanup_routines:
        Reprompted.shortcode_objects[i].cleanup()

while True:
    try:
            command = input("(INPUT) Unprompted String:")
            do_reprompted(command)
    except ValueError: print("ValueError occured.")