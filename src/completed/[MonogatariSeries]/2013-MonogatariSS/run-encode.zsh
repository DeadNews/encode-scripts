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
    ./vspipe-x264-lossless.zsh --depth 8 op{1,3}_aa.vpy ed{1,3,4,5,6}_aa.vpy
    ./run-vspipe-x265.zsh --rcloneUpload e{1..23}.vpy {op,ed}{1..4}.vpy ed{5..6}.vpy

    ./vspipe-x264-lossless.zsh --unlinkMode op{1,3}_aa.vpy ed{1,3,4,5,6}_aa.vpy
fi

# 60fps
# ./vspipe-x264-lossless.zsh --depth 10 --staticName e15.vpy
# ./run-vspipe-x265.zsh --rcloneUpload e15.vpy -- менять in
# ./run-vspipe-x265.zsh --rcloneUpload --keyint 625 e15_60fps.vpy
