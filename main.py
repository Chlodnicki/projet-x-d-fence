import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import os

class DefenseHandler(FileSystemEventHandler):
    def on_created(self, event):
        self.log_event("Création", event)

    def on_modified(self, event):
        self.logevent("Modification", event)

    def on_deleted(self, event):
        self.log_event("Suppression", event)

    def log_event(self, action, event):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ligne = f"[{timestamp}] {action} : {event.src_path}"
        print(ligne)
        with open("logs/events.log", "a") as log_file:
            log_file.write(ligne + "\n")

if __name__ == "__main__":
    dossier_a_surveiller = "./surveillance"
    os.makedirs("logs", exist_ok=True)

    event_handler = DefenseHandler()
    observer = Observer()
    observer.schedule(event_handler, path=dossier_a_surveiller, recursive=True)
    observer.start()

    print(f"Surverillance activée sur : {os.path.abspath(dossier_a_surveiller)}\nAppuie sur Ctrl+C pour arrêter.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nSurveillance arrêtée.")
    observer.join()