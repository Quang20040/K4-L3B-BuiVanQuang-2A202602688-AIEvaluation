"""Run interactive evaluation dashboard in the default web browser."""

import webbrowser
from pathlib import Path


def main() -> None:
    dashboard_path = Path(__file__).parent / "demo_dashboard.html"
    if dashboard_path.exists():
        print(f"Opening dashboard: {dashboard_path.resolve()}")
        webbrowser.open(dashboard_path.resolve().as_uri())
    else:
        print(f"Dashboard file not found: {dashboard_path}")


if __name__ == "__main__":
    main()
