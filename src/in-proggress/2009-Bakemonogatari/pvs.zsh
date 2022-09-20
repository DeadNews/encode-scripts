#!/usr/bin/env zsh

cd "${0:h}"
mkdir -p ./temp

for F in pv{1..12}; do
    echo ${F}
    vspipe --arg in_filename=${F} pvs.vpy - --y4m | x264 --crf 0 --qp 0 --output-depth 10 \
        --preset ultrafast --threads auto --output ./temp/${F}.mp4 --demuxer "y4m" -

    ./run-vspipe-x265.zsh --EVL ./temp/${F}.mp4
done
