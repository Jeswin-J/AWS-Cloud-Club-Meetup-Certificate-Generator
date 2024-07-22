# Bulk Certificate Generator

This Python project generates personalized certificates for event attendees. It uses `pandas` to read attendee data from a CSV file and `reportlab` to create overlay text on a PDF certificate template. The final certificates are saved as individual PDF files.


## Features

- Reads attendee names from a `attendees.csv` file in `Input` directory.
- Creates personalized certificates using a template in `Template` directory.
- Saves each certificate as a separate PDF file in `Output` directory.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)
