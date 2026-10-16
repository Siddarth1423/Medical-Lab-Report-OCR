def split_into_patches(image, patch_height=1000, overlap=100):
    """Split a tall image into overlapping horizontal patches."""
    height, width = image.shape[:2]
    if patch_height <= overlap:
        raise ValueError("patch_height must be greater than overlap")

    patches = []
    step = patch_height - overlap

    for y in range(0, height, step):
        end_y = min(y + patch_height, height)
        patch = image[y:end_y, :]
        if patch.size:
            patches.append(patch)
        if end_y == height:
            break

    return patches
