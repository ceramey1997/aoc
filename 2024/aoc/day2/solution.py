from enum import Enum
from typing import Optional


class ReportDirection(Enum):
    INCREASING = 1
    DECREASING = 2


def get_fission_reports(filename: str) -> list[list[int]]:
    fission_reports: list[list[int]] = []
    file = open(filename, "r")
    while True:
        line = file.readline()
        if not line:
            break
        fission_reports.append([int(i) for i in line.split(" ")])
    return fission_reports


def is_fission_report_safe(report: list[int]) -> bool:
    direction = fission_report_direction(report)
    if not direction:
        return False
    return is_fission_report_slope(report, direction)


def is_fission_report_slope(report: list[int], direction: ReportDirection) -> bool:
    i = 0
    last_num = report[i]
    while True:
        i = i + 1
        if i >= len(report):
            return True
        if abs(report[i] - last_num) > 3 or abs(report[i] - last_num) < 1:
            return False
        if direction == ReportDirection.INCREASING:
            if report[i] < last_num:
                return False
        if direction == ReportDirection.DECREASING:
            if report[i] > last_num:
                return False
        last_num = report[i]


def fission_report_direction(report: list[int]) -> Optional[ReportDirection]:
    if report[0] > report[1]:
        return ReportDirection.DECREASING
    if report[0] < report[1]:
        return ReportDirection.INCREASING
    return None


def count_safe_reports(reports: list[list[int]]) -> int:
    safe_reports = 0
    for report in reports:
        if is_fission_report_safe(report):
            safe_reports = safe_reports + 1
    return safe_reports


fission_reports = get_fission_reports("input1.txt")
count_safe = count_safe_reports(fission_reports)

print(count_safe)
