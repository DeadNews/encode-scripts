#!/usr/bin/env zsh

# default
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode

# # default
# chmod u+x ~/my/bin/vpy-x265/x265
# chmod u+x vspipe-x264-lossless.zsh
# chmod u+x run-vspipe-x265.zsh

# encode
if [ -f "./run-encode-override.zsh" ]; then
    chmod u+x run-encode-override.zsh && ./run-encode-override.zsh
else
    ./vspipe-x264-lossless.zsh --depth 8 op{1,3}_aa.py ed{1,3,4,5,6}_aa.py
    ./run-vspipe-x265.zsh --rcloneUpload e{1..23}.py {op,ed}{1..4}.py ed{5..6}.py

    ./vspipe-x264-lossless.zsh --unlinkMode op{1,3}_aa.py ed{1,3,4,5,6}_aa.py
fi

# 60fps
# ./vspipe-x264-lossless.zsh --depth 10 --staticName e15.py
# ./run-vspipe-x265.zsh --rcloneUpload e15.py -- менять in
# ./run-vspipe-x265.zsh --rcloneUpload --keyint 625 e15_60fps.py
