import multiprocessing
import os
import subprocess
import logging

logging.basicConfig(filename="sample.log", format='%(message)s', level=logging.INFO)

dir_v = 'C:\\Users\\gerku\\Downloads\\dir1'
dir_a = 'C:\\Users\\gerku\\Downloads\\dir2'
dir_f = 'C:\\Users\\gerku\\Downloads\\finish'

vids_path = [os.path.join(dir_v, name) for name in os.listdir(dir_v)]
auds_path = [os.path.join(dir_a, name) for name in os.listdir(dir_a)]

logging.info(auds_path)


def merge(i):
    subprocess.call(
        [
            'ffmpeg', '-hide_banner',
            '-i', vids_path[i], '-i', auds_path[i],
            '-map', '0:v:0', '-c:v', 'copy', '-map', '1:a', '-c:a', 'copy',
            f'{dir_f}\\vid{i + 6}.mkv'
        ]
    )

for i in range(6):
    merge(i)
