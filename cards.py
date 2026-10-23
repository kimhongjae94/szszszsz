# 결과 공유 카드: 테스트마다 결과별로
#   <폴더>/r/<번호>/story.png  (1080x1920, 인스타 스토리·카톡 이미지 공유용)
#   <폴더>/r/<번호>/og.png     (1200x630, 링크 미리보기용)
#   <폴더>/r/<번호>/index.html (친구가 링크를 열면 "OO 결과" 미리보기 + "나도 해 보기" 버튼)
# build.py 가 자동으로 부릅니다.
import html, os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
# 상업용·이미지 포함 무료 글꼴 (넥슨 메이플스토리). 없으면 맑은 고딕.
FONT_CANDIDATES = [
    r"D:\Jinjusung\Jinjusung\Assets\00_Project\Resources\Fonts\Maplestory.ttf",
    os.path.join(HERE, "fonts", "Maplestory.ttf"),
    r"C:\Windows\Fonts\malgunbd.ttf",
]
FONT = next(p for p in FONT_CANDIDATES if os.path.exists(p))

PINK, DEEP, CREAM = (200, 107, 126), (44, 37, 80), (251, 243, 238)


def results_of(t):
    """[(번호, 결과 이름, 한 줄 설명, 하트 수 0~4)]"""
    c = t["cfg"]
    if c["mode"] == "score":
        return [(str(i), r["t"], r["s"], r["h"].count("♥")) for i, r in enumerate(c["results"])]
    return [(k, v["name"], v["s"], 0) for k, v in c["types"].items()]


def first_sentence(s, limit=60):
    for mark in (". ", "요. ", "다. "):
        i = s.find(mark)
        if 0 < i < limit:
            return s[: i + 1].strip()
    return s if len(s) <= limit else s[:limit].rstrip() + "…"


def wrap(draw, text, font, width):
    """단어(띄어쓰기) 단위로 줄 바꿈 — 단어가 중간에서 잘리지 않게."""
    lines, cur = [], ""
    for word in text.split(" "):
        test = (cur + " " + word).strip()
        if draw.textlength(test, font=font) <= width or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def gradient(w, h):
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        t = y / (h - 1)
        col = tuple(int(DEEP[i] * (1 - t) + (82, 52, 96)[i] * t) for i in range(3))
        for x in range(w):
            px[x, y] = col
    return img


def heart(draw, cx, cy, r, fill):
    draw.ellipse([cx - r, cy - r, cx, cy], fill=fill)
    draw.ellipse([cx, cy - r, cx + r, cy], fill=fill)
    draw.polygon([(cx - r, cy - r * 0.35), (cx + r, cy - r * 0.35), (cx, cy + r)], fill=fill)


