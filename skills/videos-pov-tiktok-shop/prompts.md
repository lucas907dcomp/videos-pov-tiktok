# Banco de prompts POV

Textos ORIGINAIS da biblioteca VSA Ultra e do Doc de prompts, copiados em 2026-10-16.
Não acesse a biblioteca: use daqui. Na hora de usar, aplique só a "Adaptação masculina" do SKILL.md.
Busque pelo id: `## <id> ·`.

# Imagens (montar a cena) · Nano Banana Pro no Flow, 9:16

## 2 · Remover roupas/textos
- Uso: Limpa um print de vídeo de referência (tira roupa, mãos, textos). Trocar a descrição do cenário pelo que aparece no print.
- Entrada: 1: print

```text
Remove all clothing pieces, the model’s hands and arms, all text, captions, interface elements, search bar, play button, progress bar, timestamps and any other overlays from the image. Keep only the original environment: the white fluffy rug, the wicker basket, the green plant and the visible wooden floor. Preserve exactly the same top-down camera angle, framing, composition, lighting, colors, texture and image proportions. Naturally reconstruct the rug and background in the areas where the clothes, hands and text were removed, without visible marks, distortions or shadows from the deleted objects. Do not change, move, resize or add anything to the environment. The final image must look like the same scene photographed completely empty.
```

## 3 · Colocando a mão no ambiente
- Uso: Põe as mãos no cenário vazio. Já temos a imagem pronta (imagens/base-maos-cama.jpg); só use se precisar refazer, com o kit da mão.
- Entrada: 1: cenário vazio

```text
Use Image 1 as the BASE scene.

TASK:
Add a pair of feminine hands into the scene, positioned naturally over the surface, matching the same top-down flat lay style and the same hand placement shown in the original composition.

IMPORTANT RULES:
• Preserve the environment from Image 1 exactly
• Preserve the white fluffy rug exactly
• Preserve the wicker basket exactly
• Preserve the green leaf exactly
• Preserve the visible wooden floor exactly
• Preserve the camera angle exactly
• Preserve the lighting exactly
• Preserve the composition exactly
• Preserve the perspective exactly
• Do not modify the background in any way

HAND DETAILS:
• Add two feminine hands with fair/light skin tone
• The hands must look elegant and natural
• Nails should be painted with light-colored polish.
• Add subtle accessories, such as delicate bracelets
• Add at least one ring
• Add a small minimalist tattoo on one of the hands or wrist area
• The tattoo should be subtle and aesthetic
• The hands should look realistic and proportional

HAND POSITION (CRITICAL):
• The hands must appear in the same lower area of the image
• One hand should be positioned on the lower left side
• One hand should be positioned on the lower right side
• Both hands should be slightly angled inward toward the center
• Fingers should be naturally relaxed and slightly curved
• The pose should feel like the person is about to arrange or present an item in the center
• Keep the hand pose natural, balanced, and symmetrical
• Show part of the forearms, entering from the bottom edges of the frame

SCENE LOCK:
• Do NOT add clothing
• Do NOT add text
• Do NOT add logos
• Do NOT add watermarks
• Do NOT add interface elements
• Do NOT change the decor
• Do NOT create a new environment
• Do NOT stylize the image

FINAL QUALITY:
• Ultra photorealistic
• Natural skin texture
• Realistic nails
• Realistic jewelry details
• Natural shadows
• Natural integration with the scene
• Looks like a real photograph
• No AI artifacts
```

## 4 · Colocar roupa no ambiente
- Uso: Coloca a peça do produto na cena com as mãos. Base dos vídeos.
- Entrada: 1: cena com mãos · 2: produto

```text
Use Image 1 as the base scene for the environment.
Use Image 2 ONLY as a reference for the clothing.
TASK:
Remove the clothing item from Image 1 and include the clothing item from Image 2.
The clothing from Image 2 must appear naturally arranged within the environment; maintain the size of real clothing.
IMPORTANT RULES:
• Preserve the environment from Image 1 exactly
• Preserve the environment exactly
• Preserve the camera angle exactly
• Preserve the lighting exactly
• Preserve the composition exactly
• Preserve the perspective exactly
HAND CONSISTENCY (CRITICAL):
• Keep the exact same hands from Image 1 • Keep the exact same skin tone • Keep the exact same manicure • Keep the exact same accessories (rings, bracelets, watches, if present) • Keep the exact same rings (if present) • Keep the exact same hand position • Keep the exact same arm position • DO NOT generate new hands • DO NOT modify the hands in any way
CLOTHING REPLACEMENT:
• Remove only the clothing from Image 1 • Include the clothing from Image 2 • Replicate the clothing EXACTLY as shown in Image 2 • Same color • Same fabric • Same shape • Same proportions
same size • No redesigning • No creative interpretation
POSITIONING:
• The clothing must occupy approximately the same area where the original clothing was located
• The clothing item must appear naturally arranged within the environment
• Realistic fabric •
Natural interaction with the environment's surface. • Natural gravity and drape
SCENE MAINTENANCE (CRITICAL):
• Do NOT alter the background • Do NOT alter the environment • Do NOT alter furniture (if present) • Do NOT alter environmental details • Do NOT alter the lighting • Do NOT create a new scene
FINAL QUALITY:
• Ultra-photorealistic • Natural shadows • Realistic fabric texture • 4K real-photo look • No AI artifacts
EXCLUSIONS:
• No text • No logos • No watermarks • No filters • No stylization
```

