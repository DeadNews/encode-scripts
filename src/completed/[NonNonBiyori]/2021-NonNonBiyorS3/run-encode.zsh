#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
    ${vsx} --rcloneUpload --EVL {op,ed}.vpy

elif [[ ${part} == 'test_1' ]]; then
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
    ${vsx} --unlinkMode e1.vpy

elif [[ ${part} == 'test_2' ]]; then
    ${vsx} --rcloneUpload --E e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e3.vpy
    ${vsx} --rcloneUpload --EVL e{1..4}.vpy {op,ed}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{5..8}.vpy
    ${vsx} --rcloneUpload --EVL --aq-strength 0.8 --crf 15.2 pv.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{9..12}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
