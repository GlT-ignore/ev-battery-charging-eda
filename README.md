# EV Battery Charging EDA

Reproducible analysis for the exploratory study of 1,000 EV charging sessions.

## Structure
- **data/** – raw and cleaned CSV files  
- **figures/** – PNG graphics used in the LaTeX report  
- **scripts/** – standalone Python to regenerate figures  
- **report/** – LaTeX source (`ev_battery_report.tex`)  
- **environment/** – `requirements.txt` for pip/venv  

## Quick start

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate
pip install -r environment/requirements.txt

python scripts/generate_figures.py data/ev_battery_charging_data.csv
cd report && pdflatex ev_battery_report.tex
```