## 1 · Recriando cenário
- Uso: Troca a peça numa cena que já tem roupa, como se tivesse saído da embalagem.
- Entrada: 1: cena com mãos+roupa · 2: produto

```text
Use Image 1 as the base scene for the environment.
Use Image 2 ONLY as a reference for the garment.
TASK:
Remove the garment from Image 1 and replace it with the garment from Image 2.
The garment from Image 2 should appear naturally arranged on the bed, as if it had just been taken out of its packaging. IMPORTANT RULES:
• Preserve the environment from Image 1 exactly
• Preserve the environment exactly
• Preserve the camera angle exactly
• Preserve the lighting exactly
• Preserve the composition exactly
• Preserve the perspective exactly

HAND CONSISTENCY (CRITICAL):
• Keep the exact same hands from Image 1 • Keep the exact same skin tone • Keep the exact same manicure • Keep the exact same accessories (rings, bracelets, watches, if present) • Keep the exact same rings (if present) • Keep the exact same hand position • Keep the exact same arm position • DO NOT generate new hands • DO NOT modify the hands in any way
CLOTHING REPLACEMENT:
• Remove only the clothing from Image 1 • Replace it with the clothing from Image 2 • Replicate the clothing EXACTLY as shown in Image 2 • Same color • Same fabric • Same shape • Same proportions • No redesigning • No creative interpretation
POSITIONING:
• The clothing must occupy approximately the same area where the original clothing was located
• The garment must appear naturally arranged on the bed
• Realistic fabric •
Natural interaction with the bed surface
• Natural gravity and drape

SCENE MAINTENANCE (CRITICAL):
• DO NOT alter the background • DO NOT alter the environment • DO NOT alter furniture (if present) • DO NOT alter environmental details • DO NOT alter the lighting • DO NOT create a new scene
FINAL QUALITY:
• Ultra-photorealistic • Natural shadows • Realistic fabric texture • Real 4K photograph appearance • No AI artifacts
EXCLUSIONS:
• No text • No logos • No watermarks • No filters • No stylization
```

## 5 · Roupa no pacote
- Uso: Troca a roupa dentro de um pacote transparente (para o gancho do pacote).
- Entrada: 1: cena com pacote · 2: produto

```text
Use Image 1 as the BASE scene.
Use Image 2 ONLY as the clothing reference.

TASK:
Replace the clothing item currently inside the transparent package with ALL clothing items shown in Image 2.

IMPORTANT:
Preserve the environment from Image 1 exactly.
Preserve the bed exactly.
Preserve the blanket exactly.
Preserve the camera angle exactly.
Preserve the lighting exactly.
Preserve the composition exactly.
Preserve the perspective exactly.
Preserve the plastic package exactly.
Preserve all hands exactly as they appear in Image 1.
Do not create a new scene.
Do not modify the room.
Do not modify the packaging position.

CLOTHING REPLACEMENT:
Remove only the clothing item currently visible inside the package.
Place ALL clothing items from Image 2 inside the same package.
Replicate the clothing exactly as shown in Image 2.
Same color.
Same fabric.
Same design.
Same print.
Same proportions.
No redesign.
No creative interpretation.

PACKING / FOLDING:
If Image 2 contains more than one clothing item, all pieces must be packed together inside the same transparent package, arranged neatly like a real online fashion order.
Fold the clothing naturally and professionally for e-commerce presentation.
Arrange the pieces so they fit realistically inside the package.
If any item contains a front print, graphic, logo, or important design element, fold and position it so the main front design remains clearly visible through the transparent packaging whenever possible.
Maintain realistic fabric folds.
Maintain realistic packaging reflections.
All garments must remain fully inside the package.

FINAL QUALITY:
Ultra photorealistic.
Natural shadows.
Realistic transparent plastic.
Realistic fabric texture.
Looks like a real product photo.
No AI artifacts.

EXCLUSIONS:
No text.
No logos added.
No watermark.
No filters.
No stylization.
```

