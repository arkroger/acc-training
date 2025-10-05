
import json, sys, argparse

def lap_type(lp):
    t = (lp.get("type") or "").strip().lower()
    return t  # "regular", "outlap", "inlap"

def current_tyre_set(lp):
    tyre = lp.get("tyre") or {}
    s = tyre.get("currentTyreSet")
    try:
        return int(s) if s is not None else None
    except Exception:
        return None

def fuel_value(lp):
    ci = lp.get("carInfo") or {}
    f = ci.get("fuel")
    try:
        return float(f) if f is not None else None
    except Exception:
        return None

def to_unified(laps):
    if not isinstance(laps, list):
        raise ValueError("Input must be an array of lap objects")

    # Helper to build fresh stint
    def new_stint(stint_no:int, initial_tyre_set):
        return {
            "stint_no": stint_no,
            "tyre_set": initial_tyre_set if initial_tyre_set is not None else 1,
            "fuel_start_l": None,
            "fuel_end_l": None,
            "pressures_cold": None,
            "laps": []
        }

    # Meta inference (basic from first lap)
    first = laps[0] if laps else {}
    env = first.get("environment", {})
    meta = {
        "event": "<YYYY-MM-DD_track_event>",
        "track": "<track?>",
        "car": "<car?>",
        "game_version": "ACC",
        "condition": {
            "rubber": (first.get("trackGripStatus") or "Optimum").title() if first.get("trackGripStatus") else "Optimum",
            "weather": (env.get("rainIntensity") or "Dry"),
            "air_temp_c": float(env.get("airTemperature")) if env.get("airTemperature") is not None else None,
            "track_temp_c": float(env.get("roadTemperature")) if env.get("roadTemperature") is not None else None,
            "time_of_day": first.get("clock")
        },
        "traffic": "unknown",
        "notes": ""
    }

    # Iterate laps building stints by rules
    stints = []
    stint_no = 1
    last_tyre_set_seen = None
    current = new_stint(stint_no, current_tyre_set(first))

    def flush_current_if_nonempty():
        nonlocal current, stints
        if current and current["laps"]:
            # set fuel start/end
            fuels = [fuel_value(lp) for lp in current["laps"]]
            fuels = [f for f in fuels if f is not None]
            if fuels:
                current["fuel_start_l"] = fuels[0]
                current["fuel_end_l"] = fuels[-1]
            stints.append(current)

    for idx, lp in enumerate(laps):
        t = lap_type(lp)            # "regular"|"outlap"|"inlap"|""
        set_now = current_tyre_set(lp)
        if set_now is not None:
            last_tyre_set_seen = set_now

        # Rule 1: Outlap starts a NEW stint
        if t == "outlap":
            # close existing (if any content)
            flush_current_if_nonempty()
            stint_no += 1 if stints else (0 if not current["laps"] else 1)
            if stints and stints[-1]["stint_no"] == stint_no:  # safety
                stint_no += 1
            # create new, with tyre_set from this lap
            current = new_stint(stint_no if stints else 1 if not stints else stint_no, set_now)
            # add the outlap to the new stint
            mapped = map_lap(lp)
            current["laps"].append(mapped)
            current["tyre_set"] = set_now if set_now is not None else current["tyre_set"]
            continue

        # Rule 2: If tyre set changed (and NOT outlap/inlap), start NEW stint before this lap
        if t not in ("outlap", "inlap"):
            if set_now is not None and current["laps"]:
                first_set_of_current = current.get("tyre_set")
                # if current stint tyre set is unknown, adopt set_now once
                if first_set_of_current is None:
                    current["tyre_set"] = set_now
                elif set_now != first_set_of_current:
                    # Split: flush current, start new stint, then add this lap
                    flush_current_if_nonempty()
                    stint_no += 1 if stints else (1 if current["laps"] else 1)
                    current = new_stint(stint_no, set_now)

        # map and add the lap
        mapped = map_lap(lp)
        current["laps"].append(mapped)

        # Rule 3: Inlap ends the current stint (Inlap goes inside current stint)
        if t == "inlap":
            flush_current_if_nonempty()
            stint_no = (stints[-1]["stint_no"] if stints else stint_no)
            # prepare an empty container for a potential next stint
            current = new_stint(stint_no + 1, None)

    # flush last container
    flush_current_if_nonempty()

    # If no stint captured (e.g., empty input), ensure at least one empty stint
    if not stints:
        stints = [new_stint(1, None)]

    unified = {
        "meta": meta,
        "stints": stints
    }
    return unified

def map_lap(lp):
    time_obj = lp.get("time") or {}
    splits = lp.get("splits") or [None, None, None]
    def to_int(x):
        try:
            return int(x) if x is not None else None
        except Exception:
            return None
    return {
        "lap_no": to_int(lp.get("lap")),
        "valid": bool(lp.get("valid")),
        "lap_time_ms": to_int(time_obj.get("time")),
        "s1_ms": to_int(splits[0]) if len(splits) > 0 else None,
        "s2_ms": to_int(splits[1]) if len(splits) > 1 else None,
        "s3_ms": to_int(splits[2]) if len(splits) > 2 else None,
        "cuts": 0,
        "notes": lp.get("type")
    }

def main():
    ap = argparse.ArgumentParser(description="Convert flat-laps JSON to unified schema (meta+stints) with Outlap/Inlap and tyre-set rules.")
    ap.add_argument("input", help="input JSON file (array of laps)")
    ap.add_argument("output", help="output JSON file (unified schema)")
    args = ap.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    out = to_unified(data)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
