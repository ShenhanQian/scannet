# ScanNet

Scripts to download and process ScanNet dataset.

## `ply2glb.py`
### Dependency
Install assimp via
```shell
sudo apt install assimp-utils
```

### Usage
```shell
python ply2glb.py --root_folder $STORAGE_USER/data/scannet/scans/ --output_folder $STORAGE_USER/data/scannet_glb
```
> [!NOTE]
> The conversion fails on the following scenes for uncaptured reasons:
> - scene0020_01
> - scene0051_03
> - scene0077_00
> - scene0349_01
> - scene0588_00
> - scene0619_00
> - scene0627_00


## Extract .SENS files

### Usage
```shell
python extract_sens.py --scannet_dir $STORAGE_USER/data/scannet/
```
