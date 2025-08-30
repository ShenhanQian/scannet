# derived from https://github.com/ScanNet/ScanNet/blob/master/SensReader/python/reader.py

import os, sys
import tyro
from pathlib import Path
from tqdm import tqdm

from SensorData import SensorData


def main(scannet_dir: Path):
    scene_folders = []
    base_folders = ['scans', 'scans_test']
    for base_folder in base_folders:
        for scene in os.listdir(os.path.join(scannet_dir, base_folder)):
            scene_folders.append((scannet_dir / base_folder / scene))

    for scene_folder in tqdm(scene_folders, desc="Scenes", unit="scene", leave=True):
        tqdm.write(f'Processing {scene_folder}...')
        extract_sens(scene_folder)

def extract_sens(scene_folder):
  scene = scene_folder.name
  sens_path = scene_folder / (scene + '.sens')
  assert sens_path.exists(), f"Sensor file {sens_path} does not exist"

  # load the data
  sd = SensorData(sens_path)
  sd.export_depth_images(scene_folder / 'depth')
  sd.export_color_images(scene_folder / 'color')
  sd.export_poses(scene_folder / 'pose')
  sd.export_intrinsics(scene_folder / 'intrinsic')
  sd.export_intrinsics(scene_folder / 'intrinsic')


if __name__ == '__main__':
    tyro.cli(main)