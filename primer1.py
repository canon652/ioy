import time


ESC = "\x1b"
CSI = f"{ESC}["


def loading():
    print("loading...")
    for i in range(100):
        print(f"{CSI}1G(i+1)%", end="",flush=True)
        time.sleep(0.2)

def show_progress(num_task, widht):
    for task in range(num_task):
        for filled in range(0,widht):
            bar = f"{'#' * filled}{'_' * (widht - filled - 1)}"
            print(f"{CSI}1G{task}/{num_task}{bar}",
                  end="",
                  flush=True)
            time.sleep(0.2)



if __name__ == "__main__": #основной сценарий
    show_progress(3)
    print()