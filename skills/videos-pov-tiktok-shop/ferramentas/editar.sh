#!/usr/bin/env bash
# Edição padrão TikTok POV. Rode DENTRO da pasta do vídeo: bash <pasta-da-skill>/ferramentas/editar.sh
# Lê de cortes.txt uma linha por trecho:  take inicio fim velocidade   (ex.: 2-tecido 0.5 6.0 1.25)
# Opcionais na pasta: headline.txt (topo, branca com contorno), audio/narracao.mp3 + audio/narracao.ass
# (gerados por ferramentas/narrar_legenda.py). Saída: final.mp4 (ou $OUT).
set -e
# ffmpeg do PATH; senão o instalado pelo winget (Gyan.FFmpeg)
if command -v ffmpeg >/dev/null; then B=$(dirname "$(command -v ffmpeg)")
else B=$(dirname "$(find "$HOME/AppData/Local/Microsoft/WinGet/Packages" -iname ffmpeg.exe | head -1)"); fi
[ -f ariblk.ttf ] || cp /c/Windows/Fonts/ariblk.ttf . 2>/dev/null || cp "/System/Library/Fonts/Supplemental/Arial Black.ttf" ariblk.ttf
HL_Y="${HL_Y:-0.10}"; HL_SIZE="${HL_SIZE:-58}"; BG_VOL="${BG_VOL:-0.15}"
# HL_STYLE=nativo: texto igual ao nativo do TikTok (TikTok Sans 700, pequeno, sombra leve, ~75% da altura) — estilo do @eulucsantos
HL_STYLE="${HL_STYLE:-grande}"
if [ "$HL_STYLE" = nativo ]; then
  cp "$(dirname "$0")/TikTokSans-700.ttf" . ; HL_FONT=TikTokSans-700.ttf; HL_Y="${HL_Y_NATIVO:-0.75}"; HL_SIZE="${HL_SIZE_NATIVO:-44}"; HL_FX="shadowcolor=black@0.55:shadowx=2:shadowy=2"
else
  HL_FONT=ariblk.ttf; HL_FX="borderw=7:bordercolor=black"
fi
IN=(); F=""; i=0; declare -A idx
while read -r t a b v; do
  [ -z "$t" ] && continue
  if [ -z "${idx[$t]}" ]; then idx[$t]=$(( ${#IN[@]} / 2 )); IN+=(-i "takes/$t.mp4"); fi
  n=${idx[$t]}
  F+="[$n:v]trim=$a:$b,setpts=(PTS-STARTPTS)/$v,scale=1080:1920,fps=30,setsar=1[v$i];"
  F+="[$n:a]atrim=$a:$b,asetpts=PTS-STARTPTS,atempo=$v,aresample=48000[a$i];"
  i=$((i+1))
done < cortes.txt
for j in $(seq 0 $((i-1))); do F+="[v$j][a$j]"; done
F+="concat=n=$i:v=1:a=1[vc][ac];"
V="[vc]"
if [ -f headline.txt ]; then
  F+="${V}drawtext=fontfile=$HL_FONT:textfile=headline.txt:text_align=C:x=(w-text_w)/2:y=h*$HL_Y:fontsize=$HL_SIZE:line_spacing=12:fontcolor=white:$HL_FX[vh];"; V="[vh]"
fi
if [ -f audio/narracao.ass ]; then
  F+="${V}subtitles=audio/narracao.ass[vs];"; V="[vs]"
fi
if [ -f audio/narracao.mp3 ]; then
  IN+=(-i audio/narracao.mp3); k=$(( ${#IN[@]} / 2 - 1 ))
  F+="[ac]volume=$BG_VOL[bg];[$k:a]aresample=48000[nar];[bg][nar]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5[a]"
else
  F+="[ac]anull[a]"
fi
F+=";${V}null[v]"
"$B/ffmpeg" -v error -y "${IN[@]}" -filter_complex "$F" -map "[v]" -map "[a]" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "${OUT:-final.mp4}"
"$B/ffprobe" -v error -show_entries format=duration -of csv=p=0 "${OUT:-final.mp4}"
