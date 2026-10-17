---
name: videos-pov-tiktok-shop
description: "Vídeos POV (mãos + produto) para TikTok Shop com IA: roteiro da Vyral ou vídeo viral de referência → cenas, imagem base e takes no Google Flow, narração com legenda palavra por palavra e edição no FFmpeg."
---

# Vídeos POV para TikTok Shop

Use quando o usuário mandar um roteiro da Vyral (blocos GANCHO / DESENVOLVIMENTO / PROVA / OBJEÇÃO / CTA) ou o link de um vídeo viral de referência, pedir para planejar as cenas de um vídeo POV ou pedir um prompt de cena.

**Perfil do criador (ler primeiro):** `~/.claude/videos-pov/perfil.md`. Tem a identidade das mãos, o cenário, o projeto do Flow, a pasta dos vídeos e onde ficam playbook e fichas. Se não existir, crie a partir de `perfil-exemplo.md` (nesta skill) perguntando ao usuário só o que faltar. Onde esta skill diz "kit da mão" ou "pasta dos vídeos", vale o que está no perfil.

**Antes de planejar:** leia o playbook (caminho no perfil): o que já sabemos e as hipóteses em teste, e as fichas que já têm métricas. Cada vídeo testa no máximo uma variável nova.
**Ao entregar o vídeo:** crie a ficha `AAAA-MM-DD-produto.md` (o que foi feito, takes descartados, edição, headline; métricas em 48h e 7 dias). Com 3+ fichas medidas, compare e atualize o playbook.

**Crítico cego (Gauntlet):** não rode por conta própria, gasta muito token. Só quando o usuário pedir.

**Ferramentas desta skill:** `ferramentas/editar.sh` e `ferramentas/narrar_legenda.py`, no diretório base desta skill (o caminho aparece quando ela carrega). Abaixo, `<skill>` = esse diretório.

Responda sempre em português. Os prompts saem em inglês, como na biblioteca (exceto os que já são em português lá).

## Fontes dos prompts

1. **Biblioteca VSA Ultra** — https://vsacomu.com.br/bibliotecadeprompts/ (login do usuário, salvo no navegador).
   - Abra no navegador. Se pedir login, peça para o usuário entrar; nunca digite senha.
   - Pegue o prompt sempre ao vivo da biblioteca, pelo id do card, com javascript na página:
     `const i = items.find(x => x.id === ID); [i.title, i.requisitos, i.config, i.prompt].join('\n\n')`
   - No Claude Code a saída do javascript corta em ~1000 caracteres. Junte os cards em `window.__p`, escreva tudo num `<article>` com `pre-wrap` no body e leia com `get_page_text` (1 chamada para todos).
   - Use o texto do prompt FIEL ao original. Só mude o que a seção "Adaptação masculina" manda. O prompt fica igual ao que funciona.
2. **Documento de prompts (Google Docs)** — https://docs.google.com/document/d/1RbynLRG9YQnBJmYplw_2hIavnnQC_rv8Qeurs8nfvNs (exportar com /export?format=txt: no Chrome isso BAIXA `Cópia de POV - PROMPTS .txt` em `~/Downloads`; leia o arquivo com grep/sed). Tem dois prompts que não estão na biblioteca:
   - **Colocar peças na cama uma por uma** ("Create a realistic top-down product placement video using the provided opening image as the starting frame..."). Usa 2 imagens: frame inicial e final.
   - **Fechamento: tirar peças da cama uma por uma** ("Create a realistic overhead closing video...").

## Catálogo POV da biblioteca (ids)

