# Avisa quando a sessão ficou cara de manter.
#
# Por quê: sessão longa relê o contexto inteiro a cada mensagem. Numa sessão
# de ~800k, 172 mensagens leram 134M de tokens com só 96k de saída: o gasto
# foi reler conversa, não trabalhar.
#
# Como mede: o Claude Code manda o caminho do transcript no stdin (JSON). A
# última linha com `usage` traz o tamanho real do contexto. Nada é estimado.
import json, sys

AVISO, URGENTE = 250_000, 400_000

try:
    # utf-8 explícito: no Windows o stdin vem no encoding local e quebra caminho com acento
    transcript = json.loads(sys.stdin.buffer.read().decode("utf-8"))["transcript_path"]
    ctx = 0
    with open(transcript, encoding="utf-8", errors="ignore") as f:
        for linha in f:
            try:
                u = (json.loads(linha).get("message") or {}).get("usage")
            except Exception:
                continue
            if u:
                ctx = (u.get("cache_read_input_tokens", 0)
                       + u.get("cache_creation_input_tokens", 0)
                       + u.get("input_tokens", 0))
except Exception:
    sys.exit(0)

sys.stdout.reconfigure(encoding="utf-8")
if ctx >= URGENTE:
    print(f"<peso-da-sessao>Contexto em {ctx/1000:.0f}k tokens: cada mensagem daqui para frente custa isso tudo de novo. PARE e rode a skill trocar-sessao agora, antes de continuar a tarefa.</peso-da-sessao>")
elif ctx >= AVISO:
    print(f"<peso-da-sessao>Contexto em {ctx/1000:.0f}k tokens. Ao terminar o passo atual, ofereça a troca de sessão (skill trocar-sessao) em uma linha, sem interromper o que está em andamento.</peso-da-sessao>")
