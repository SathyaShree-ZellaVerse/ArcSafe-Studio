# ⚡ ArcSafe Studio

### Electrical Power System Fault Analysis & Visualization

ArcSafe Studio is a web-based educational application designed to calculate fault current and perform basic power system fault analysis. It provides an interactive interface to explore electrical fault conditions and visualize calculation results.

## 🚀 Features

- **Fault Current Calculator** – Calculate estimated fault current using voltage and impedance.
- **Power System Analysis** – Analyze generator, transformer, and line impedance.
- **Fault Type Analysis** – Explore LG, LL, LLG, and three-phase (3PH) faults.
- **Interactive Visualization** – View power system diagrams and graphs.
- **Calculation History** – Review previous calculations in the browser.

## 🛠️ Technologies Used

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- NumPy
- SciPy
- NetworkX
- Plotly

## 💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SathyaShree-ZellaVerse/ArcSafe-Studio.git
cd ArcSafe-Studio
```



### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn numpy scipy networkx plotly
```

### 5. Start the backend

```bash
uvicorn main:app --reload
```

Open the API documentation at `http://127.0.0.1:8000/docs`.

Run the frontend using the included launcher files or a local web server, as configured in the project.

## 🎯 Project Objective

To provide an interactive educational tool for understanding electrical power system fault-current calculations and basic fault analysis.

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes only. Its simplified calculations have not been independently validated for real-world electrical protection or safety decisions. Do not use its results for equipment selection, protection coordination, or actual electrical installations.

## 👩‍💻 Developer

**B.E. Electrical and Electronics Engineering Student**

## 📌 Project Status

Educational prototype — further testing and technical validation are required.
