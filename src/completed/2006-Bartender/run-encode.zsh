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
    # ${vsx} --rcloneUpload --E --fast_mode e1.vpy
    # ${vsx} --rcloneUpload --E --fast_mode --aq-strength 0.50 e1.vpy
    # ${vsx} --rcloneUpload --E --fast_mode --aq-strength 0.30 e1.vpy
    # ${vsx} --rcloneUpload --E --fast_mode --crf 17 e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode --crf 16.5 --aq-strength 0.70 e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --EVL e{1..3}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{4..6}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{7..9}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --EVL ed.vpy op.vpy m.vpy e{10..11}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end'
