#!/usr/bin/env zsh

customOptions=(
    --aq-mode 3
    --cutree
    --aq-strength 0.70
    # --crf 15
    # --crf 16.5
    --crf 17.5
    --qcomp 0.72
    --psy-rd 2
    --rdoq-level 2
    --psy-rdoq 2
)
x265="${HOME}/my/bin/vpy-x265/vspipe-x265.zsh"
chmod u+x ${x265} && ${x265} ${customOptions[@]} ${@}
