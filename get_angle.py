""""This class calculated the angle between hour hands and minute hands"""

# from  google.cloud import logging
# import google.cloud.logging

# client = google.cloud.logging.Client()
# logger = client.logger('log_clock_angle')


class Angle: # pylint: disable=too-few-public-methods
    """"
    This class calculated the angle between hour hands and minute hands
    """
    def __init__(self, hour=None, minute=None):
        """"Init method"""
        self.hour = hour
        self.minute = minute

    def calculate_angle(self):
        """"validate the input"""
        if self.hour < 0 or self.minute < 0 or self.hour > 12 or self.minute > 60:
            # logger.log_text('Wrong input')
            return {"response":"wrong input"}

        if self.hour == 12:
            self.hour = 0
        if self.minute == 60:
            self.minute = 0

        # Calculate the angles moved by
        # hour and minute hands with
        # reference to 12:00
        hour_angle = 0.5 * (self.hour * 60 + self.minute)
        minute_angle = 6 * self.minute

        # Find the difference between two angles
        angle = abs(hour_angle - minute_angle)

        # Return the smaller angle of two
        # possible angles
        angle = min(360 - angle, angle)

        return {"response" : str(angle)}


# if __name__ == '__main__':
#
#     h = 3
#     m = 00
#     a = Angle(h, m)
#     f = a.calculate_angle()
#     print('Angle ', f)
#
