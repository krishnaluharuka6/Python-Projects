from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "*** Take Rest ***",
            message = "rest leu, refresh feel hunxa",
            timeout = 5
        )
        time.sleep(10)