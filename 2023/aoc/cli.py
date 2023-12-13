import click
import os
import time
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor

@click.command()
@click.option("--day", "-d", required=False, help="day to execute")
@click.option("--part", "-p", required=False, type=click.Choice(['1', '2']), help="day part to execute")
def cli(day: int | None, part: int | None) -> None:
    mods = get_modules()
    if not day:
        modules = {d: __import__(mod, fromlist=["object"]) for d, mod in mods.items()}
        res: dict[int, list[any]] = {}
        with ThreadPoolExecutor() as exec:
            results = [exec.submit(determine_execution, m, part) for d, m in modules.items()]
            for i in results:
                r = i.result()
                res[r[0]] = r
        keys = list(res.keys())
        keys.sort()
        s_res = {i: res[i] for i in keys}
        vals = [s_res[i] for i in s_res.keys()]
        print_results(vals)
    else:
        module = __import__(mods[int(day)], fromlist=["object"])
        print_results([determine_execution(module, part)])

def determine_execution(module, part: str | None) -> list[any]:
    if part != None:
        part = int(part)
    if part == 1:
        res1, elapsed1 = execute(module.part_one)
        return [module.day.day, module.day.title, res1, elapsed1, None, None]
    elif part == 2:
        res2, elapsed2 = execute(module.part_two)
        return [module.day.day, module.day.title, None, None, res2, elapsed2]
    else:
        res1, elapsed1 = execute(module.part_one)
        res2, elapsed2 = execute(module.part_two)
        return [module.day.day, module.day.title, res1, elapsed1, res2, elapsed2]

def execute(fn: callable) -> tuple[any, int]:
    start = time.perf_counter()
    res = fn()
    finish = time.perf_counter()
    timing = round(finish-start, 6)
    return res, timing

def print_results(data):
    print(tabulate(data, headers=["Day", "Title", "Part One Result", "Part One Elapsed","Part Two Result", "Part Two Elapsed"]))



def get_modules() -> dict[int,str]:
    days: list[str] = [folder for folder in os.listdir("aoc") if folder.startswith("day")]
    mods: dict[int,str] = {int(folder.replace("day", "")): f"aoc.{folder}.solution" for folder in days}
    return mods
