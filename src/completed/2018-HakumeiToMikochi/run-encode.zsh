#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# rm -R ./temp
# encode
encodeAll() {
    ${vsx} --rcloneUpload --EVL e{1..13}.py op{1..2}.py m{1..4}.py ed{1..13}.py
}
if [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{2..5}.py e1.py
elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{6..9}.py ed{1..11}.py
elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{10..13}.py op{1..2}.py ed{12..13}.py
    ${vsx} --rcloneUpload --EVL --keyint 700 m{1..4}.py
elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py
else
    encodeAll
fi
