
class MonitorPrints:

    @staticmethod
    def start_screen():
        print()
        print("This is program start screen.")
        print()

    @staticmethod
    def help_section():
        print()
        print("print help (monitor)")
        print()

    @staticmethod
    def quit_message():
        print()
        print("Thank your choosing this app.")
        print()

    @staticmethod
    def wrong_input():
        print()
        print("wrong command entered (Monitor)")
        print()

class CommandHandlerPrints:

    @staticmethod
    def help_section():
        print()
        print("print help (Command Handler)")
        print()

    @staticmethod
    def wrong_input():
        print()
        print("wrong command entered (Command Handler)")
        print()

    @staticmethod
    def quit_error():
        print()
        print("cannot quit without closing running thread")
        print()

    @staticmethod
    def stop_error():
        print()
        print("there is no working thread to be stopped")
        print()

    @staticmethod
    def start_error():
        print()
        print("cannot start a new thread without closing running one")
        print()