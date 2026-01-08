# CSS-Clamp-Calculator
A python css calculator for clamp values.

This project includes:
- a reusable calculation module
- a command line interface (CLI)
- a Streamlit web interface for interactive use

----------

## Why this exists
I built this to take the next step from creating a clamp value via excel to understand more python and to practice separating core logic from different user interfaces.

The same calculation logic powers both the CLI and the Streamlit app.

----------

## Features
- Calculates `clamp(min, PREFERRED, max)` values with real user input
- Input validation with clear error messages
- Clean formatting with configurable decimal precision
- CLI support for scripting and quick use
- Streamlit UI for interactive exploration

----------

## Project Structure
```text
CSS-Clamp-Calculator
 ├── clamp_calc.py
 ├── clamp_app.py #Streamlit UI
 └── README.md
```

----------

## Running the Streamlit app
```bash
pip install streamlit
streamlit run clamp_app.py
```

This will start a local web app at:
http://localhost:8501

----------

## Using the CLI
```bash
python clamp_calc.py --min 1 --max 2.5 --vw_min 400 --vw_max 1440
```

Optional flags: `--precision 4`

If any flags are omitted, the CLI will prompt for input interactively. Precision is optional and defaults to 3.

Example output: `clamp(1rem, 0.423rem + 2.308vw, 2.5rem)`

----------

## What I learned
- How to structure Python code for reuse across interfaces
- Using argparse for CLI tools
- Handling errors cleanly with raise and try/except
- Building lightweight web tools with Streamlit

----------

## Possible future improvements
- Copy to clipboard functionality in the Streamlit UI
- Visual preview of scaling behavior
- Preset viewport ranges (mobile, tablet, desktop)
- Packaging the calculator as a small Python module
