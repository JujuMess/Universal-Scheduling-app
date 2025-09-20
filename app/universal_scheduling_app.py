import openpyxl
import pandas as pd
import calendar


def normalise(text):
    print(f"initialising normalise for {text}")
    try: 
        isinstance(text, str)
        text.strip().lower().replace(" ", "_").replace("-", "_")
        print(text)
        return text
    except AttributeErrror:
        print()
        return text