### Imagens (montar a cena)
| id | Card | O que faz | Imagens |
|---|---|---|---|
| 2 | Remover roupas/textos | Limpa um print de vídeo de referência: tira roupa, mãos e textos. Trocar a descrição do cenário pelo que aparece no print. | 1: print |
| 3 | Colocando a mão no ambiente | Põe as mãos no cenário vazio. **Usar o kit da mão do perfil.** | 1: cenário vazio |
| 4 | Colocar roupa no ambiente | Coloca a peça do produto na cena com as mãos. Base dos vídeos. | 1: cena com mãos · 2: produto |
| 1 | Recriando cenário | Troca a peça numa cena que já tem roupa, "como se tivesse saído da embalagem" na cama. | 1: cena com mãos+roupa · 2: produto |
| 5 | Roupa no pacote | Troca a roupa dentro de um pacote transparente (para o gancho do pacote). | 1: cena com pacote · 2: produto |
| 6 | Colocar embalagem do TikTok | Põe o pacote preto do TikTok Shop nas mãos. Lembrete do card: o pacote deve ser pequeno. | A: cena com mãos · B: pacote |

Se a imagem da cena NÃO tem roupa (caso da imagem base com mãos), no card 4 troque "Remove the clothing item from Image 1 and include..." por "Add the clothing item from Image 2..." e posicione a peça no centro, entre as mãos.

### Vídeos (todos Google Flow, vertical 9:16, salvo indicado)
| id | Card | Ação | Entrada | Melhor para |
|---|---|---|---|---|
| 43 | Gancho esticar rápido POV (IA) | Pega a peça de cima, estica forte 3x perto da câmera, devolve; repete com a próxima. Regra de pegada: blusa pelo peito, **calça/short pela cintura**. ~10s, com áudio de tecido. | imagem do card 4 | GANCHO (elasticidade, resistência) |
| 7 | Gancho esticar a roupa | Estica a peça de cima devagar, em loop. | imagem do card 4 | GANCHO calmo |
| 11 | Gancho pacote transparente | Rasga o pacote transparente com som e levanta a peça. ~5s. Ativar som no Flow. | imagem do card 5 | GANCHO unboxing |
| 12 | Gancho embalagem TikTok Shop | Rasga o pacote preto e tira as peças uma por uma (prompt em PT, editar ROUPA 1/2/3). Ativar som no Flow. | imagem do card 6 | GANCHO unboxing com várias peças |
| 10 | Gancho jogar roupa — opção 2 | Tira as peças do quadro e recoloca. Tem versão ESPECÍFICA (descrever cada peça) e PADRÃO (PT). | imagem do card 4 | GANCHO / variedade |
| 15 | Mostrar o tecido de perto | Pega uma peça, leva perto da câmera e passa os dedos no tecido. 8s. Original diz "blouse": trocar pela peça certa. | imagem do card 4 | DESENVOLVIMENTO (tecido, conforto) |
| 13 | Passar a mão na roupa | Peça fica na cama; mãos abrem e mostram detalhes (alça, gola, costura). Até 2 peças. | imagem do card 4 | DESENVOLVIMENTO / OBJEÇÃO |
| 39 | Passar a mão na roupa + zoom | Igual ao 13, com aproximação sutil da câmera no tecido. | imagem do card 4 | DESENVOLVIMENTO (qualidade) |
| 38 | Abrir zíper + zoom | **O texto é idêntico ao 39 e não fala em zíper.** Quando precisar do zíper, acrescente uma linha descrevendo a ação (ex.: abrir o zíper do bolso e mostrar o interior). | imagem do card 4 | OBJEÇÃO (bolso, zíper, fechamento) |

> **Zíper no Flow (testado 2026-10-15, calça):** o card 38 com a linha do zíper não abriu nada (o zoom tomou o vídeo). Prompt próprio com o zíper como ação principal abriu um zíper inventado no meio da calça. Funcionou no lugar certo só quando o prompt disse: quantos zíperes existem, de que lado da imagem, cor da fita e do puxador, e "o centro NÃO tem zíper". Ainda assim o zíper abriu longo demais (até o joelho) e fechou num salto: diga também o comprimento ("short pocket zipper, about one hand long").
| 14 | Mostrar as peças | Pega 2 peças, uma de cada vez, mostra perto da câmera, estica e devolve. | imagem do card 4 | PROVA (cores/variações) |
| 8 | Gancho tapar câmera e pegar produto | Mostra detalhes na cama e, no fim, a palma tampa 100% da câmera (transição). | imagem do card 4 | Transição entre cenas / CTA |

