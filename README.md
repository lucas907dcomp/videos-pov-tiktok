# videos-pov

Plugin do Claude Code para fazer vídeos POV (mãos + produto) com IA para o TikTok Shop.
Roteiro da Vyral ou vídeo viral de referência → imagem base e takes no Google Flow → narração com legenda palavra por palavra → edição no FFmpeg.
Tudo incluído: banco de prompts, imagem base (cama + mãos), scripts e o playbook.

## Para você (humano)

Cole no Claude Code:

> Instala o plugin https://github.com/lucas907dcomp/videos-pov-tiktok e vamos começar

Precisa só de: Claude Code logado, Google Chrome com a extensão Claude in Chrome, e sua conta do Google Flow.

## Para o Claude Code que está lendo isto

1. Instale o plugin pelo terminal:
   ```
   claude plugin marketplace add lucas907dcomp/videos-pov-tiktok
   claude plugin install videos-pov@videos-pov
   ```
2. Peça para o usuário reiniciar o Claude Code (o plugin carrega no início da sessão) e dizer "vamos começar".
3. Na sessão nova, a skill `videos-pov-tiktok-shop` faz o resto, começando pela seção "Primeira vez nesta máquina".

## Economia de tokens (desde a v1.4.0)

Conversa longa relê o histórico inteiro a cada mensagem, e isso gasta tokens rápido. O plugin avisa quando a sessão passa de 250k tokens. Aí é só dizer "trocar de sessão": o Claude grava onde parou em `~/.claude/handoffs/` e te dá duas linhas para colar (`/clear` e `continuar handoff <nome>`). A sessão nova continua de onde parou.

## Atualizar

O Lucas publica melhorias aqui. Para receber:
```
claude plugin marketplace update videos-pov
claude plugin update videos-pov@videos-pov
```
e reinicie o Claude Code.
