"""
Example script for testing. This adds a simple timer that has your
character make observations and notices at irregular intervals.

To test, use
  @script me = tutorial_examples.intrusivethoughts.IntrusiveThoughts

The script will only send messages to the object it is stored on, so
make sure to put it on yourself or you won't see any messages!

"""
import random
from evennia import DefaultScript


class IntrusiveThoughts(DefaultScript):
    """
    This class defines the script itself
    """

    def at_script_creation(self):
        self.key = "intrusivethoughts"
        self.desc = "Adds various timed mentations to a character."
        self.interval = 120  # seconds
        # self.repeats = 5  # repeat only a certain number of times
        self.start_delay = True  # wait self.interval until first call
        # self.persistent = True

    def at_repeat(self):
        """
        This gets called every self.interval seconds. We make
        a random check here so as to only return 33% of the time.
        """
        if random.random() < 0.66:
            # no message this time
            return
        self.send_random_message()

    def send_random_message(self):
        rand = random.random()
        # return a random message
        if rand < 0.1:
            string = "You look for your self, but find the group."
        elif rand < 0.2:
            string = "You look for the group, but find your self."
        elif rand < 0.3:
            string = (
                "You feel disconnected from your colleagues."
            )
        elif rand < 0.4:
            string = "You find yourself staring at the ground."
        elif rand < 0.5:
            string = "You wonder if your emotions are your own."
        elif rand < 0.6:
            string = "You scratch your head, looking around."
        elif rand < 0.7:
            string = "You blink, forgetting what it was you were going to do."
        elif rand < 0.8:
            string = "You feel unsettled all of a sudden."
        elif rand < 0.9:
            string = "You get a great idea. Of course, you won't tell anyone."
        else:
            string = "You suddenly feel lost in a familiar place."

        # echo the message to the object
        self.obj.msg(string)