## Mapa roteiro → cena (ponto de partida, ajustar ao produto)
- **GANCHO**: 43 (peça elástica) · 11 ou 12 (unboxing) · 7 · 10.
- **DESENVOLVIMENTO** (tecido, conforto, toque gelado): 15 · 39 · 13.
- **PROVA** (várias cores, comprei todas, preço): 14 · "colocar peças na cama uma por uma" (doc) · 10.
- **OBJEÇÃO / detalhes** (bolso, zíper, cintura, costura): 38 (com linha do detalhe) · 13.
- **CTA**: 8 (palma tampa a câmera) · "fechamento tirar peças" (doc). O card 8 é o texto do 13/39 + palma: se a cena anterior for 13, 38 ou 39, use o fechamento do doc.
- Evite repetir a mesma ação em cenas seguidas. Um vídeo típico: 4 a 6 cenas.

## Kit da mão (vem do perfil)
- A identidade das mãos (luvas, tatuagem, relógio...), o cenário e a imagem base estão em `~/.claude/videos-pov/perfil.md`. Ela é fixa: todo take descreve a mesma mão.
- Se precisar gerar as mãos de novo: adaptar o card 3 trocando "feminine hands / fair skin / nails / bracelets / ring / small tattoo" pela descrição em inglês do perfil.

## Adaptação masculina (únicas mudanças permitidas no texto original)
Vale quando o kit do perfil é masculino. Os exemplos abaixo usam o kit luva preta + tatuagem + relógio; troque pelos itens do perfil.
- "feminine hands" / "the woman's hands" / "she" → "masculine hands" / "the man's hands" / "he".
- Onde o prompt fala de mãos/unhas/acessórios ("white nails", "nails", "manicure", "bracelets", "rings", "red nails") → "black nitrile gloves, tattooed forearms, wristwatch".
- Em HAND CONSISTENCY, trocar "Keep the exact same manicure" por "Keep the exact same black gloves • Keep the exact same tattoos • Keep the exact same wristwatch".
- "carpet" / "rug" → "bed sheet" (ou o cenário que estiver em uso), e manter "the same orange and blue lighting" quando for o cenário da cama.
- "blouse" → nome da peça real (pants, shorts, t-shirt...).
- Corrigir erros de digitação do original (ex.: "Ωproducts" no card 7).
- Não reescrever, resumir nem "melhorar" o resto do prompt.

## Checagem do roteiro
- A Vyral pode gerar o roteiro em voz feminina ("lindas", "as minhas"). Se o produto/conteúdo é masculino, avisar e oferecer a versão masculina do texto.

## Referência viral (TikTok) → estrutura do vídeo
Testado 2026-10-16 (camiseta dry fit). O usuário manda o link de um vídeo de IA que estourou; copiamos a estrutura, não o roteiro da Vyral (que costuma ser de vídeo com pessoa real).
1. Baixar: `python -m yt_dlp --impersonate chrome -o "referencia/ref.%(ext)s" <link>` (precisa de `pip install "yt-dlp[default,curl-cffi]"`; sem o impersonate o TikTok recusa). No Chrome o vídeo do TikTok não toca na automação (só a capa).
2. Métricas públicas: `python -m yt_dlp --impersonate chrome --skip-download --print "%(duration)s | views=%(view_count)s likes=%(like_count)s" <link>`.
3. Folha de contato (fps=2) + detecção de corte (`scdet`) + volume (`ebur128`). Se tiver legenda queimada, recorte só a faixa da legenda a fps=6 e leia as palavras: vira a transcrição sem precisar de Whisper.
4. Anote: duração, nº de cortes, o que as mãos fazem em cada trecho, headline, estilo de legenda, narração. Depois mapeie cada trecho num take nosso.

