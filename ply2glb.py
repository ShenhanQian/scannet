import subprocess  # Better than os.system for capturing output
from pathlib import Path
import tyro
from tqdm import tqdm


def main(
    root_folder: Path,
    output_folder: Path,
) -> None:
    # get all folders in the root folder
    scenes = sorted([x.name for x in root_folder.iterdir() if x.is_dir()])
    print(f"Found {len(scenes)} scenes in {root_folder}")

    for scene in tqdm(scenes):
        # tqdm.write(f"Processing {scene}")

        output_folder.mkdir(exist_ok=True)
        tmp_path = output_folder /f"{scene}.tmp.glb"
        glb_path = output_folder /f"{scene}.glb"
        if glb_path.exists():
            continue

        ply_path = root_folder / scene / f"{scene}_vh_clean.ply"
        assert ply_path.exists(), f"PLY file not found: {ply_path}"

        # Use command line assimp with verbose logging and explicit format
        cmd = f"assimp export {ply_path} {tmp_path} --verbose --format glb"
        try:
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            if result.returncode != 0:
                tqdm.write(f"Error output: {result.stderr}")
                raise Exception(f"Assimp failed with return code {result.returncode}\nCommand: {cmd}\nOutput: {result.stdout}")
            
            # Rename only if export was successful
            tmp_path.rename(glb_path)
            tqdm.write(f"Exported {ply_path} to {glb_path}")
        except Exception as e:
            tqdm.write(f"Failed to process {scene}: {str(e)}")



if __name__ == "__main__":
    # Generate a CLI and call `main` with its two arguments: `foo` and `bar`.
    tyro.cli(main)
