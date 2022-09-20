#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L {op,ed}{1,2}_aa.vpy
    ${vsx} --rcloneUpload --EVL e{1..24}.vpy {op,ed}{1,2}.vpy pv{1,2}.vpy
}
if [[ ${part} == '1' ]]; then
    # ${vsx} --staticName   --L   {op,ed}1_aa.vpy
    # ${vsx} --rcloneUpload --EVL {op,ed}1.vpy e{1..8}.vpy pv{2,1}.vpy

    ${vsx} --rcloneUpload --EVL {op,ed}1.vpy e{1..8}.vpy

elif [[ ${part} == '2' ]]; then
    # ${vsx} --staticName   --L   {op,ed}{1,2}_aa.vpy
    # ${vsx} --rcloneUpload --EVL op2.vpy e{9..16}.vpy

    ${vsx} --unlinkMode e10.vpy
    ${vsx} --rcloneUpload --EVL e{9..16}.vpy

elif [[ ${part} == '3' ]]; then
    # ${vsx} --staticName   --L   {op,ed}2_aa.vpy
    # ${vsx} --rcloneUpload --EVL ed2.vpy e{17..24}.vpy

    ${vsx} --unlinkMode e18.vpy
    ${vsx} --rcloneUpload --EVL e{17..24}.vpy

elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
    # ${vsx} --rcloneUpload --EVL --crf 14.8  e1.vpy
    # ${vsx} --rcloneUpload --E --psy-rdoq 3  e1.vpy

else
    encodeAll
fi
