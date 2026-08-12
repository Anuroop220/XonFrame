import os
import threading
import time
from dotenv import load_dotenv
from pushbullet import Pushbullet

load_dotenv()
API_KEY = os.environ.get("PUSHBULLET_API_KEY")


def start_notifications(state):
    def listen():
        if not API_KEY:
            print("PUSHBULLET_API_KEY not set — add it to your .env file. Notifications disabled.")
            return
        try:
            pb = Pushbullet(API_KEY)
            print("Pushbullet connected - waiting for notifications")

            last_iden = None
            existing = pb.get_pushes()
            if existing:
                last_iden = existing[0].get("iden")

            while True:
                try:
                    pushes = pb.get_pushes()
                    if pushes:
                        latest = pushes[0]
                        iden = latest.get("iden")
                        if iden != last_iden and latest.get("active"):
                            title = latest.get("title", "Notification")
                            body = latest.get("body", "")
                            msg = f"{title}: {body}" if title else body
                            state["notification"] = msg[:58]
                            print(f"New notification: {msg}")
                            last_iden = iden

                            def clear():
                                time.sleep(5)
                                state["notification"] = ""
                            threading.Thread(target=clear, daemon=True).start()

                except Exception as e:
                    print(f"Notification error: {e}")
                time.sleep(3)
        except Exception as e:
            print(f"Pushbullet error: {e}")

    t = threading.Thread(target=listen, daemon=True)
    t.start()