## 6 · Colocar embalagem do TikTok
- Uso: Põe o pacote preto do TikTok Shop nas mãos. Ordem das imagens: primeiro o ambiente, depois o pacote. O pacote deve ser pequeno.
- Entrada: A: cena com mãos · B: pacote

```text
Create a realistic overhead product image using two references.
Image A = the empty environment scene with only the model’s hands visible.
Image B = the package reference.

Use Image A as the main base for the scene. Preserve the exact same environment, background, surface, framing, lighting, camera angle, hand position style, skin tone, maintain your nail color.

Add the package from Image B into the model’s hands, so the model is naturally holding the package in the scene.

IMPORTANT:
– The package must appear clearly visible in the hands
– Show the FRONT side of the package
– The shipping label must face the camera
– The label should be readable and fully visible from the front
– The package must look naturally held, centered, and well positioned
– The hands must hold the package firmly and realistically from both sides, similar to a natural product presentation
– The package must keep the same black plastic material, proportions, folds, and front label appearance as the reference
– Do not change the package design
– Do not redesign the label
– Do not replace the package with another one

The final image should look like the model is presenting the package for a TikTok Shop product reveal, with the package clearly shown in front view.

Keep the camera completely fixed in a top-down overhead angle.
No camera movement.
No extra objects.
No product outside the package.
No distorted hands.
No extra fingers.
No deformed package.
No label changes.
No background changes.

Final result:
A clean, realistic overhead product image where the model is naturally holding the package with both hands, clearly showing the front side of the package and its label, using the empty environment as the main base.
```

# Vídeos · Google Flow, vertical 9:16

## 43 · Gancho esticar rápido POV
- Uso: Pega a peça de cima, estica forte 3x perto da câmera, devolve; repete com a próxima. ~10s, com áudio de tecido.
- Entrada: imagem do card 4

```text
Ultra-realistic vertical POV video. Static camera, fixed high-angle top-down. No camera movement, no zoom, no panning, no shaking. The surface, lighting, framing, background props and the arrangement of the garments remain exactly as in the reference image at all times. Approximately 10 seconds.

SETUP: the garments lie on the surface exactly as in the reference image. The hands, skin tone, nails, rings, watch and bracelets are preserved exactly as shown.

GRIP RULE — READ THE GARMENT: the hands always grip the garment at its stretchiest structural point, chosen according to what the garment is.
- If it is a TOP — shirt, tank, blouse, bodysuit, sweater — both hands grip the fabric across the BUST, one hand on each side, and pull outward horizontally.
- If it is a BOTTOM — trousers, jeans, shorts, skirt, leggings — both hands grip the WAISTBAND, one hand at each side of it, and pull outward horizontally.
The grip is firm and full-handed, never pinching a corner, never gripping a sleeve, hem or strap.

SEQUENCE:
0-1s: Both hands rest on the garments as in the reference image, then take hold of the TOP garment — the one lying uppermost, closest to the camera — and lift it off the stack.

1-4s: The hands bring that garment up close to the camera until it fills most of the frame, gripping it at its correct stretch point per the grip rule. They pull it apart outward with real force — a quick, committed stretch — hold the tension for a beat, release back, and repeat. THREE distinct stretches in a row, each one brisk and deliberate, the release between them fast and clean.

4-5s: The hands lower that garment back down and lay it flat on the surface in its exact original position, orientation and layering, exactly as it sat in the reference image. They release it and it settles.

5-6s: The hands take hold of the NEXT garment in the stack — the one now lying uppermost — and lift it off.

6-9s: They bring it up close to the camera the same way, grip it at its correct stretch point per the grip rule, and pull it apart outward with real force. THREE distinct stretches in a row, same brisk committed rhythm.

9-10s: The hands lower it back down and lay it flat in its exact original position, orientation and layering. The final frame matches the reference image arrangement.

FABRIC BEHAVIOUR — MATCH THE MATERIAL: the fabric stretches according to what it actually is. Ribbed knit, jersey, spandex blends and seamless stretch fabrics extend visibly and elastically, the weave opening under tension and snapping back tight on release. Woven cotton, denim, poplin and structured fabrics barely give at all, going taut with almost no extension and holding their shape. Never make a rigid fabric behave like elastic, and never make a stretch fabric behave like it is stiff. On release the fabric recovers with real speed and settles naturally, with no permanent deformation.

CONTINUITY: only the garment currently being handled ever moves. Every other garment stays completely still in its exact position, orientation and layering order for the whole clip — never touched, dragged, shifted, lifted, uncovered or rearranged. Only the garments from the reference image ever appear; never invent, duplicate, swap, add or remove any garment. Each garment keeps the exact same color, cut, neckline, seams, stitching and proportions throughout, and any printed graphic keeps the same text, letterforms, size and position, sharp and undistorted.

REALISM: real fabric physics with natural weight, drape, tension and recoil, visible weave and stitch detail, folds forming under the pull and releasing on the return. Real skin texture with visible knuckles, veins, tendons flexing under the pull, fine hair and natural nails, no beauty smoothing. Jewellery, watch and bracelets stay exactly as shown and in place. Spontaneous unchoreographed hand movement with subtle human imperfection, small grip adjustments between stretches. Natural available light from the existing scene with soft realistic shadows. Shot on a phone camera, handheld feel with only the faintest organic drift.

PACING: brisk, energetic and purposeful, at real human speed — the stretches are quick and forceful, like someone demonstrating durability, not delicately presenting it. Continuous from first frame to last, no dead air, no frozen poses, no slow motion.

AUDIO: soft fabric tension and stretch sounds on each pull, light rustle on each release and as each garment is laid down, plus quiet room tone. No dialogue, no voiceover, no music, no sound effects, no background noise.

NEGATIVE: no dialogue, no voiceover, no music, no text overlay, no captions, no cuts, no camera movement, no zoom, no pan, no shake, no slow motion, gripping a sleeve or hem or strap, pinching a corner, stretching the wrong part of the garment, rigid fabric stretching like elastic, stretch fabric behaving stiffly, fabric tearing, fabric permanently deformed, garment not returning to its original position, other garments moving, shifting, dragging or being uncovered, wrong layering order on return, switching garments, invented garments, duplicated garments, extra clothing, changing colors, changing prints, warping text, object morphing, clipping, hand deformation, finger distortion, extra fingers, plastic skin, jewellery changing or disappearing, changes to the surface or background.
```

