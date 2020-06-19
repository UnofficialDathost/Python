class AccountModel:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.gravatar_url = data["gravatar_url"]
        self.credits = data["credits"]
        self.seconds_left = data["seconds_left"]
        self.time_left = data["time_left"]
        self.roles = data["roles"]
        self.trial = data["trial"]
