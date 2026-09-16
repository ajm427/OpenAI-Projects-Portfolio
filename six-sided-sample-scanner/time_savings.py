"""Time-savings estimator for the Six-Sided Sample Scanner.

Edit the assumptions below to match the real intake workflow.
All time inputs are in seconds unless otherwise stated.
"""

# ---------------- EDITABLE ASSUMPTIONS ----------------
SAMPLES_PER_DAY = 100
WORK_DAYS_PER_YEAR = 250

# Current manual workflow: place/rotate/reposition sample and capture all needed views.
MANUAL_SECONDS_PER_SAMPLE = 60

# Proposed scanner workflow: place sample, trigger capture, remove sample.
SCANNER_SECONDS_PER_SAMPLE = 15

# Fully loaded or simple hourly labor rate used for cost estimates.
LABOR_COST_PER_HOUR = 25.00

# Optional prototype/build cost for estimating simple payback.
SCANNER_BUILD_COST = 500.00
# ------------------------------------------------------


def calculate_savings():
    seconds_saved_per_sample = MANUAL_SECONDS_PER_SAMPLE - SCANNER_SECONDS_PER_SAMPLE

    samples_per_year = SAMPLES_PER_DAY * WORK_DAYS_PER_YEAR
    seconds_saved_per_day = seconds_saved_per_sample * SAMPLES_PER_DAY
    seconds_saved_per_year = seconds_saved_per_sample * samples_per_year

    hours_saved_per_day = seconds_saved_per_day / 3600
    hours_saved_per_year = seconds_saved_per_year / 3600

    labor_savings_per_day = hours_saved_per_day * LABOR_COST_PER_HOUR
    labor_savings_per_year = hours_saved_per_year * LABOR_COST_PER_HOUR

    if labor_savings_per_day > 0:
        payback_work_days = SCANNER_BUILD_COST / labor_savings_per_day
    else:
        payback_work_days = float("inf")

    percent_time_reduction = (
        seconds_saved_per_sample / MANUAL_SECONDS_PER_SAMPLE * 100
        if MANUAL_SECONDS_PER_SAMPLE > 0
        else 0
    )

    return {
        "seconds_saved_per_sample": seconds_saved_per_sample,
        "percent_time_reduction": percent_time_reduction,
        "hours_saved_per_day": hours_saved_per_day,
        "hours_saved_per_year": hours_saved_per_year,
        "labor_savings_per_day": labor_savings_per_day,
        "labor_savings_per_year": labor_savings_per_year,
        "payback_work_days": payback_work_days,
    }


def main():
    r = calculate_savings()

    print("SIX-SIDED SAMPLE SCANNER — TIME SAVINGS")
    print("=" * 45)
    print(f"Samples/day:                 {SAMPLES_PER_DAY:,}")
    print(f"Manual time/sample:          {MANUAL_SECONDS_PER_SAMPLE:.1f} sec")
    print(f"Scanner time/sample:         {SCANNER_SECONDS_PER_SAMPLE:.1f} sec")
    print(f"Time saved/sample:           {r['seconds_saved_per_sample']:.1f} sec")
    print(f"Time reduction:              {r['percent_time_reduction']:.1f}%")
    print()
    print(f"Labor hours saved/day:       {r['hours_saved_per_day']:.2f}")
    print(f"Labor hours saved/year:      {r['hours_saved_per_year']:.1f}")
    print(f"Labor value saved/day:       ${r['labor_savings_per_day']:,.2f}")
    print(f"Labor value saved/year:      ${r['labor_savings_per_year']:,.2f}")

    if r["payback_work_days"] != float("inf"):
        print(f"Estimated build cost:        ${SCANNER_BUILD_COST:,.2f}")
        print(f"Simple payback:              {r['payback_work_days']:.1f} work days")


if __name__ == "__main__":
    main()