## 7 · Gancho esticar a roupa
- Uso: Estica a peça de cima devagar, em loop. Corrigir o erro de digitação "Ωproducts".
- Entrada: imagem do card 4

```text
Create a realistic overhead product video using the provided image as the main reference. Keep the camera completely fixed from a top-down view. Preserve the same carpet background, lighting, framing, hands, skin tone, nails, and the exact arrangement of the clothing pieces.
The video should focus only on the top/front piece — the first visible piece on top. The hands gently pick up only this piece and hold it from both sides, showing the fabric clearly. Then the hands softly stretch the fabric outward in a natural way, not too hard, just enough to show the material and elasticity. Hold for a brief moment, then relax slightly, and stretch the same piece again. Repeat this same action smoothly during the video: stretch, hold, relax a little, and stretch again.
Only this single clothing piece should move. The other pieces underneath or behind it must remain in the same position the whole time and should not be touched, removed, or rearranged.
The motion must be slow, controlled, and natural, as if someone is demonstrating the quality of the fabric. Keep the same hands visible throughout the video. No sudden movements.
No camera movement, no zoom, no cuts, no transitions, no changing clothes, no extra Ωproducts, no switching pieces, no distorted hands, no deformed fabric, and no movement in the other garments.
If needed, end with the piece still being held neatly in front of the other items, maintaining a clean product showcase look.
```

## 11 · Gancho pacote transparente
- Uso: Rasga o pacote transparente com som e levanta a peça. ~5s. ATIVAR SOM NO FLOW.
- Entrada: imagem do card 5

```text
Static camera. No camera movement. No zoom. No panning. No shaking.
The clothing item remains neatly folded inside the transparent package.
The woman’s hands firmly grip both sides of the package opening.
With a quick and realistic motion, she tears the plastic package open from the center.
The plastic stretches naturally and creates realistic tearing behavior.
At the exact moment the package is torn open, include a clear, crisp, and realistic plastic ripping sound.

The tearing sound must be perfectly synchronized with the movement of the hands and the plastic.
The sound should resemble a real transparent clothing package being firmly ripped open.
Include natural plastic stretching, crinkling, and tearing sounds during the opening motion.
The tearing sound should feel strong, satisfying, and impactful, creating an engaging viral unboxing effect.
Immediately after tearing, both hands pull the torn plastic away from the garment.
The packaging is completely removed from the clothing.
The empty plastic is pulled out of the frame and does not remain covering the garment.

Include subtle and realistic plastic crinkling sounds as the empty packaging is removed from the frame.

The folded clothing remains centered on the surface.

Without pause, both hands grab the garment from both sides.

The garment is lifted smoothly as a single physical object.

No duplicate clothing.
No second garment.
No remaining copy on the surface.
The same garment is lifted upward toward the camera.
The front side of the garment faces the camera.
The hands slightly adjust the garment to showcase the front design, print, texture, and details.
The garment is presented close to the camera for a brief moment.
Include subtle, natural fabric movement sounds while the garment is lifted and adjusted.
Keep the audio clean, realistic, and synchronized with every action.
No music.
No voice.
No talking.
No artificial sound effects.
No unnecessary background noise.
Fast but realistic product reveal.
Natural fabric movement.
Natural gravity.
Smooth hand coordination.
Realistic interaction between hands, packaging, and clothing.
No object morphing.
No clipping.
No hand deformation.
No finger distortion.
No extra fingers.
No camera movement.

Ultra-realistic TikTok Shop product reveal.
Total duration approximately 5 seconds.
The entire sequence should feel quick, satisfying, and natural, like a viral fashion unboxing reveal.
```

