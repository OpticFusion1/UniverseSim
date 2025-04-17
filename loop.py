import time
from simulation import CosmicSimulation

RENDER_TIME = True
FPS = 60
UPS = 60

def game_loop():
    sim = CosmicSimulation()

    def update():
        sim.universe.update()

    def render():
        sim.universe.render()

    running = True
    initialTime = time.perf_counter_ns()
    timeU = 1_000_000_000 / UPS
    timeF = 1_000_000_000 / FPS
    deltaU = 0
    deltaF = 0
    frames = 0
    ticks = 0
    timer = int(time.time() * 1000)

    print("\nSimulation running. Press Ctrl+C to stop.\n")

    try:
        while running:
            currentTime = time.perf_counter_ns()
            deltaU += (currentTime - initialTime) / timeU
            deltaF += (currentTime - initialTime) / timeF
            initialTime = currentTime

            if deltaU >= 1:
                update()
                ticks += 1
                deltaU -= 1

            if deltaF >= 1:
                render()
                frames += 1
                deltaF -= 1

            if RENDER_TIME and (int(time.time() * 1000) - timer > 1000):
                print(f"[UPS: {ticks} | FPS: {frames}]")
                ticks = 0
                frames = 0
                timer += 1000
    except KeyboardInterrupt:
        print("\nSimulation ended by user.")