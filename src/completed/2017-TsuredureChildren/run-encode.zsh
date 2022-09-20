#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

${vsx} --unlinkMode e1.vpy
# encode
encodeAll() {
    ${vsx} --rcloneUpload --EVL e{1..12}.vpy
}
if [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{1..6}.vpy
elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{7..12}.vpy
elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --psy-rdoq 1 --E e1.vpy
    # ${vsx} --rcloneUpload --psy-rdoq 2 --E e1.vpy
else
    encodeAll
fi
