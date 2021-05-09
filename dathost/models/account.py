from datetime import datetime


class AccountModel:
    """Holds infomation around a account.

    Attributes
    ----------
    account_id : str
    email : str
    gravatar_url : str
    credits : str
    seconds_left : int
    time_left : int
    roles : str
    trial : bool
    accepted_terms_of_service_version : int
    subscription_pay_with_credits : bool
    affiliate : bool
    first_month_discount_percentage : float
    confirmed_at : datetime
    """

    def __init__(self, data: dict) -> None:
        self.account_id = data["id"]
        self.email = data["email"]
        self.gravatar_url = data["gravatar_url"]
        self.credits = data["credits"]
        self.seconds_left = data["seconds_left"]
        self.time_left = data["time_left"]
        self.roles = data["roles"]
        self.trial = data["trial"]
        self.accepted_terms_of_service_version = (
            data["accepted_terms_of_service_version"]
        )
        self.subscription_pay_with_credits = (
            data["subscription_pay_with_credits"]
        )
        self.affiliate = data["affiliate"]
        self.first_month_discount_percentage = (
            data["first_month_discount_percentage"]
        )
        self.confirmed_at = datetime.fromtimestamp(data["confirmed_at"])
