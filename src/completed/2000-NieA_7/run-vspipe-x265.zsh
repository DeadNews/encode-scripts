#!/usr/bin/env zsh

customOptions=(
    --ref 6
    --cutree
    --aq-strength 1.04
    # --aq-strength 0.85
    --crf 13.4
    --qcomp 0.72
    --psy-rd 2
    --rdoq-level 2
    --psy-rdoq 2
)
x265="${HOME}/my/bin/vpy-x265/vspipe-x265.zsh"
chmod u+x ${x265} && ${x265} ${customOptions[@]} ${@}
