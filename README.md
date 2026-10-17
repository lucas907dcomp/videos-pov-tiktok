# videos-pov

Plugin do Claude Code para fazer vídeos POV (mãos + produto) com IA para o TikTok Shop.
Roteiro da Vyral ou vídeo viral de referência → imagem base e takes no Google Flow → narração com legenda palavra por palavra → edição no FFmpeg.

## Instalar (uma vez)

1. Pré-requisitos (Windows):
   ```
   winget install Gyan.FFmpeg
   pip install edge-tts "yt-dlp[default,curl-cffi]"
   ```
   Também: Git for Windows (o Claude Code já usa), extensão Claude in Chrome, conta no Google Flow e acesso à biblioteca VSA e ao doc de prompts.
2. No Claude Code:
   ```
   /plugin marketplace add lucas907dcomp/videos-pov-tiktok
   /plugin install videos-pov@videos-pov
   ```
   O repositório é privado: sua conta do GitHub precisa ter sido convidada, e o git precisa estar logado nela (`gh auth login`).
3. Reinicie o Claude Code e peça: "vamos fazer um vídeo POV". Na primeira vez ele monta seu perfil em `~/.claude/videos-pov/perfil.md` (sua mão, seu cenário, seu projeto do Flow).

## Atualizar

```
/plugin marketplace update videos-pov
```
Depois reinicie o Claude Code. Ou ative a atualização automática em `/plugin` → Marketplaces → videos-pov.
Seu perfil não é tocado pela atualização.
