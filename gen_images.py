import math
import os
import random

OUT = "/home/claude/sazon-y-mesa/images"


def save(path, content):
    with open(os.path.join(OUT, path), "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------- retratos
def portrait(fname, bg1, bg2, skin, hair, role, style, accent, stubble=False, moustache=False, hat=True):
    ink = "#2A1740"
    s = []
    s.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 750" role="img" aria-label="Foto de ejemplo">')
    s.append(f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient></defs>')
    s.append('<rect width="600" height="750" fill="url(#g)"/>')
    s.append('<circle cx="510" cy="110" r="160" fill="#fff" opacity=".13"/>')
    s.append('<circle cx="60" cy="600" r="200" fill="#fff" opacity=".10"/>')
    s.append('<circle cx="120" cy="170" r="46" fill="#fff" opacity=".12"/>')

    # pelo largo por detrás
    if style == "long":
        s.append(f'<path d="M182 330 C140 450 150 610 185 660 L415 660 C450 610 460 450 418 330 C400 235 200 235 182 330 Z" fill="{hair}"/>')

    # cuerpo
    body = "M40 750 C40 610 160 565 300 565 C440 565 560 610 560 750 Z"
    if role == "chef":
        s.append(f'<path d="{body}" fill="#FFFFFF"/>')
        s.append('<path d="M300 650 L300 750" stroke="#E4DBF0" stroke-width="4"/>')
        for y in (680, 725):
            s.append(f'<circle cx="268" cy="{y}" r="8" fill="#E4DBF0"/><circle cx="332" cy="{y}" r="8" fill="#E4DBF0"/>')
    else:
        s.append(f'<path d="{body}" fill="{ink}"/>')
        s.append('<path d="M240 565 L300 700 L360 565 Z" fill="#FFFFFF"/>')
        s.append('<path d="M240 565 L300 700 M360 565 L300 700" stroke="#4A2F66" stroke-width="5" fill="none"/>')

    # cuello y sombra
    s.append(f'<rect x="262" y="470" width="76" height="120" rx="32" fill="{skin}"/>')
    s.append('<ellipse cx="300" cy="528" rx="62" ry="26" fill="#000" opacity=".14"/>')

    # pañuelo del chef / moño del mesero
    if role == "chef":
        s.append(f'<path d="M238 566 Q300 612 362 566 L300 650 Z" fill="{accent}"/>')
    else:
        s.append(f'<path d="M300 598 L252 574 L252 622 Z M300 598 L348 574 L348 622 Z" fill="{accent}"/><circle cx="300" cy="598" r="12" fill="{accent}"/>')

    # orejas y cabeza
    s.append(f'<ellipse cx="198" cy="412" rx="18" ry="30" fill="{skin}"/><ellipse cx="402" cy="412" rx="18" ry="30" fill="{skin}"/>')
    s.append(f'<ellipse cx="300" cy="400" rx="102" ry="124" fill="{skin}"/>')

    if stubble:
        s.append(f'<path d="M199 412 C204 520 396 520 401 412 C391 482 360 502 300 502 C240 502 209 482 199 412 Z" fill="{hair}" opacity=".5"/>')

    # pelo frontal
    s.append(f'<path d="M198 398 C190 270 410 270 402 398 C394 346 356 322 300 322 C244 322 206 346 198 398 Z" fill="{hair}"/>')
    if style == "bun":
        s.append(f'<circle cx="300" cy="238" r="50" fill="{hair}"/>')

    # rasgos
    s.append('<circle cx="250" cy="446" r="22" fill="#FF6A6A" opacity=".16"/><circle cx="350" cy="446" r="22" fill="#FF6A6A" opacity=".16"/>')
    s.append(f'<circle cx="257" cy="402" r="9" fill="{ink}"/><circle cx="343" cy="402" r="9" fill="{ink}"/>')