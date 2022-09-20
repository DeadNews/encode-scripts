#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    ${vsx} --rcloneUpload --EVL --fast_mode {op1,ed}.vpy e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{1..2}.vpy {op1,ed}.vpy op2.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{3..5}.vpy m{1..3}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{6..8}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
