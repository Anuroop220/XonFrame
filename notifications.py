from pushbullet import Pushbullet
import threading
import time

API_KEY = "o.pPRmwHqV0JKV8qjro8NBSmkqNRzwp9KW"

def start_notifications(state):
    def listen():
        try:
            pb = Pushbullet(API_KEY)
            print("Pushbullet connected - waiting for notifications")
            
            # Track last seen push iden
            last_iden = None
            
            # Get current pushes to find the latest one
            existing = pb.get_pushes()
            if existing:
                last_iden = existing[0].get("iden")
            
            while True:
                try:
                    pushes = pb.get_pushes()
                    if pushes:
                        latest = pushes[0]
                        iden = latest.get("iden")
                        
                        # Only show if it's a new push
                        if iden != last_iden and latest.get("active"):
                            title = latest.get("title", "Notification")
                            body = latest.get("body", "")
                            msg = f"{title}: {body}" if title else body
                            state["notification"] = msg[:58]
                            print(f"New notification: {msg}")
                            last_iden = iden
                            
                            # Clear notification after 5 seconds
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