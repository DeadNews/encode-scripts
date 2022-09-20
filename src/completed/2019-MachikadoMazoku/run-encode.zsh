#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    # ${vsx} --staticName   --L   {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL {op,ed}.vpy e{1..12}.vpy
    ${vsx} --rcloneUpload --EVL --keyint 700 --psy-rdoq 1 s{1..4}.vpy pv{1..4}.vpy m{1..4}.vpy
}
if [[ ${part} == '1' ]]; then
    # ${vsx} --rcloneUpload --EVL e{1..6}.vpy
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --EVL e{2..6}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL --keyint 700 --psy-rdoq 1 s{2..3}.vpy pv{2..3}.vpy m{2..3}.vpy
    ${vsx} --rcloneUpload --EVL e{7..9}.vpy
    # ${vsx} --rcloneUpload --EVL --keyint 700 --psy-rdoq 1 {op,ed}.vpy s{1..3}.vpy pv{1..3}.vpy m{1..3}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL --keyint 700 --psy-rdoq 1 s4.vpy pv4.vpy m4.vpy
    ${vsx} --rcloneUpload --EVL e{10..12}.vpy

elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
else
    encodeAll
fi
