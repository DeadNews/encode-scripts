#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy
    # ${vsx} --unlinkMode e1.vpy

elif [[ ${part} == 'test_nc' ]]; then
    ${vsx} --rcloneUpload --staticName --L {ed,op}.vpy
    ${vsx} --rcloneUpload --E --fast_mode {ed,op}.vpy
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.35' {ed,op}.vpy
    ${vsx} --unlinkMode {ed,op}.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.vpy
    # ${vsx} --rcloneUpload --EVL e{1..5}.vpy
    ${vsx} --rcloneUpload --EVL e{2..5}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{6..10}.vpy

elif [[ ${part} == '3' ]]; then
    # ${vsx} --rcloneUpload --EVL e{11..12}.vpy
    ${vsx} --unlinkMode e12.vpy
    ${vsx} --rcloneUpload --EVL e12.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --EVL e13.vpy s1.vpy {ed,op}.vpy
    ${vsx} --rcloneUpload --E --keyint 700 m1.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
