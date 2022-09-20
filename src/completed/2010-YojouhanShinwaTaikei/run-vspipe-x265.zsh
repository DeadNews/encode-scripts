#!/usr/bin/env zsh

customOptions=(
    --aq-strength 0.85
    # --crf 15.4
    --crf 15.2
    --qcomp 0.72
    --psy-rd 2
    --rdoq-level 2
    # --psy-rdoq 2
    --psy-rdoq 1
)
x265="${HOME}/my/bin/vpy-x265/vspipe-x265.zsh"
chmod u+x ${x265} && ${x265} ${customOptions[@]} ${@}
