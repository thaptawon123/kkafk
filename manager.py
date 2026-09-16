import os
import subprocess
import time

FOLDERS = ["1", "2", "3", "4", "5", "6"]


def main():
  print("=== Starting MCC AFK Manager (With Logging) ===")

  for i, folder in enumerate(FOLDERS):
    if i > 0:
      print(f"-> Waiting 120 seconds before starting folder {folder}...")
      time.sleep(120)

    script_path = os.path.join(folder, "run.py")
    if os.path.exists(script_path):
      print(f"-> Launching instance in folder: {folder}")
      try:
        # สร้างและเขียน Log ลงในไฟล์ bot.log ประจำแต่ละโฟลเดอร์
        log_path = os.path.join(folder, "bot.log")
        log_file = open(log_path, "w")
        subprocess.Popen(
            ["python3", "run.py"], cwd=folder, stdout=log_file, stderr=log_file
        )
      except Exception as e:
        print(f"Error starting {folder}: {e}")
    else:
      print(f"-> Script not found in folder {folder}")

  print("=== All instances launched successfully ===")


if __name__ == "__main__":
  main()
