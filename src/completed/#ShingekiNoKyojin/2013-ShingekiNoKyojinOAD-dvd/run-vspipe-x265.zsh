#!/usr/bin/env zsh

customOptions=(
    --ref 6
    --limit-refs 0
    --cutree
    --aq-strength 1.0
    # --aq-strength 0.9
    # --aq-strength 0.85
    # --crf 13.4
    # --crf 14.4
    # --crf 15.4
    --crf 15.7
    --qcomp 0.72
    --psy-rd 2
    --rdoq-level 2
    --psy-rdoq 2
)
x265="${HOME}/my/bin/vpy-x265/vspipe-x265.zsh"
chmod u+x ${x265} && ${x265} ${customOptions[@]} ${@}
