#!/usr/bin/env zsh

customOptions=(
    # --aq-mode 2 #no
    --aq-mode 3
    --cutree
    # --aq-strength 1.00
    --aq-strength 1.03
    --crf 15
    --qcomp 0.72
    --psy-rd 2
    --rdoq-level 2
    --psy-rdoq 2
)
x265="${HOME}/my/bin/vpy-x265/vspipe-x265.zsh"
chmod u+x ${x265} && ${x265} ${customOptions[@]} ${@}
