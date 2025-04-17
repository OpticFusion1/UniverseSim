import time

def main():
    universe_loop() # Perhaps throw this on a separate thread??

def universe_loop():
    RENDER_TIME = True # Determines if UPS & FPS should be logged
    FPS = 60
    UPS = 60
    # TODO: Improve this loop if possible.
    running = True
    initialTime = int(time.time() * 1000)
    timeU = 1000000000 / UPS
    timeF = 1000000000 / FPS
    deltaU = 0
    deltaF = 0
    frames = 0
    ticks = 0
    timer = int(time.time() * 1000)
    while running:
        currentTime = time.perf_counter_ns()
        deltaU += (currentTime - initialTime) / timeU
        deltaF += (currentTime - initialTime) / timeF
        initialTime = currentTime
        if (deltaU >= 1):
            update()
            ticks += 1
            deltaU -= 1
        if (deltaF >= 1):
            render()
            frames += 1
            deltaF -= 1
        if RENDER_TIME:
            if (int(time.time() * 1000) - timer > 1000):
                print(f"UPS: {ticks} FPS: {frames}")
        pass

def update():
    print("Update")

def render():
    print("Render")

if __name__ == "__main__":
    main()