## 12 · Gancho embalagem TikTok Shop (PT)
- Uso: Rasga o pacote preto e tira as peças uma por uma. Editar ROUPA 1/2/3. ATIVAR SOM NO FLOW.
- Entrada: imagem do card 6

```text
Use a imagem/vídeo de referência como base.
Câmera fixa, vista de cima, sem zoom, sem movimento de câmera e sem cortes.

As mãos devem rasgar o pacote e, em seguida, retirar as roupas que estão dentro dele, uma por uma.

SEQUÊNCIA OBRIGATÓRIA:
1. Primeiro: A ROUPA 1
2. Segundo: A ROUPA 2
3. Terceiro: A ROUPA 3

IMPORTANTE:
As roupas devem sair de dentro do pacote preto.
Não criar nenhuma roupa nova.
Não trocar as peças.
Não puxar roupas que já estão fora do pacote.
Manter exatamente o modelo, cor, tecido e aparência das roupas da referência.
Depois de retirar cada peça, colocar a roupa sobre a superfície, ao lado das outras peças, seguindo a organização mostrada na imagem de referência.
As roupas devem aparecer de forma natural, como em um verdadeiro vídeo de unboxing.
Movimentos das mãos realistas e suaves.
Não alterar o ambiente, iluminação, superfície ou enquadramento.
Manter o pacote e as roupas visualmente consistentes durante todo o vídeo.

A ação deve ser simples e contínua: abrir o pacote → colocar a mão dentro → retirar a roupa de dentro do pacote → colocar a roupa na superfície → repetir com a próxima peça.

O PACOTE PRETO NÃO PODE DESAPARECER, SER REMOVIDO AUTOMATICAMENTE OU MUDAR DE POSIÇÃO DURANTE O VÍDEO. Depois de retirar a última roupa, as mãos devem pegar fisicamente o pacote e retirá-lo da cena. O pacote só deve sair da cena nesse momento.
Vídeo ultra-realista, aparência de gravação real para TikTok Shop.
```

## 10 · Gancho jogar roupa — opção 2 (PT)
- Uso: Tira as peças do quadro e recoloca. Duas versões: ESPECÍFICO (descreva cada peça) e PADRÃO.
- Entrada: imagem do card 4

```text
ESPECÍFICO (descreva a roupa)
Crie um vídeo realista de produto com a câmera totalmente fixa em uma visão superior (top-down). Mantenha a câmera perfeitamente imóvel durante toda a cena. Preserve exatamente o mesmo fundo, iluminação, enquadramento e sombras naturais.
As mãos pegam delicadamente o SHORTS PRETO e a retiram completamente para fora do campo de visão da câmera, depois as mãos pegam delicadamente a BLUSA PRETA e também a retiram completamente para fora do campo de visão.
Em seguida as mãos pegam delicadamente o SHORTS MARROM e também a retiram completamente para fora do campo de visão e por último as mãos pegam delicadamente a BLUSA BRANCA e também a retiram completamente para fora do campo de visão.
Após um breve momento, as mãos colocam as peças de roupa de volta exatamente em sua posição original, recriando exatamente a mesma disposição inicial das peças.
Todos os movimentos devem ser lentos, suaves e extremamente naturais, como se uma pessoa estivesse organizando as roupas. Não altere o ângulo da câmera, o enquadramento, a iluminação ou o fundo. Não faça movimentos de câmera, zoom, cortes ou transições.
PADRÃO
Crie um vídeo realista de produto com a câmera totalmente fixa em uma visão superior (top-down). Mantenha a câmera perfeitamente imóvel durante toda a cena. Preserve exatamente o mesmo fundo, iluminação, enquadramento e sombras naturais.
As mãos pegam delicadamente cada peça de roupa e a retiram completamente para fora do campo de visão da câmera.
Após um breve momento, as mãos colocam as peças de roupas exatamente em sua posição original. Em seguida, recriando exatamente a mesma disposição inicial das peças.
Todos os movimentos devem ser lentos, suaves e extremamente naturais, como se uma pessoa estivesse organizando as roupas. Não altere o ângulo da câmera, o enquadramento, a iluminação ou o fundo.
Não faça movimentos de câmera, zoom, cortes ou transições.
```

