"""Install requirements for WD14-tagger."""
import os
import subprocess
import sys

from launch import run  # pylint: disable=import-error

NAME = "WD14-tagger"
req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        "requirements.txt")
print(f"loading {NAME} reqs from {req_file}")
run(f'"{sys.executable}" -m pip install -q -r "{req_file}"',
    f"Checking {NAME} requirements.",
    f"Couldn't install {NAME} requirements.")

# TensorFlow is optional for WD14 ONNX usage, but if installed together with
# Forge's pinned protobuf 4.x it can crash WebUI import in transformers.
# Default behavior: remove TensorFlow runtimes at install time.
# Set WD14_KEEP_TENSORFLOW=1 to opt out.
if os.environ.get("WD14_KEEP_TENSORFLOW", "0") != "1":
    print("Removing optional TensorFlow runtime packages for WD14-tagger stability.")
    subprocess.run(
        f'"{sys.executable}" -m pip uninstall -y '
        "tensorflow tensorflow-intel tensorflow-cpu tensorflow-io "
        "tensorflow-io-gcs-filesystem",
        shell=True,
        check=False,
    )
