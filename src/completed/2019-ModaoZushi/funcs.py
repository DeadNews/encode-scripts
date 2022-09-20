def epis_crop(clip):
    return clip.std.CropRel(top=138, bottom=138)


def epis_add(clip):
    return clip.std.AddBorders(top=6, bottom=6)
