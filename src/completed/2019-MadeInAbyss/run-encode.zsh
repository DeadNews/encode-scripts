#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --rcloneUpload --EVL e{1..2}.py
    ${vsx} --rcloneUpload --E --keyint 1000 --crf 16 --psy-rdoq 1 --cutree m2.py
}
if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E --fast_mode e1.py
    ${vsx} --rcloneUpload --E --keyint 1000 --crf 16 --psy-rdoq 1 --cutree m1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py
    ${vsx} --rcloneUpload --E --keyint 1000 --crf 16 --psy-rdoq 1 --cutree m1.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --staticName --L e2.py
    ${vsx} --rcloneUpload --E e2.py
    ${vsx} --rcloneUpload --E --keyint 1000 --crf 16 --psy-rdoq 1 --cutree m2.py

else
    encodeAll
fi
