# Receita padrão — vídeo aprovado pelo Lucas (2026-10-20)

Vídeo de referência aprovado: camisa de compressão gola alta, `final-d4.mp4` (14,7 s). "Nessa qualidade, com esses cortes, com esses takes." Todo vídeo novo começa daqui.
Modelo do playbook: **D · espelho do @eulucsantos**. Os modelos A, B e C continuam em teste; esta receita não os apaga.

## 0. De onde vêm os produtos e o formato
- Espelhar o perfil **@eulucsantos** (TikTok): postar os produtos que ele postou (são vencedores) com o mesmo gancho e o mesmo jeito de filmar.
- Listar os vídeos dele com views: `python -m yt_dlp --impersonate chrome --flat-playlist --print "%(id)s|%(view_count)s|%(duration)s|%(title).60s" https://www.tiktok.com/@eulucsantos`. Ordenar por views e baixar o do produto escolhido.
- O vídeo base do formato é o de 2,6 mi (id 7688739395641314580).

## 1. Analisar o vídeo dele (antes de gerar qualquer coisa)
- Folha de contato a **4 fps** (não 2) com tempo escrito: é o que mostra cada troca de cena.
- Cortes: `scdet` com **limiar 4** e conferir o quadro antes/depois de cada pico. Limiar alto não vê jump cut entre cenas parecidas (erro já cometido: disse "1 take" e eram 5 trechos).
- Anotar: duração, cada trecho (o que a mão faz), primeiro quadro, escala da peça, texto (frase), fim.
- Se quiser comparar sem viés, um agente analisa folhas anônimas (dele + nossas) sem saber quem é quem.

## 2. Estrutura (5 cenas, na ordem)
| # | Cena | Duração final | Como gerar |
|---|---|---|---|
| 1 | **Jogar na cama**: joga a peça de baixo, depois a de cima por cima | ~2,5 s | Frames: Início = cama vazia com as mãos, Fim = imagem do produto |
| 2 | **Esticada longa e sustentada** pela barra, peça rente à cama | ~2,3 s | Animar a imagem do produto |
| 3 | **Esticar com vai e volta**: levanta um pouco, estica moderado e solta 4–5 vezes, devolve a peça | ~3,8 s | Animar a imagem do produto |
| 4 | **Close**: palma passando na estampa/logo, zoom digital 1,35x na edição | ~1,7 s | Animar a imagem do produto |
| 5 | **Tirar tudo da cama**: uma peça de cada vez, fecha na cama vazia | ~4,3 s | Frames: Início = imagem do produto, Fim = cama vazia |
Duração livre (Lucas testa várias); o que importa é ter as 5 cenas bem cortadas.

## 3. Imagens (Nano Banana Pro, 0 crédito, 9:16)
1. **Imagem do produto**: peças grandes, tamanho adulto real, mangas vazando pelas bordas do quadro, uma peça por cima da outra (a de cima um pouco à esquerda). Lençol **azul royal acetinado** com **luz laranja forte vindo da esquerda**, sombras azuis, contraste alto. Mãos: luvas pretas, braço tatuado, relógio preto de mostrador preto.
   - Gerar 2 peças grandes de uma vez faz o modelo fundir as duas numa só. Funciona em 2 passos: (a) gerar a disposição certa (pode sair pequena), (b) EDITAR essa imagem: "crop/zoom in so the shirts fill the whole frame… sleeves past the edges… change the sheet to royal blue satin with strong orange light from the left… premium athletic fabric with subtle sheen, not rubbery".
2. **Cama vazia**: editar a imagem do produto: "remove BOTH shirts completely… keep the same sheet, light, camera, gloved hands". Serve de início da cena 1 e fim da cena 5.