## 15 · Mostrar o tecido de perto
- Uso: Pega uma peça, leva perto da câmera e passa os dedos no tecido. 8s. Trocar "blouse" pela peça certa.
- Entrada: imagem do card 4

```text
Create a realistic 8-second overhead product video using the provided image as the main reference. Keep the camera completely fixed in a top-down position. Preserve the same carpet background, lighting, framing, feminine hands, white nails, bracelets, and the clothing arrangement.
The hands should pick up only one blouse from the arrangement in a natural way. After picking it up, gently stretch the blouse a little to show the fabric, then bring it closer to the camera without moving the camera itself. While holding the blouse near the camera, use the fingers to softly rub and slide over the fabric, showing the texture and quality of the material. The movement should look smooth, elegant, and natural, like a product showcase.
After showing the fabric up close, keep the blouse well positioned in the hands, with the material clearly visible. The action should focus only on this single blouse.
No camera movement, no zoom, no cuts, no transitions, no extra products, no switching pieces, no distorted hands, and no deformed fabric.
```

## 13 · Passar a mão na roupa
- Uso: Peça fica na cama; mãos abrem e mostram detalhes (alça, gola, costura). Até 2 peças.
- Entrada: imagem do card 4

```text
Create a realistic overhead product showcase video using the provided image as the main reference. Keep the camera completely fixed in a top-down position. Preserve the same bed or fabric surface, lighting, framing, hands, nails, and all clothing pieces exactly as they appear.

The clothes must remain lying on the bed during the whole video. The hands should not lift the clothing too much. Instead, the hands gently touch and handle the pieces while they stay mostly resting on the bed.

The hands should interact with only one piece at a time, and during the whole video they may show one or at most two products from the arrangement.

For the first product, the hands gently hold the garment and open it slightly to reveal the details. If the piece has straps, lightly lift and show the straps. If it has a neckline, gently open and show the neckline. If needed, slightly spread the fabric to show the shape, stitching, cut, texture, or design. The motion should feel like a seller carefully presenting the product details while keeping the piece mostly in place on the bed.

The hands can also softly pull a small area of the fabric, smooth it with the fingers, lightly open the front area, and show the important details in a natural and elegant way. The piece should never be fully removed from the bed or lifted too high.

After showing the first piece, place it back exactly as it was. Then, if a second product is shown, repeat the same action: gently touch it, slightly open or spread it, show details like straps, neckline, cut, or fabric texture, and keep the piece mostly resting on the bed.

The motion should be smooth, slow, elegant, and natural, like a product-detail presentation video. The other garments must remain still and untouched.

No camera movement, no zoom, no cuts, no transitions, no fast motion, no removing the clothing from the bed, no shaking, no distorted hands, no deformed fabric, and no handling multiple pieces at the same time.
```

## 39 · Passar a mão na roupa + zoom
- Uso: Igual ao 13, com aproximação sutil da câmera no tecido. Mesmo texto do card 38.
- Entrada: imagem do card 4

