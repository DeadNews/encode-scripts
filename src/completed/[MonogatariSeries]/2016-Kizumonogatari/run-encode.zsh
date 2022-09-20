#!/usr/bin/env zsh

# default
chmod u+x ~/my/bin/vpy-x265/x265
chmod u+x vspipe-x264-lossless.zsh
chmod u+x run-vspipe-x265.zsh

# encode
if [ -f "./run-encode-override.zsh" ]; then
    chmod u+x run-encode-override.zsh && ./run-encode-override.zsh
else
    # ./vspipe-x264-lossless.zsh --depth 8 {op,ed}1_aa.py
    ./run-vspipe-x265.zsh --rcloneUpload e{1..3}.py m{1..3}.py
fi
