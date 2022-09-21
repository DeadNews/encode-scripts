#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E --fast_mode e1.py
    # ${vsx} --unlinkMode e1.py

elif [[ ${part} == 'test_nc' ]]; then
    ${vsx} --rcloneUpload --staticName --L {ed,op}.py
    ${vsx} --rcloneUpload --E --fast_mode {ed,op}.py
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.35' {ed,op}.py
    ${vsx} --unlinkMode {ed,op}.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.py
    # ${vsx} --rcloneUpload --EVL e{1..5}.py
    ${vsx} --rcloneUpload --EVL e{2..5}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{6..10}.py

elif [[ ${part} == '3' ]]; then
    # ${vsx} --rcloneUpload --EVL e{11..12}.py
    ${vsx} --unlinkMode e12.py
    ${vsx} --rcloneUpload --EVL e12.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --EVL e13.py s1.py {ed,op}.py
    ${vsx} --rcloneUpload --E --keyint 700 m1.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
