from datetime import date, timedelta

class Subscription:
    def __init__(self, subscriber_name, subscription_type, start_date, duration_days):
        """
        Initialize a new subscription.

        Parameters:
        subscriber_name (str): The name of the subscriber.
        subscription_type (str): The type of subscription.
        start_date (date): The start date of the subscription.
        duration_days (int): The duration of the subscription in days.
        """
        self.subscriber_name = subscriber_name
        self.subscription_type = subscription_type
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=duration_days)
        self.active = False

    def activate(self):
        """Activate the subscription."""
        self.active = True
        print(f"Subscription for {self.subscriber_name} activated.")

    def deactivate(self):
        """Deactivate the subscription."""
        self.active = False
        print(f"Subscription for {self.subscriber_name} deactivated.")

    def is_active(self):
        """
        Check if the subscription is currently active.

        Returns:
        bool: True if the subscription is active, False otherwise.
        """
        today = date.today()
        return self.active and self.start_date <= today <= self.end_date

    def remaining_days(self):
        """
        Calculate the remaining days of the subscription.

        Returns:
        int: The number of days remaining in the subscription.
        """
        today = date.today()
        if today > self.end_date:
            return 0
        return (self.end_date - today).days

    def __str__(self):
        """Return a string representation of the subscription."""
        status = "active" if self.is_active() else "inactive"
        return (f"Subscription({self.subscriber_name}, {self.subscription_type}, "
                f"{self.start_date}, {self.end_date}, {status})")


# Example usage
if __name__ == "__main__":
    # Create a new subscription
    sub = Subscription("John Doe", "Premium", date(2024, 11, 25), 30)
    
    # Activate the subscription
    sub.activate()
    
    # Check if the subscription is active
    print(sub.is_active())  # Output: True

    # Get the remaining days of the subscription
    print(sub.remaining_days())  # Output will depend on the current date

    # Print the subscription details
    print(sub)  # Output: Subscription(John Doe, Premium, 2024-11-25, 2024-12-25, active)
