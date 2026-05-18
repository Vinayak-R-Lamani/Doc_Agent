from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
import time 


class ChageHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File modified: {event.src_path}") 
        
        

if __name__ == "__main__":
    path = "."  # Watch the current directory
    observer = Observer() 
    observer.schedule(ChageHandler(),path , recursive=True)
    observer.start()
    print(f"Watching for changes in {path}...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()