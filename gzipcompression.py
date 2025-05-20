import gzip
import shutil

input_file = "7b733783-f1b8-4ec6-966d-43800a4b0694.pkl"
output_file = "compressed_file.pkl.gz"

with open(input_file, 'rb') as f_in:
    with gzip.open(output_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
