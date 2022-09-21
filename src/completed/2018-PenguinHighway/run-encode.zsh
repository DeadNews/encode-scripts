#!/usr/bin/env zsh

# default
bin265="${HOME}/my/bin/vpy-x265"
export LD_LIBRARY_PATH=${bin265}
chmod u+x "${bin265}/x265"
chmod u+x vspipe-x264-lossless.zsh
chmod u+x vspipe-x265.zsh

# encode
if [ -f "./run-encode-override.zsh" ]; then
    chmod u+x run-encode-override.zsh && ./run-encode-override.zsh
else
    # ./vspipe-x264-lossless.zsh --depth 8 {op,ed}{1..2}_aa.py
    ./vspipe-x265.zsh --dontconvertMKV --rcloneUpload PenguinHighway.py menu.py pv.py
fi
