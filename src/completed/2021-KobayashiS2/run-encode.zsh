#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    ${vsx} --rcloneUpload --E --fast_mode {op,ed}.vpy e1.vpy
    # ${vsx} --rcloneUpload --staticName --L {op,ed}.vpy e1.vpy
    # ${vsx} --rcloneUpload --E --fast_mode --aq-strength 0.97 --cutree {op,ed}.vpy e1.vpy
    # ${vsx} --rcloneUpload --E --fast_mode --crf 16 {op,ed}.vpy e1.vpy
    # ${vsx} --unlinkMode {op,ed}.vpy e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{1..3}.vpy {op,ed}.vpy ed_e3.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{4..6}.vpy
    ${vsx} --rcloneUpload --E --keyint 700 m{1..4}.vpy f{1..24}.vpy
    ${vsx} --rcloneUpload --E --keyint 350 pv{1..4}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{7..9}.vpy s{1..4}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{10..12}.vpy

elif [[ ${part} == '5' ]]; then
    ${vsx} --rcloneUpload --E e13.vpy s5.vpy i{1..16}.vpy
    ${vsx} --rcloneUpload --E --keyint 700 m5.vpy f{25..26}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
