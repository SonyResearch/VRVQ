import os
from glob import glob

"""
Remove except folloing given conditions:
- given index_list
- given level_list
- given n_q list
- metadata.json
- input.wav
- input.png
"""

index_list_daps = [2, 3, 10, 14, 15, 21, 23, 27, 28]
nq_list_daps = [2, 4, 6, 8]
level_list_daps = [4.00, 6.40, 9.60, 16.00]


index_list_musdb = [6, 7, 9, 10, 17, 20, 21, 27]
nq_list_musdb = [2, 4, 6, 8]
level_list_musdb = [4.00, 6.40, 9.60, 16.00]
common_keep = ["metadata.json", "input.wav", "input.png"]

root_dir = './'
## Remove in CBR
mode = 'cbr'
dataset_list = ['daps', 'musdb18']
root_dirs = [
    "daps/cbr/",
    "musdb18/cbr/"
    "daps/vbr/",
    "musdb18/vbr/"
]
root_dirs_daps = [
    "daps/cbr/",
    "daps/vbr/"
]
root_dirs_musdb = [
    "musdb18/cbr/",
    "musdb18/vbr/"
]

def should_keep(file_name, nq_list, level_list):
    if file_name in common_keep:
        return True
    if file_name.startswith("recon_nq_"):
        for nq in nq_list:
            if file_name == f"recon_nq_{nq}.wav":
                return True
    if file_name.startswith("recon_"):
        for level in level_list:
            if file_name == f"recon_{level:.2f}.wav":
                return True
    if file_name.startswith("imp_map_"):
        for level in level_list:
            if file_name == f"imp_map_{level:.2f}.png":
                return True
    return False

total_idx = list(range(30))
import shutil
for root in root_dirs_daps:
    for idx in total_idx:
        if idx not in index_list_daps:
            path = os.path.join(root, f"{idx}")
            # path is directory
            if os.path.exists(path):
                print("Removing", path)
                shutil.rmtree(path)
        else:
            path = os.path.join(root, f"{idx}")
            if not os.path.exists(path):
                continue
            for file in os.listdir(path):
                if not should_keep(file, nq_list_daps, level_list_daps):
                    full_path = os.path.join(path, file)
                    print("Removing", full_path)
                    os.remove(full_path)

for root in root_dirs_musdb:
    for idx in total_idx:
        if idx not in index_list_musdb:
            path = os.path.join(root, f"{idx}")
            if os.path.exists(path):
                print("Removing", path)
                shutil.rmtree(path)
        else:
            path = os.path.join(root, f"{idx}")
            if not os.path.exists(path):
                continue
            for file in os.listdir(path):
                if not should_keep(file, nq_list_musdb, level_list_musdb):
                    full_path = os.path.join(path, file)
                    print("Removing", full_path)
                    os.remove(full_path)
