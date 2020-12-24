hhfetcher is for fetching common resources in a directory.

Current supported API:
```
get_subfolders(root: str) -> [str]: Get immediate subfolders in folder of root.

get_subfolder_names(root: str) -> [str]: Get names of immediate subfolder in folder of root.

get_subfolders_recursively(root: str) -> [str]: Get all subfolders recursively in folder of root.

get_files_in_dir(root: str, formats: [str]) -> [str]: Get all files just in directory of root.

get_files_recursively_in_dir(root: str, formats: [str]) -> [str]: Get all files recursively contained in directory of root.

get_imgs_in_dir(root: str) -> [str]: Get all imgs just in directory of root.

get_imgs_recursively_in_dir(root: str) -> [str]: Get all imgs recursively contained in directory of root.

```

## Installation
```
pip install hhfetcher
```

## Usage
```
import hhfetcher as fetcher

# get subfolders
subfolders = fetcher.get_subfolders("/home")
subfolder_names = fetcher.get_subfolder_names("/home")
subfolders_recur = fetcher.get_subfolders_recursively("/home")

# get files with specified formats
all_jsons = fetcher.get_files_in_dir("/home", formats=[".json"])
all_jsons_recur = fetcher.get_files_recursively_in_dir("/home", formats=[".json"])

# get all images with default image_formats = [".jpg", ".jpeg", ".png", ".JPEG", ".JPG", ".PNG"]
imgs = fetcher.get_imgs_in_dir("/home")
imgs_recur = fetcher.get_imgs_recursively_in_dir("/home")

```