HHfetcher is for fetching common resources in a dir.

Supported API:

`get_subfolders(root: str) -> [str]`: Get immediate subfolders in folder of root
`get_subfolder_names(root: str) -> [str]`: Get names of immediate subfolder in folder of root
`get_subfolders_recursively(root: str) -> [str]`: Get all subfolders recursively in folder of root.

`get_files_in_dir(root: str, formats: [str]) -> [str]`: Get all files just in directory of root.
`get_files_recursively_in_dir(root: str, formats: [str]) -> [str]`: Get all files recursively contained in directory of root.

`get_imgs_in_dir(root: str) -> [str]`: Get all imgs just in directory of root.
`get_imgs_recursively_in_dir(root: str) -> [str]`: Get all imgs recursively contained in directory of root.