## 4. Takes (Google Flow)
- **Modelo: Veo 3.1 Fast (20 créditos).** Nunca o Omni 1.1 Flash (padrão do Flow): é ele que deixava o tecido emborrachado. Veo 3.1 Quality (100) só se o Lucas pedir.
- Conferir antes de gerar: Vídeo · Frames · **9:16** · Veo 3.1 Fast · **x1**. Trocar de modelo pode voltar para 16:9 e o x2 da imagem passa para o vídeo.
- Prompts que funcionaram (em inglês, numa linha):
  - **Esticada longa (cena 2)**: "Static top-down phone camera above a bed… The black-gloved tattooed hands grab the bottom hem of the black shirt, one hand on each side, and stretch the fabric outward… The elastic athletic fabric visibly extends, forms long tension wrinkles and shiny highlights… then snaps back… Then the right palm slides slowly over the print… Both shirts stay big, filling the frame, sleeves cut off by the frame edges… Real fabric physics… not rubbery, no morphing, no extra garments, no text." (o mesmo take dá a cena 4)
  - **Vai e volta (cena 3)**: "…grab the shirt at both sides of the chest and lift it just a little off the bed, then do a gentle, rhythmic stretch-and-release: pull the fabric outward a moderate amount… let it come back… four or five times… Controlled and relaxed, NOT a strong yank, never as if trying to tear it, the shirt never flies… At the end the shirt is laid back flat…"
  - **Jogar (cena 1)**: "The video starts with the empty royal blue satin bed… ends exactly like the end frame. In the first second the hands quickly throw the white shirt onto the bed… right after, they toss the black shirt on top of it, slightly to the left, and smooth it flat… Fast, natural, confident movements…"
  - **Tirar (cena 5)**: "starts exactly like the start frame… ends exactly like the end frame (empty blue bed)… first grab the black shirt by the shoulders and pull it out of the frame toward the bottom, then… the white shirt… One shirt at a time, both removed within the first 6 seconds, nothing ever comes back."
  - Em todo prompt: "same black nitrile gloves, tattoos, black metal wristwatch with black dial".
- Baixar sempre em **1080p**.

## 5. Revisão dos takes (antes de editar)
- Folha a 4 fps de cada take. Cortar: relógio virando claro/dourado (aparece no fim dos takes, ~6 s+), peça trocando de modelo (camisa branca virando manga curta), quadros vazios no início (comece ≥ 0,2 s), puxão brusco.

## 6. Edição (`ferramentas/editar.sh`)
`cortes.txt` do vídeo aprovado:
```
jogar          0.6 3.8 1.3
esticada-longa 0.2 3.2 1.3
vai-e-volta    0.8 5.8 1.3
esticada-longa 3.4 5.6 1.3 1.35 0.4
tirar          0.9 6.5 1.3
```
Comando: `EQ="saturation=1.15:contrast=1.04" HL_STYLE=nativo bash <skill>/ferramentas/editar.sh` (sai 1080x1920, **60 fps**).
- Velocidade **1.3x** (ritmo dele; 1.6x ficou rápido demais).
- Zoom de 1,35x no trecho do close (5ª coluna do cortes.txt).
- Cor: só um leve `saturation=1.15` — a cor vem da imagem (lençol azul), não do filtro.

## 7. Texto
- `HL_STYLE=nativo`: TikTok Sans 700 largura 110, tamanho 41, contorno preto 5 px + halo escuro, a 74,5% da altura. Medido contra o vídeo dele (434×38 px vs 436×38).
- Frase curta, gíria, falando com "tu", sem preço: "Irmão essa aqui é braba", "Essa aqui é padrão ein", "Essa tá padrão demais e no precinho de amigo", "Esse kit com 2 camisas premium é o que tu precisa irmão". Emoji o Lucas põe no app se quiser.

## 8. Entrega
Folha final a 4 fps, conferir o último quadro (cama vazia), abrir o vídeo para o usuário (`Start-Process`), ficha com métricas 48 h / 7 dias.
Custo do vídeo aprovado: ~80 créditos (4 takes Veo Fast) + imagens grátis.

## Métricas que a análise usou (para repetir em outro perfil)
- yt-dlp: views, likes, duração, data/hora de cada vídeo do perfil (frequência de postagem, horários, mediana de views, quantos passaram de 100 mil).
- TikTok Studio (nossos): tempo médio assistido, % até o fim, onde a maioria sai, origem do tráfego.
- FFmpeg/scdet: cortes e duração de cada trecho; `signalstats`: movimento (YDIF), brilho, saturação, contraste; quadros repetidos → fps real e velocidade usada.
- Pixel: % de borda do quadro ocupada pela peça (escala), saturação do lençol, largura/altura do texto.
