from time import sleep, time

from python_imagesearch.imagesearch import imagesearch, imagesearch_loop, imagesearch_numLoop
import mouse
import psutil

PIXEL_TO_CLICK = 15


def is_process_running(process_name):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


start = time()

while 1:
    if is_process_running('League of Legends.exe'):
        print(f"[{time() - start} s] Found League Of Legends.exe. Quitting.")
        exit()
    pos = imagesearch("C:/Users/W/PycharmProjects/lol_aceept_queue/accept_only.png", .6)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        print(mouse.get_position())
        mouse.move(pos[0] - 3840 + PIXEL_TO_CLICK, pos[1] - 670 + PIXEL_TO_CLICK, absolute=True, duration=0)
        mouse.click()
        mouse.move(0, 0)
        sleep(6)

    else:
        print(f"[{time() - start} s] League Accept Queue Not Found")
