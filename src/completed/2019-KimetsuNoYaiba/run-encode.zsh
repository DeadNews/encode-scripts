#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E --fast_mode e1.py

elif [[ ${part} == '1' ]]; then
    rm -R ./temp
    ${vsx} --rcloneUpload --EVL e{1..7}.py

elif [[ ${part} == '2' ]]; then
    rm -R ./temp
    ${vsx} --rcloneUpload --EVL e{8..14}.py

elif [[ ${part} == '3' ]]; then
    rm -R ./temp
    ${vsx} --rcloneUpload --EVL {op,ed}1.py ed2.py e{15..20}.py

elif [[ ${part} == '4' ]]; then
    rm -R ./temp
    ${vsx} --rcloneUpload --EVL e{21..26}.py m{1..11}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
