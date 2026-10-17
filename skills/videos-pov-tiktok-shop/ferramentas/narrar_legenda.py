"""Narração (edge-tts) + legenda palavra por palavra (.ass) no estilo TikTok.

Uso: python narrar_legenda.py <texto.txt> <saida_sem_ext> [voz] [rate]
Gera <saida>.mp3 e <saida>.ass (1 palavra por vez, branca com contorno preto, a 80% da altura).
"""
import asyncio, sys
import edge_tts

TXT, OUT = sys.argv[1], sys.argv[2]
VOZ = sys.argv[3] if len(sys.argv) > 3 else "pt-BR-AntonioNeural"
RATE = sys.argv[4] if len(sys.argv) > 4 else "+15%"

ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Palavra,Arial Black,84,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,3,14,0,2,60,60,330,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def ts(t):  # segundos -> h:mm:ss.cc
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


async def main():
    texto = open(TXT, encoding="utf-8").read().strip()
    com = edge_tts.Communicate(texto, VOZ, rate=RATE, boundary="WordBoundary")
    palavras = []
    with open(OUT + ".mp3", "wb") as f:
        async for c in com.stream():
            if c["type"] == "audio":
                f.write(c["data"])
            elif c["type"] == "WordBoundary":
                ini = c["offset"] / 1e7
                palavras.append([ini, ini + c["duration"] / 1e7, c["text"]])
    # cada palavra fica na tela até a próxima começar (sem piscar vazio entre palavras)
    for a, b in zip(palavras, palavras[1:]):
        a[1] = max(a[1], b[0])
    with open(OUT + ".ass", "w", encoding="utf-8") as f:
        f.write(ASS_HEAD)
        for ini, fim, w in palavras:
            f.write(f"Dialogue: 0,{ts(ini)},{ts(fim)},Palavra,,0,0,0,,{w.upper()}\n")
    print(f"{len(palavras)} palavras, fim da fala em {palavras[-1][1]:.2f}s")


asyncio.run(main())