```text
Create a realistic overhead product showcase video using the provided image as the main reference. Preserve the same bed or fabric surface, lighting, framing, hands, nails, and all clothing pieces exactly as they appear.
The clothes must remain lying on the bed during the whole video. The hands should not lift the clothing too much. Instead, the hands gently touch and handle the pieces while they stay mostly resting on the bed.
The hands should interact with only one piece at a time, and during the whole video they may show one or at most two products from the arrangement.
For the first product, the hands gently hold the garment and open it slightly to reveal the details. If the piece has straps, lightly lift and show the straps. If it has a neckline, gently open and show the neckline. If needed, slightly spread the fabric to show the shape, stitching, cut, texture, or design. The motion should feel like a seller carefully presenting the product details while keeping the piece mostly in place on the bed.
The hands can also softly pull a small area of the fabric, smooth it with the fingers, lightly open the front area, and show the important details in a natural and elegant way.
IMPORTANT FABRIC FOCUS:
While one hand slowly slides and passes over the fabric, the framing should gradually move slightly closer to the product, creating a very subtle and smooth close-up effect.
The approach must be gentle and minimal.
Do not move extremely close to the product.
The goal is only to slightly emphasize the fabric texture, stitching, and material while the hand is touching and sliding over it.
The subtle close-up should happen gradually while the hand moves across the fabric, then remain stable for a brief moment.
The product must still remain clearly recognizable and mostly visible in the frame.
Do not crop the product excessively.
Do not create a dramatic zoom.
Do not suddenly jump closer.
Use only a soft, slow, subtle push-in toward the product.
The piece should never be fully removed from the bed or lifted too high.
After showing the first piece, place it back exactly as it was. Then, if a second product is shown, repeat the same action: gently touch it, slightly open or spread it, show details like straps, neckline, cut, or fabric texture, and keep the piece mostly resting on the bed.
The motion should be smooth, slow, elegant, and natural, like a product-detail presentation video. The other garments must remain still and untouched.
CAMERA:
Top-down overhead view.
Keep the same camera angle and orientation.
Only allow a VERY SMALL and smooth forward push-in while the hand is passing over the fabric.
No large zoom.
No abrupt camera movement.
No pan.
No rotation.
No shaking.
No cuts.
No transitions.
No fast motion, no removing the clothing from the bed, no distorted hands, no deformed fabric, and no handling multiple pieces at the same time.
FINAL RESULT:
A realistic overhead product showcase where the hand gently slides over the fabric while the view slowly moves slightly closer to emphasize the material and texture, without getting too close or changing the original composition dramatically.
```

## 38 · Abrir zíper + zoom
- Uso: O texto é IDÊNTICO ao 39 e não fala em zíper: use o texto do 39 + a linha do zíper (ver SKILL.md, "Zíper no Flow").
- Entrada: imagem do card 4

## 14 · Mostrar as peças
- Uso: Pega 2 peças, uma de cada vez, mostra perto da câmera, estica e devolve.
- Entrada: imagem do card 4

```text
Create a realistic overhead product showcase video using the provided image as the main reference. Keep the camera completely fixed in a top-down position at all times. Preserve the same carpet background, lighting, framing, clothing arrangement, feminine hands, nails, and bracelets.
The hands should interact with only one clothing piece at a time. Choose two pieces only from the arrangement. First, the hands gently pick up one piece from its place on the bed/carpet, lift it closer to the camera to show the details clearly, softly stretch or pull the fabric a little to demonstrate the material, hold it for a brief moment, and then place it back neatly in the exact same original position.
After that, the hands move to a second clothing piece and repeat the same action: pick up only that one piece, bring it closer to the camera, show the details, gently stretch the fabric a little, hold briefly, and then place it back in the same exact place.
The movements should look elegant, smooth, controlled, and natural. The camera must remain still the whole time. The other clothing pieces that are not being handled must remain in place and should not move.
No camera movement, no zoom, no cuts, no transitions, no changing arrangement, no picking up two pieces at the same time, no extra products, no distorted hands, and no deformed fabric.
```

## 8 · Gancho tapar câmera e pegar produto
- Uso: Mostra detalhes na cama e, no fim, a palma tampa 100% da câmera (transição).
- Entrada: imagem do card 4