## Imagem base no Flow (produto na nossa cama)
1. Foto do produto: o link do TikTok Shop traz a imagem principal no parâmetro `og_info` da URL (CDN ibyteimg) — baixe com curl. A página do produto pode abrir CAPTCHA: feche, nunca resolva.
2. Subir a foto no Flow sem seletor de arquivo: no console da página do Flow, `fetch(url)` → `File` → disparar `paste` com `DataTransfer` na caixa de comando (contenteditable). Ela entra como ingrediente.
3. A cena com as mãos (imagem base do perfil) já está no projeto: ⋮ → Incluir no comando.
4. Configuração → Imagem (Nano Banana Pro, 9:16, x1). Prompt = card 4 adaptado + **escala explícita**: "cada peça tem uns 4 palmos de largura; juntas ocupam ~85% da largura do quadro; nunca pequenas". Sem isso as peças saem pequenas (calça).
5. No vídeo há durações 4/6/8/10s no mesmo painel.

## Gerar no Flow (Claude opera o Chrome do usuário)
Testado em 2026-10-14 (cena 4 da calça, ~40s para gerar).
1. Abra o projeto numa aba sua do grupo MCP (`https://flow.google.com/project/<id>`). Não feche a última aba do grupo no meio: o grupo some e as ids mudam.
2. Na imagem de entrada, menu ⋮ → **Animar**: ela vira o frame "Início". Para 2 frames (ex.: colocar uma por uma), preencha também "Fim".
3. Clique na caixa "O que você quer criar?", digite o prompt **numa linha só** (Enter pode enviar) e confira o rodapé: `Vídeo · 720p · 8s · 9:16 · x1`.
4. Clique na seta. O vídeo aparece como 1º card do projeto.
5. **Revisar cada take antes de mostrar ao usuário** (o player é canvas, sem `<video>` no DOM). Abra o card no editor; a régua da timeline vai de x≈20 (0s) a x≈836 (8s), ~102 px/s, em y≈345. Para cada tempo (0, 1, 2 … 7,9s; 0,5s onde houver ação): clique na régua → botão tela cheia → espere 0,7s → zoom no quadro → botão sair da tela cheia (NÃO Esc: Esc sai do editor). Nunca revisar com o vídeo rodando em loop.
6. Checklist por take: a ação principal do prompt aconteceu? peça inventada/duplicada ou detalhe novo (bolso, zíper, estampa)? peça some/teletransporta? mão/braço sem corpo ou deformado? câmera pula ou zoom volta de uma vez? último quadro bate com o que a próxima cena espera? Veredito: APROVADO / REPROVADO + o motivo com o segundo.

## Narração + legenda palavra por palavra (estilo da referência)
- `python <skill>/ferramentas/narrar_legenda.py narracao.txt audio/narracao [voz] [rate]` (precisa de `pip install edge-tts`) → `audio/narracao.mp3` + `audio/narracao.ass` (1 palavra por vez, Arial Black branca contorno preto, ~83% da altura). Voz padrão pt-BR-AntonioNeural +15%.
- Texto da narração segue a estrutura da referência: produto/oferta → benefício do tecido → caimento → escassez → CTA ("carrinho laranja aqui embaixo"). Não cite preço sem conferir a variação do kit.
- Encaixe cada frase num take pelo tempo da 1ª palavra da frase no .ass (`grep` nas palavras-chave).
- Escreva a narração numa frase só, separada por vírgulas: com ponto final o edge-tts faz pausas de ~0,8s (23% do vídeo mudo na 1ª versão da camiseta).
- Legenda em caixa preta sólida (BorderStyle 3), como a referência: contorno sozinho some em cima de camiseta branca.
- CTA "aponta pro carrinho": a IA não entende "apontar pro canto" (fez os indicadores apontarem um pro outro). Funcionou com alvo físico: "o indicador direito toca a cama no canto inferior esquerdo 3 vezes, como apertando um botão".
- Acessório (relógio etc.) troca de cor entre takes ou no meio do take: descreva o acessório exato do perfil no prompt de todo take e corte os trechos em que ele muda.
- O crítico cego não conhece gíria: "não marca pizza" (mancha de suor) é expressão brasileira e fica.
- Edição: `bash <skill>/ferramentas/editar.sh` dentro da pasta do vídeo, com `cortes.txt` (`take inicio fim velocidade`), `headline.txt` e `audio/`. Velocidade por trecho (1x a 1.25x com narração; 1.6x no formato só-música).

