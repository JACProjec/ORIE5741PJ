import zstandard as zstd
import os
import json
import sys
from datetime import datetime
import logging.handlers

# Setup logger
log = logging.getLogger("bot")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

# Function to read and decode chunks from the .zst file
def read_and_decode(reader, chunk_size, max_window_size, previous_chunk=None, bytes_read=0):
    chunk = reader.read(chunk_size)
    bytes_read += chunk_size
    if previous_chunk is not None:
        chunk = previous_chunk + chunk
    try:
        return chunk.decode()
    except UnicodeDecodeError:
        if bytes_read > max_window_size:
            raise UnicodeError(f"Unable to decode frame after reading {bytes_read:,} bytes")
        log.info(f"Decoding error with {bytes_read:,} bytes, reading another chunk")
        return read_and_decode(reader, chunk_size, max_window_size, chunk, bytes_read)

# Function to read lines from the .zst file
def read_lines_zst(file_name):
    with open(file_name, 'rb') as file_handle:
        buffer = ''
        reader = zstd.ZstdDecompressor(max_window_size=2**31).stream_reader(file_handle)
        while True:
            chunk = read_and_decode(reader, 2**27, (2**29) * 2)
            if not chunk:
                break
            lines = (buffer + chunk).split("\n")
            for line in lines[:-1]:
                yield line
            buffer = lines[-1]
        reader.close()

if __name__ == "__main__":
    # The first command line argument is the path to the .zst file to process
    file_path = sys.argv[1]
    # Specify your output file name here
    output_file_path = "output.jsonl"
    
    # Initialize counters for logging
    file_lines = 0
    bad_lines = 0

    # Open the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Process each line in the .zst file
        for line in read_lines_zst(file_path):
            try:
                # Attempt to load the line as JSON to ensure it's valid
                obj = json.loads(line)
                # Write the valid JSON line to the output file
                output_file.write(line + '\n')
                file_lines += 1
            except (json.JSONDecodeError, ValueError) as e:
                # Log and count lines that could not be parsed as JSON
                bad_lines += 1
            # Optional: log progress every 100000 lines
            if file_lines % 100000 == 0:
                log.info(f"Processed {file_lines} lines, encountered {bad_lines} bad lines")

    # Log summary of the processing
    log.info(f"Complete: Processed {file_lines} lines in total, encountered {bad_lines} bad lines")
