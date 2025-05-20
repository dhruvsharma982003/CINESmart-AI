import gzip
import shutil
from pathlib import Path

# Define file paths
input_path = Path("/mnt/data/314faceb-8f57-4b83-8fed-d57987a576f8.pkl")
output_path = input_path.with_suffix(".pkl.gz")

# Compress using gzip
with open(input_path, 'rb') as f_in:
    with gzip.open(output_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# Return compressed file path and size
output_path, output_path.stat().st_size / (1024 * 1024)  # Size in MB
