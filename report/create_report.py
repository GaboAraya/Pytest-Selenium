import datetime
import os
import stat
import subprocess
import sys
from pathlib import Path

allure_exec = "allure.bat" if sys.platform == "win32" else "allure"
allure_path = Path(f"report/allure-2.28.0/bin/{allure_exec}")
allure_results = Path("report/temp/allure-results")
allure_report_name = f"allure-report-{datetime.datetime.now().strftime('%m-%d-%Y-%H_%M_%S')}"
allure_output_report = Path(f"report/reports/{allure_report_name}")

if not os.access(allure_path, os.X_OK):
    st = os.stat(allure_path)
    os.chmod(allure_path, st.st_mode | stat.S_IEXEC)

command = (f"{allure_path} "
           f"generate {allure_results} "
           f"-c --single-file "
           f"-o {allure_output_report}")

subprocess.run(command, capture_output=True, check=True, timeout=120, shell=True)