def card(w, h, test_title, name, line, hearts):
    img = gradient(w, h)
    d = ImageDraw.Draw(img)
    s = w / 1080
    big = h > w
    f_brand = ImageFont.truetype(FONT, int(40 * s))
    f_test = ImageFont.truetype(FONT, int((54 if big else 46) * s))
    f_name = ImageFont.truetype(FONT, int((96 if big else 74) * s))
    f_line = ImageFont.truetype(FONT, int((46 if big else 36) * s))
    f_cta = ImageFont.truetype(FONT, int((44 if big else 36) * s))
    pad = int(90 * s)
    inner = w - pad * 2

    def center(text, font, y, fill):
        tw = d.textlength(text, font=font)
        d.text(((w - tw) / 2, y), text, font=font, fill=fill)

    y = int((150 if big else 50) * s)
    center("szszszsz · 무료 이혼 테스트" if "이혼" in test_title else "톡할까 말까 · 무료 연애 테스트", f_brand, y, (232, 160, 180))
    y += int((110 if big else 70) * s)
    for ln in wrap(d, test_title, f_test, inner):
        center(ln, f_test, y, (230, 222, 240))
        y += int(f_test.size * 1.35)

    # 결과 상자
    name_lines = wrap(d, name, f_name, inner - int(80 * s))
    desc_lines = wrap(d, line, f_line, inner - int(80 * s)) if big else []
    box_h = int(80 * s) + len(name_lines) * int(f_name.size * 1.3) + (int(40 * s) + len(desc_lines) * int(f_line.size * 1.5) if desc_lines else 0)
    if hearts:
        box_h += int(110 * s)
    box_top = y + int((70 if big else 26) * s)
    if big:  # 스토리: 결과 상자를 화면 가운데쯤에 (위아래 빈 곳 고르게)
        box_top = max(box_top, int((h - box_h) / 2 - 40 * s))
    d.rounded_rectangle([pad, box_top, w - pad, box_top + box_h], radius=int(48 * s), fill=CREAM)
    yy = box_top + int(40 * s)
    if hearts:
        r = int(34 * s)
        total = 4 * r * 2 + 3 * int(22 * s)
        x0 = (w - total) / 2 + r
        for i in range(4):
            heart(d, x0 + i * (2 * r + int(22 * s)), yy + r, r, PINK if i < hearts else (232, 214, 220))
        yy += int(110 * s)
    for ln in name_lines:
        center(ln, f_name, yy, DEEP)
        yy += int(f_name.size * 1.3)
    if desc_lines:
        yy += int(40 * s)
        for ln in desc_lines:
            center(ln, f_line, yy, (110, 96, 120))
            yy += int(f_line.size * 1.5)

    # 아래: 나도 해 보기
    cta_y = h - int((330 if big else 120) * s)
    btn_w = int(760 * s)
    d.rounded_rectangle([(w - btn_w) / 2, cta_y, (w + btn_w) / 2, cta_y + int(118 * s)], radius=int(60 * s), fill=PINK)
    center("너도 해 봐 → quiz.szszszsz.com", f_cta, cta_y + int(34 * s), (255, 255, 255))
    return img


def result_page(base, slug, t, rid, name, line):
    test_url = f"{base}/{slug}/"
    url = f"{base}/{slug}/r/{rid}/"
    title = f"내 결과는 '{name}' · {t['cfg']['title']}"
    desc = f"{first_sentence(line)} 너도 무료로 해 봐!"
    e = html.escape
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="noindex">
<link rel="canonical" href="{test_url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{url}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{url}og.png">
<style>
body{{margin:0;background:#2c2550;font-family:system-ui,-apple-system,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;word-break:keep-all}}
.w{{max-width:440px;margin:0 auto;padding:24px 16px 40px;text-align:center}}
img{{width:100%;border-radius:18px;display:block}}
a.b{{display:block;margin:18px 0 0;padding:16px;border-radius:999px;background:#c86b7e;color:#fff;font-weight:700;font-size:18px;text-decoration:none}}
p{{color:#d9d2ea;font-size:14px}}
</style>
</head>
<body><div class="w">
<img src="story.png" alt="{e(title)}">
<a class="b" href="{test_url}">나도 무료로 해 보기 →</a>
<p>회원가입 없이 1분이면 끝나요</p>
</div></body>
</html>
"""


def build(base, tests):
    made = 0
    for slug, t in tests.items():
        for rid, name, line, hearts in results_of(t):
            folder = os.path.join(HERE, slug, "r", rid)
            os.makedirs(folder, exist_ok=True)
            short = first_sentence(line, 70)
            card(1080, 1920, t["cfg"]["title"], name, short, hearts).save(os.path.join(folder, "story.png"), optimize=True)
            card(1200, 630, t["cfg"]["title"], name, short, hearts).save(os.path.join(folder, "og.png"), optimize=True)
            with open(os.path.join(folder, "index.html"), "w", encoding="utf-8", newline="\n") as f:
                f.write(result_page(base, slug, t, rid, name, line))
            made += 1
    return made
