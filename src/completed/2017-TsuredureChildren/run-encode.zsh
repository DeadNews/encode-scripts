#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

${vsx} --unlinkMode e1.py
# encode
encodeAll() {
    ${vsx} --rcloneUpload --EVL e{1..12}.py
}
if [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{1..6}.py
elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{7..12}.py
elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --psy-rdoq 1 --E e1.py
    # ${vsx} --rcloneUpload --psy-rdoq 2 --E e1.py
else
    encodeAll
fi
