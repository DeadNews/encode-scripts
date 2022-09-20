#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --EVL --keyint 1000 --psy-rdoq 1 m1.py
    ${vsx} --rcloneUpload --L --staticName e1.py
    ${vsx} --rcloneUpload --E e1.py
}
if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E --fast_mode --cutree --aq-strength 1.07 e1.py
    ${vsx} --rcloneUpload --E --fast_mode e1.py

else
    encodeAll
fi
