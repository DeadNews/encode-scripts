#!/usr/bin/env zsh

customOptions=(
    --cutree
    --aq-strength 1.17
    --crf 15
    --qcomp 0.72
    # --qcomp=0.76
    --psy-rd 2
    --rdoq-level 2
    --psy-rdoq 2
)
x265="${HOME}/my/bin/vpy-x265/vspipe-x265.zsh"
chmod u+x ${x265} && ${x265} ${customOptions[@]} ${@}
