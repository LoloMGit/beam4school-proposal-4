#!/usr/bin/env python3
"""
generate_macros.py — Convert a student YAML request into Geant4 .mac files.

For each material × momentum combination, generates a macro file that:
  1. Sets the target material and thickness
  2. Sets the beam particle and momentum
  3. Runs the requested number of events
  4. Saves output to CSV

Usage:
  python generate_macros.py requests/myfile.yaml --output-dir simulation/macros/auto/
"""

import argparse
import os
import sys
import re

try:
    import yaml
except ImportError:
    os.system(f"{sys.executable} -m pip install pyyaml -q")
    import yaml


# Map student-friendly particle names to Geant4 names
PARTICLE_MAP = {
    "e-":     "e-",
    "e+":     "e+",
    "pi+":    "pi+",
    "pi-":    "pi-",
    "proton": "proton",
    "mu+":    "mu+",
    "mu-":    "mu-",
}


# Rest masses (MeV/c^2) for basic momentum→kinetic-energy conversion.
MASS_MEV = {
    "e-": 0.51099895,
    "e+": 0.51099895,
    "mu-": 105.6583755,
    "mu+": 105.6583755,
    "pi-": 139.57039,
    "pi+": 139.57039,
    "proton": 938.27208816,
}


def slugify(name: str) -> str:
    """Make a filesystem-safe identifier."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")


def momentum_to_kinetic_energy_MeV(p_MeV: float, particle: str) -> float:
    """Convert momentum (MeV/c) to kinetic energy (MeV) for the given particle."""
    m = MASS_MEV.get(particle)
    if m is None:
        # Fallback: treat as ultra-relativistic
        return p_MeV
    total_E = (p_MeV ** 2 + m ** 2) ** 0.5
    return total_E - m


def generate_macro(config, output_path):
    """Generate a single Geant4 macro file for one material × momentum."""
    particle = PARTICLE_MAP.get(config["particle"], config["particle"])
    p_GeV = config["momentum_GeV"]
    p_MeV = p_GeV * 1000.0
    kin_MeV = momentum_to_kinetic_energy_MeV(p_MeV, particle)

    mac = f"""# ═══════════════════════════════════════════════════════════════
# Auto-generated BeamScan macro
# Material: {config['material_name']} ({config['geant4_name']})
# Momentum: {p_GeV} GeV/c
# Thickness: {config['thickness_mm']} mm
# Events: {config['num_events']}
# ═══════════════════════════════════════════════════════════════

# Verbosity
/control/verbose 0
/run/verbose 0
/event/verbose 0
/tracking/verbose 0

# Target configuration
/beamscan/target/material {config['geant4_name']}
/beamscan/target/thickness {config['thickness_mm']} mm

# Initialize geometry
/run/initialize

# Beam configuration
/gun/particle {particle}
/gun/energy {kin_MeV:.6f} MeV
/gun/direction 0 0 1
/gun/position 0 0 -80 cm

# Output file
/beamscan/output/filename {config['output_csv']}

# Run
/run/beamOn {config['num_events']}
"""
    with open(output_path, 'w') as f:
        f.write(mac)
    return output_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("request_file", help="Path to YAML request file")
    parser.add_argument("--output-dir", default="simulation/macros/auto", help="Output directory")
    parser.add_argument("--results-dir", default="results/geant4", help="Where Geant4 CSV output goes")
    parser.add_argument("--events-per-config", type=int, default=0,
                        help="Override events per (material × momentum). 0 = use YAML value")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs(args.results_dir, exist_ok=True)

    with open(args.request_file) as f:
        req = yaml.safe_load(f)

    macros = []
    for mat in req["materials"]:
        for p in req["beam"]["momenta_GeV"]:
            safe_name = f"{slugify(mat['name'])}_{p:.1f}GeV_{float(mat['thickness_mm']):.1f}mm"
            output_csv = os.path.join(args.results_dir, safe_name, "events.csv")
            os.makedirs(os.path.dirname(output_csv), exist_ok=True)

            config = {
                "material_name": mat["name"],
                "geant4_name": mat["geant4_name"],
                "thickness_mm": mat["thickness_mm"],
                "momentum_GeV": p,
                "particle": req["beam"].get("particle", "e-"),
                "num_events": (args.events_per_config if args.events_per_config > 0
                               else req["beam"].get("num_events", 10000)),
                "output_csv": output_csv,
            }

            mac_path = os.path.join(args.output_dir, f"{safe_name}.mac")
            generate_macro(config, mac_path)
            macros.append(mac_path)
            print(f"  ✅ {mac_path}")

    # Write a run-all script
    run_all = os.path.join(args.output_dir, "run_all.sh")
    with open(run_all, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("set -e\n")
        f.write("# Auto-generated: run all Geant4 simulations\n")
        f.write(f"# From request: {args.request_file}\n\n")
        f.write('BEAMSCAN="${BEAMSCAN_BIN:-./build/beamscan}"\n\n')
        for mac in macros:
            f.write(f'echo "Running {os.path.basename(mac)}..."\n')
            f.write(f'"$BEAMSCAN" -m "{mac}"\n\n')
        f.write('echo "All simulations complete."\n')
    os.chmod(run_all, 0o755)
    print(f"\n  📋 Run script: {run_all}")
    print(f"  Total macros: {len(macros)}")


if __name__ == "__main__":
    main()