## Baixar e editar (FFmpeg)
Testado em 2026-10-15 (calça, 4 takes → 12,9s).
1. Baixar cada take no Flow: ⋮ → Fazer o download → **1080p** (não existe 2K; 4K pede upgrade). O upscale leva ~1 min; um por vez. Cai em `~/Downloads`; copie para `<pasta do vídeo>/takes/N-nome.mp4`.
2. Folha de contato por take (1 quadro a cada 0,5s com tempo): `ffmpeg -i take.mp4 -vf "fps=2,scale=180:-1,drawtext=fontfile=revisao/arial.ttf:text='%{pts\:hms}':...,tile=8x2" -frames:v 1 revisao/take.png` (copie a arial.ttf do sistema para `revisao/`: caminho com `C:` quebra o filtro). Leia a imagem e escolha os trechos sem erro.
3. Padrão que funcionou: **13s no total, 1.6x**, ordem colocar na cama → esticar → tecido de perto → tirar da cama. 13s × 1.6 = ~20,8s de bruto para distribuir entre os takes.
4. Escreva `cortes.txt` (uma linha por trecho: `take inicio fim velocidade`, ex. `2-tecido 0.5 6.0 1.6`) e rode `bash <skill>/ferramentas/editar.sh` dentro da pasta do vídeo → `final.mp4` (1080x1920, 30fps). Lê também `headline.txt` e `audio/` se existirem. Ajustes por variável: `HL_Y`, `HL_SIZE`, `BG_VOL`, `OUT`.
5. Na escolha dos trechos, corte também a TRANSIÇÃO entre ações: peça deslizando/arrastando por cima de outra (ex.: bege passando na diagonal sobre a preta) parece errado mesmo sem deformar. Entre direto na ação já acontecendo (jump cut funciona no TikTok). Erro pego na revisão humana da calça, não na do Claude.
   **Regra: só corte no meio de um take se tiver erro** (corte sem motivo fica abrupto). Para caber nos 13s, apare o começo e o fim dos takes.
6. **Headline** (obrigatória): `headline.txt` na pasta do vídeo, uma frase por linha (3 linhas curtas, MAIÚSCULAS). Título chamativo sobre preço/achado (ex.: "NÃO ACREDITO QUE ESSAS / 3 CALÇAS SAÍRAM / QUASE DE GRAÇA!"). O `editar.sh` desenha em Arial Black (`ariblk.ttf` copiada para a pasta), branca com contorno preto (borderw=7), fontsize 58, a 20% da altura, o vídeo todo. Emoji fica de fora (drawtext não desenha emoji colorido); use "!". Confira um quadro: a linha mais longa não pode encostar nas bordas (os botões do TikTok ficam à direita).
7. Revise o `final.mp4` com folha de contato (fps=3) e amplie qualquer trecho suspeito antes de entregar.
FFmpeg: do PATH; no Windows, se não estiver no PATH, `winget install Gyan.FFmpeg` (o `editar.sh` acha sozinho).

## Formato da resposta (Claude Code)
O usuário copia os prompts de uma página com botão de copiar, não do terminal.
1. Pasta do vídeo: `<pasta dos vídeos do perfil>/AAAA-MM-DD-<produto>/`.
2. Escreva `conteudo.html` lá, copiando a estrutura de `exemplo-conteudo.html` (nesta skill): header com título e `.progress`, bloco do roteiro, bloco das imagens na ordem, um `<article class="scene">` por prompt (número, título, `.beat` com bloco + card, `.line` com a fala, `.meta` com ferramenta/entrada e `li.warn` para som ligado ou alerta, `<pre>` com o prompt, actions com copy/more/checkbox), e uma `.note` de no máximo 2 linhas sobre o que foi adaptado. Escape `&` e `<` no `<pre>`.
3. Monte com `template.html` desta skill trocando `{{TITULO}}` (nome curto: "<Produto> POV") e `{{CONTEUDO}}`, salve como `prompts.html`, e publique com a ferramenta Artifact (icon `video`).
4. No chat: só o link, a tabela roteiro → cena e os alertas. Nada de prompt no terminal.
