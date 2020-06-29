#! /bin/zsh
for i in **/*.jpg; do
    if [[ $i != *'-small'* && $i != *'-medium'* && $i != *'-large'* ]]; then
        sips -Z 500 "${i}" --out "${i%.jpg}-small.jpg";
        sips -Z 800 "${i}" --out "${i%.jpg}-medium.jpg";
        cp $i "${i%.jpg}-large.jpg"
    fi
done
