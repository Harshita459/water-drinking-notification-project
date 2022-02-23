#step1: import our module.
#step2: pass a notification.
#step3:  run the python program in background.
#step1:

from plyer import notification
import time
if  __name__ == "__main__":
#step2:

    notification.notify(
        title = "Please Drink Water!",
        message = "Drinking Water Increases Energy & Relieves Fatigue.",
        app_icon = "D:\\reminder notification project\\icon.ico",
        timeout = 12
    )
    time.sleep(1800)