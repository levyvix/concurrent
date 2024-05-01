from concurrent.futures import ThreadPoolExecutor
import time
from typer import Typer

app = Typer()


@app.command()
def eepy(seconds: int):
    time.sleep(seconds)

    print(f"i slept for {seconds} seconds!")


@app.command()
def super_eepy(seconds: int, workers: int):
    with ThreadPoolExecutor(workers) as pool:
        pool.map(eepy, [seconds, 1, 2, 3, 3])


if __name__ == "__main__":
    app()
