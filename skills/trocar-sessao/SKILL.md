---
name: trocar-sessao
description: Troca de sessão sem perder o fio, para economizar tokens. Grava o estado do trabalho em andamento num arquivo de handoff e devolve a frase exata para colar na sessão nova. Use quando o usuário disser "trocar de sessão", "tá pesado", "handoff", "vamos continuar em outra sessão", quando o aviso <peso-da-sessao> aparecer, ou quando ele disser "continuar handoff <nome>".
---

# Trocar de sessão

Sessão longa relê o contexto INTEIRO a cada mensagem: quanto maior a conversa, mais cara cada resposta. O hook `peso-da-sessao` do plugin avisa a partir de 250k tokens. Esta skill fecha o fio num arquivo para a sessão nova começar limpa, sem reler a conversa.

## 1. Escrever o handoff

Arquivo: `~/.claude/handoffs/handoff-<slug>.md` (slug curto da frente de trabalho: `tiktok-shop`, `camiseta-cac`...). Crie a pasta se não existir. Um arquivo por frente; se já existir, **sobrescreva**: vale o estado de agora.

```markdown
---
trabalho: <slug>
data: YYYY-MM-DD HH:MM
---

# Handoff · <trabalho>

## Onde paramos
<2-4 linhas: o que estava sendo feito e em que ponto exato>

## Estado agora
<o que está pronto, o que falta, arquivos/vídeos e onde estão, projeto do Flow e modelo usado>

## Decisões desta sessão
- <decisão + motivo em meia linha>

## Próximo passo concreto
1. <primeira coisa a fazer, com caminho de arquivo>

## Armadilhas
- <o que já deu errado aqui e como evitar>
```

**Referencie, não transcreva**: código, prompts e regras já vivem nos arquivos da skill e nas pastas dos vídeos, então o handoff só aponta para eles. Passou de ~60 linhas, virou resumo da conversa: corte. Nunca grave senha, token ou chave.

Se nesta sessão surgiu regra nova de vídeo (corte, prompt, take que reprovou), grave também na `ficha.md` do vídeo antes de trocar.

## 2. Entregar a troca

Responda curto: o caminho do handoff e as duas ações do usuário, nesta ordem:

```
/clear
continuar handoff <slug>
```

## 3. Na sessão nova ("continuar handoff <slug>")

Leia `~/.claude/handoffs/handoff-<slug>.md`, diga em uma linha onde paramos e qual é o próximo passo, e siga. Não tente recuperar a conversa antiga: se faltou algo, o handoff estava incompleto, então capriche no próximo.
