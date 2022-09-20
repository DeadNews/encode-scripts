#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    #     ${vsx} --unlinkMode e4.vpy
    ${vsx} --rcloneUpload --staticName --L e4.vpy
    ${vsx} --rcloneUpload --E e4.vpy
    ${vsx} --rcloneUpload --EVL {op1,ed}.vpy
    ${vsx} --rcloneUpload --EVL m1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e4.vpy
    ${vsx} --rcloneUpload --EVL e{1..5}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{6..10}.vpy {op1,ed}.vpy op2.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{11..15}.vpy m{1..4}.vpy

elif
    [[ ${part} == 'all' ]]
then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
