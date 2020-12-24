import os

img_formats = [".jpg", ".jpeg", ".png", ".JPEG", ".JPG", ".PNG"]
video_formats = [".mp4", ".MP4", ".avi", ".AVI"]


__all__ = [
    "get_subfolders",
    "get_subfolder_names",
    "get_subfolders_recursively",
    "get_files_in_dir",
    "get_files_recursively_in_dir",
    "get_imgs_in_dir",
    "get_imgs_recursively_in_dir"
]


def _expand_user_and_relative_for_path(p):
    p = os.path.expanduser(p)
    return os.path.abspath(p)


def get_subfolders(root: str) -> [str]:
    """Get immediate subfolders in folder of root

    Args:
        root (str): target folder path

    Returns:
        list[str]: list of subfolder path string
    """
    root = _expand_user_and_relative_for_path(root)

    assert os.path.isdir(root), "invalid folder: {}".format(root)
    return [f.path for f in os.scandir(root) if f.is_dir()]


def get_subfolder_names(root: str) -> [str]:
    """Get names of immediate subfolder in folder of root

    Args:
        root (str): target folder path

    Returns:
        list[str]: list of subfolder name string
    """
    root = _expand_user_and_relative_for_path(root)
    assert os.path.isdir(root), "invalid folder: {}".format(root)
    return [f.name for f in os.scandir(root) if f.is_dir()]


def get_subfolders_recursively(root: str) -> [str]:
    """Get all subfolders recursively in folder of root.

    Args:
        root (str): target folder path

    Returns:
        list[str]: list of subfolder path string
    """
    root = _expand_user_and_relative_for_path(root)
    assert os.path.isdir(root), "invalid folder: {}".format(root)
    folder_list = []
    for root, dirs, _ in os.walk(root):
        for one_dir in dirs:
            one_dir = os.path.join(root, one_dir)
            folder_list.append(one_dir)
    return folder_list


def get_files_in_dir(root: str, formats: [str]) -> [str]:
    """Get all files just in directory of root.

    Args:
        root (str): target directory path
        formats (list[str]): file formats

    Returns:
        list[str]: list of file path string
    """
    root = _expand_user_and_relative_for_path(root)
    assert os.path.isdir(root), "invalid directory: {}".format(root)
    assert len(formats), "invalid format: {}".format(formats)
    all_files = []
    files = os.listdir(root)
    for f in files:
        ext = os.path.splitext(f)[1]
        if ext in formats:
            all_files.append(os.path.join(root, f))
    return all_files


def get_files_recursively_in_dir(root: str, formats: [str]) -> [str]:
    """Get all files recursively contained in directory of root.

    Args:
        root (str): target directory
        formats (list[str]): file formats

    Returns:
        list[str]: list of file path string
    """
    root = _expand_user_and_relative_for_path(root)
    assert os.path.isdir(root), "invalid directory: {}".format(root)
    assert len(formats), "invalid format: {}".format(formats)
    all_files = []
    subfolders = get_subfolders_recursively(root)
    subfolders.append(root)
    for folder in subfolders:
        files = get_files_in_dir(folder, formats)
        all_files.extend(files)
    return all_files


def get_imgs_in_dir(root: str) -> [str]:
    """Get all imgs just in directory of root.

    Args:
        root (str): target directory

    Returns:
        list[str]: list of img path string
    """
    global img_formats
    return get_files_in_dir(root, img_formats)


def get_imgs_recursively_in_dir(root: str) -> [str]:
    """Get all imgs recursively contained in directory of root.

    Args:
        root (str): target directory

    Returns:
        list[str]: list of img path string
    """
    global img_formats
    return get_files_recursively_in_dir(root, img_formats)

