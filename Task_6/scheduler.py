from retry import retry


class Scheduler:

    def __init__(self, platform, message):
        self.platform = platform
        self.message = message

    def schedule_message(self):
        for plat in self.platform:
            print(f"Scheduling message for: {plat.get_name}")
            if self.message_ack(plat):
                print(f"Message scheduled for: {plat.get_name}")
            else:
                print(f"Skipped schedule for: {plat.get_name}")

    def message_ack(self, plat):
        if plat.get_status == "Active":
            return True
        else:
            return False


class Platform:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    @property
    def get_name(self):
        return self.name

    @property
    def get_status(self):
        return self.status


class Message:
    def __init__(self, message):
        self.message = message
        self.status = "New"

    @property
    def get_message(self):
        return self.message

    def set_status(self):
        self.status = "Delivered"


def main():
    my_platform_list = [Platform("Mail", "Inactive"), Platform("Skype", "Active"), Platform("Slack", "Active"), Platform
    ("Discord", "Active")]
    msg = Message("This is a test")
    sched = Scheduler(my_platform_list, msg)
    sched.schedule_message()


if __name__ == "__main__":
    main()