```text
Create a realistic overhead product showcase video using the provided image as the main reference. Keep the camera completely fixed in a top-down position, directly overhead. Preserve exactly the same bed or fabric surface, lighting, framing, hands, nails, and all clothing pieces as they appear in the image.

The clothes must remain lying on the bed throughout the entire video. The hands should not lift the clothing excessively. Instead, they should gently touch and handle the pieces while keeping them mostly resting on the bed.

The hands must interact with only one piece at a time and, throughout the entire video, may present only one or, at most, two products from the arrangement.

For the first product, the hands gently hold the garment and slightly open it to reveal its details. If the piece has straps, gently lift them to show them. If it has a neckline, gently open the area to show the neckline. If necessary, slightly spread the fabric to reveal the shape, stitching, cut, texture, or design. The movement should feel like a seller carefully presenting the product details while keeping the garment mostly in the same position on the bed.

The hands may also gently pull a small area of the fabric, smooth it with the fingers, slightly open the front area, and show the important details in a natural and elegant way. The piece must never be completely removed from the bed or lifted too high.

After presenting the first piece, place it back exactly as it was. Then, if a second product is presented, repeat the same action: gently touch the piece, slightly open or spread it, show details such as straps, neckline, cut, or fabric texture, and keep the piece mostly resting on the bed.

The movement should be smooth, slow, elegant, and natural, like a detailed product presentation video. All other garments must remain completely still and untouched.

FINAL CAMERA-COVER TRANSITION:

Only begin this action after the product presentation has been completely finished.

Only one hand begins a continuous movement toward the camera lens, as if reaching out to touch the viewer.

* Gently rotate until the palm is facing the camera — a natural rotation of the arm/forearm, without forcibly bending or twisting the wrist.
* The movement travels in a straight line along the lens axis, approaching the camera frontally, simulating a POV perspective of the camera being "touched."
* Maintain a constant, controlled speed: neither abrupt nor hesitant — a fluid movement from beginning to end.

*Lens coverage:*

* The palm progressively approaches until it fills 100% of the frame, with no gaps visible around the edges.
* The final contact should create the sensation of completely physically blocking the camera lens, with a slight natural blur from proximity during the final frames before full coverage.

*Final state (mandatory):*

* The camera remains completely covered by the left palm until the cut.
* There must be absolutely no movement away from the lens, no opening of the fingers, and no partial reveal of the scene after the lens is covered.
* The final frame must show only the palm, filling 100% of the frame, with no part of the previous scene visible.

*Suggested duration:* approximately 1 to 1.5 seconds, so the movement is clearly visible without feeling slow or dragged out.

IMPORTANT:

– Perform the entire normal product presentation first
– Cover the camera only at the very end
– Do not interrupt the product presentation prematurely
– No sudden hand movements
– No aggressive movements
– Do not twist the wrist
– Do not deform the fingers
– Do not create extra fingers
– Do not generate deformed hands
– The palm must completely fill the camera view in the final frame

Do not move the camera, do not apply zoom, do not use cuts, do not add transitions before the final camera-cover action, do not use fast movements, do not remove the clothes from the bed, do not shake the camera, do not deform the hands, do not deform the fabric, and do not handle multiple pieces at the same time.

FINAL RESULT:
A realistic continuous POV product showcase in which the hands naturally demonstrate the clothing exactly as described and, only at the very end, one hand smoothly approaches the lens and completely covers the camera with the palm, ending the video with the view fully covered to create a clean transition into the next scene.
```

## colocar · Colocar peças na cama uma por uma (Doc)
- Uso: Usa 2 imagens no Flow: frame Início (cama com mãos) e Fim (arranjo final).
- Entrada: Início: cena com mãos · Fim: imagem do card 4

```text
Create a realistic top-down product placement video using the provided opening image as the starting frame and the provided final arrangement image as the ending reference.
The camera must stay completely fixed in an overhead view. Keep the same carpet background, lighting, framing, shadows, and the same feminine hands with the same nails and accessories.
Very important: the hands must handle only one single clothing piece at a time. Never pick up, hold, or place two pieces together.
The action should happen step by step:
the hands bring in one piece only
gently place or lightly toss this single piece into its exact final position
adjust it naturally remove the hands
then bring in the next single piece
place it in its correct final position
repeat the same process until all pieces are arranged
Each piece must be placed separately, one after another, never simultaneously. No stacking two pieces in the hands, no overlapping placement action with multiple items at once.
The items must appear in a logical order based on the final arrangement. Start with one piece, place it correctly, then move on to the next, until the final layout matches the reference image exactly.
The movements should be smooth, natural, and slightly slow — not rushed. The hands should look like they are organizing the products carefully on the bed/carpet.
The final frame must match the reference arrangement exactly, with the same quantity of pieces, same colors, same orientation, same spacing, and same placement.
No camera movement, no zoom, no cuts, no transitions, no morphing, no teleporting items, no extra products, no duplicated items, no missing items, no deformed hands, and absolutely no picking up two pieces at the same time.
```

## fechamento · Fechamento: tirar peças da cama uma por uma (Doc)
- Uso: Termina com a cama vazia.
- Entrada: imagem do card 4

```text
Create a realistic overhead closing video using the provided image as the starting reference. Keep the camera completely fixed in a top-down position. Preserve the same carpet background, lighting, framing, feminine hands, nails, bracelets, and the exact clothing arrangement.
The video starts with all clothing pieces already arranged in place. Then the hands begin removing the pieces one by one, not all at once. Each time, the hands pick up only one single piece, pull it smoothly out of the scene to the side, and then come back to remove the next one.
The process should continue step by step:
pick up one piece only
remove it from the frame
return the hands
pick up the next piece only
remove it from the frame
repeat until all pieces are gone
The movements should be smooth, elegant, controlled, and slightly slow. Never remove two pieces together. Never drag all the pieces at once. Each item must leave the scene separately.
The other pieces should remain in place until it is their turn to be removed. The hands should look natural and consistent the whole time.
By the end of the video, all clothing pieces must be removed from the frame, leaving only the empty background visible, creating a clean closing shot.
No camera movement, no zoom, no cuts, no transitions, no extra products, no distorted hands, no deformed fabric, and no removing multiple pieces at once.
```
