#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL e{1..12}.vpy {op,ed}.vpy pv.vpy m{1..6}.vpy
}
if [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL op.vpy e{1..6}.vpy
    ${vsx} --rcloneUpload --EVL --keyint 600 --psy-rdoq 1 m{1..3}.vpy
elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL ed.vpy e{7..12}.vpy
    ${vsx} --rcloneUpload --EVL --keyint 600 --psy-rdoq 1 m{4..6}.vpy
elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
else
    encodeAll
fi
