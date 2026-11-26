"""Fetch LUMA's public outage numbers for the Mayagüez region and Rincón; write luma.json.

Runs on GitHub Actions (see .github/workflows/luma.yml). Uses LUMA's public MiLUMA
outage feed, the same data its outage map shows. No login or key involved.
"""
import json, os, sys, unicodedata, urllib.request
from datetime import datetime, timezone, timedelta

API = "https://api.miluma.lumapr.com/miluma-outage-api/outage"
UA = "Mozilla/5.0 (compatible; oeste-news outage check)"
OUT = os.path.join(os.path.dirname(__file__), "..", "luma.json")
FOCUS = ("PUEBLO", "ANGELICA", "COREA", "KOREA")

def norm(s):
    return unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().upper().strip()

def call(path, body=None):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(API + path, data=data, headers={
        "User-Agent": UA, "Accept": "application/json",
        **({"Content-Type": "application/json"} if data else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def now():
    return datetime.now(timezone(timedelta(hours=-4))).isoformat(timespec="minutes")

def main():
    try:
        prev = json.load(open(OUT))
    except Exception:
        prev = {}
    try:
        reg = call("/regionsWithoutService")
        may = next((r for r in reg.get("regions", []) if norm(r.get("name")) == "MAYAGUEZ"), None)
        if not may:
            raise ValueError("Mayagüez region missing from LUMA's response")
        towns = call("/municipality/towns", ["RINCON", "RINCÓN"])
        areas = []
        if isinstance(towns, dict):
            for k, v in towns.items():
                if norm(k) == "RINCON":
                    for a in v or []:
                        name = str(a.get("area") or "").strip()
                        if name and name not in [x["area"] for x in areas]:
                            areas.append({"area": name, "zone": a.get("zone") or "",
                                          "focus": any(f in norm(name) for f in FOCUS)})
        out = {
            "checked": now(), "ok": True, "error": None,
            "lumaTime": reg.get("timestamp"),
            "region": {
                "name": "Mayagüez",
                "total": may.get("totalClients"),
                "out": may.get("totalClientsWithoutService"),
                "planned": may.get("totalClientsAffectedByPlannedOutage"),
                "loadShed": may.get("totalClientsAffectedByLoadShed"),
                "pctOut": may.get("percentageClientsWithoutService"),
            },
            "rincon": areas,
        }
    except Exception as e:
        # Keep the last good numbers; record the failed attempt.
        out = {**prev, "ok": False, "error": f"{type(e).__name__}: {e}"[:300], "attempted": now()}
        print("LUMA check failed:", out["error"], file=sys.stderr)
    with open(OUT, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")

if __name__ == "__main__":
    main()
