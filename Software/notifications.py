import os
import threading
import time
from pathlib import Path

from dotenv import load_dotenv
from pushbullet import Pushbullet


load_dotenv(Path(__file__).resolve().parent / ".env")
api_key = os.getenv("PUSHBULLET_API_KEY")


def start_notifications(state):
    notification_number = 0

    def clear_notification(number):
        time.sleep(5)

        if number == notification_number:
            state["notification"] = ""

    def listen():
        nonlocal notification_number

        if not api_key:
            print("PUSHBULLET_API_KEY is missing. Notifications are disabled.")
            return

        try:
            pushbullet = Pushbullet(api_key)
            print("Pushbullet connected - waiting for notifications")

            pushes = pushbullet.get_pushes()
            last_iden = pushes[0].get("iden") if pushes else None

            while True:
                try:
                    pushes = pushbullet.get_pushes()

                    if pushes:
                        latest = pushes[0]
                        iden = latest.get("iden")

                        if iden != last_iden and latest.get("active"):
                            title = latest.get("title") or "Notification"
                            body = latest.get("body") or ""
                            message = f"{title}: {body}"

                            state["notification"] = message[:58]
                            print(f"New notification: {message}")

                            last_iden = iden
                            notification_number += 1

                            threading.Thread(
                                target=clear_notification,
                                args=(notification_number,),
                                daemon=True,
                            ).start()

                except Exception as error:
                    print(f"Notification error: {error}")

                time.sleep(3)

        except Exception as error:
            print(f"Pushbullet error: {error}")

    threading.Thread(target=listen, daemon=True).start()