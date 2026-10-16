from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI(title="ArcSafe Studio API", version="1.0.0", description="Educational power-system fault analysis workbench")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"])


def positive(**values):
    for name, value in values.items():
        if not math.isfinite(value) or value <= 0:
            raise HTTPException(status_code=422, detail=f"{name} must be a positive number")


@app.get("/")
def home():
    return {"message": "Welcome to ArcSafe Studio", "status": "Backend is running", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy", "app": "ArcSafe Studio"}

@app.post("/calculate-fault-current")
def calculate_fault_current(voltage: float, impedance: float):
    positive(voltage=voltage, impedance=impedance)
    return {"voltage_V": voltage, "impedance_ohm": impedance, "fault_current_A": round(voltage / impedance, 3), "formula": "I = V / Z"}

@app.post("/power-system-analysis")
def power_system_analysis(voltage: float, generator_impedance: float, transformer_impedance: float, line_impedance: float):
    positive(voltage=voltage, generator_impedance=generator_impedance, transformer_impedance=transformer_impedance, line_impedance=line_impedance)
    total = generator_impedance + transformer_impedance + line_impedance
    return {"voltage_V": voltage, "generator_impedance_ohm": generator_impedance, "transformer_impedance_ohm": transformer_impedance, "line_impedance_ohm": line_impedance, "total_impedance_ohm": round(total, 4), "estimated_fault_current_A": round(voltage / total, 3), "formula": "I = V / (Zg + Zt + Zline)"}

@app.post("/fault-analysis")
def fault_analysis(fault_type: str, voltage: float, z1: float, z2: float, z0: float, fault_impedance: float = 0.001):
    """Simplified sequence-network magnitude estimate. Not for protection design."""
    fault_type = fault_type.upper()
    if fault_type not in {"LG", "LL", "LLG", "3PH"}:
        raise HTTPException(status_code=422, detail="fault_type must be LG, LL, LLG, or 3PH")
    positive(voltage=voltage, z1=z1, z2=z2, z0=z0, fault_impedance=fault_impedance)
    # For a three-phase system, input voltage is line-to-line voltage.
    v_phase = voltage / math.sqrt(3)
    if fault_type == "3PH":
        i1 = v_phase / z1
        phase_current = i1
        ground_current = 0.0
        formula = "I3PH ≈ Vphase / Z1"
    elif fault_type == "LG":
        i0 = v_phase / (z1 + z2 + z0 + 3 * fault_impedance)
        phase_current = 3 * i0
        ground_current = phase_current
        formula = "ILG ≈ 3Vphase / (Z1 + Z2 + Z0 + 3Zf)"
    elif fault_type == "LL":
        phase_current = math.sqrt(3) * v_phase / (z1 + z2 + fault_impedance)
        ground_current = 0.0
        formula = "ILL ≈ √3 Vphase / (Z1 + Z2 + Zf)"
    else:
        z0g = z0 + 3 * fault_impedance
        parallel = (z2 * z0g) / (z2 + z0g)
        i1 = v_phase / (z1 + parallel)
        i0 = i1 * z2 / (z2 + z0g)
        phase_current = abs(i1 + i2_safe(i1, i0))
        ground_current = abs(3 * i0)
        formula = "LLG simplified sequence-network magnitude estimate"
    return {"fault_type": fault_type, "line_voltage_V": voltage, "phase_voltage_V": round(v_phase, 4), "estimated_fault_current_A": round(abs(phase_current), 3), "estimated_ground_current_A": round(ground_current, 3), "formula": formula, "assumption": "Positive real sequence-impedance magnitudes; simplified educational estimate only."}

def i2_safe(i1, i0):
    # Magnitude-only estimate; phase angles are not modelled.
    return max(0.0, i1 - i0)
