# szszszsz 무료 테스트 페이지 만들기: python build.py
# 헤더·푸터는 szszszsz.com 홈과 같고, 결과 끝은 네이버 카페로 연결됩니다.
import json, os

HOME = "https://szszszsz.com"
CAFE = "https://cafe.naver.com/s2s2s2s2s2s2s2s2"
BASE = "https://quiz.szszszsz.com"
HERE = os.path.dirname(os.path.abspath(__file__))
IMG = "https://szszszszcom.wordpress.com/wp-content/uploads/2026/10/sz-{}.png?resize=1200,630"
OG_IMG = {"crush-test": "hero-mind", "attraction-test": "hero-pull", "reply-test": "hero-talk",
          "love-style-test": "hero-love", "jealousy-test": "hero-envy", "conflict-test": "hero-fight", "tarot": "card-1"}


def seo_head(slug, name, desc, url):
    """공유 미리보기(카카오톡·페이스북 등)와 검색엔진용 구조화 데이터."""
    img = IMG.format(OG_IMG[slug])
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": name, "description": desc, "url": url,
          "inLanguage": "ko-KR", "image": img, "isAccessibleForFree": True,
          "isPartOf": {"@type": "WebSite", "name": "szszszsz", "url": HOME + "/"},
          "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "szszszsz", "item": HOME + "/"},
              {"@type": "ListItem", "position": 2, "name": name, "item": url}]}}
    return "\n".join([
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="szszszsz">',
        '<meta property="og:locale" content="ko_KR">',
        f'<meta property="og:image" content="{img}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'])


CSS = r""":root{--bg:#1f1a3a;--card:#fff;--ink:#2a2728;--pink:#e8a0b4;--rose:#c86b7e;--soft:#f8f1f3;--muted:#8a8488;--line:#ece4e7}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;display:flex;flex-direction:column;background:radial-gradient(circle at 50% 0,#3a2f63 0,var(--bg) 60%);color:var(--ink);font:17px/1.55 "Bitter",serif;word-break:keep-all}
a{color:inherit}
/* ── 홈페이지(szszszsz.com)와 같은 헤더 ── */
.site-hd{background:#fff;border-bottom:1px solid #f0eaec;padding:0 32px;display:flex;flex-wrap:nowrap;justify-content:space-between;align-items:center;gap:16px;font-family:"Bitter",serif;position:relative;z-index:5}
.site-logo{color:#c86b7e;font-size:24px;font-weight:700;line-height:1;text-decoration:none;text-transform:uppercase}
.site-nav{display:flex;justify-content:center;gap:24px;padding:16px 0;font-size:15px;line-height:1.5}
.site-nav a{color:#2a2a2a;text-decoration:none}.site-nav a:hover{color:#c86b7e}
.site-act{display:flex;align-items:center;gap:8px;flex-shrink:0}
.site-cafe{display:inline-flex;align-items:center;font:13px "Bitter",serif;color:#c86b7e;border:1.5px solid #c86b7e;border-radius:999px;padding:7px 16px;text-decoration:none;line-height:1.2;white-space:nowrap}
.site-cafe:hover{background:#c86b7e;color:#fff}
.site-menu{display:none;background:none;border:0;padding:16px 0;cursor:pointer;color:#2a2a2a}
@media(max-width:600px){.site-hd{padding:0 16px;gap:10px}.site-logo{font-size:21px}.site-cafe{font-size:12px;padding:6px 12px}.site-menu{display:block;margin-left:auto}.site-nav{display:none;position:absolute;top:100%;left:0;right:0;background:#fff;flex-direction:column;gap:0;padding:8px 16px;border-bottom:1px solid #f0eaec}.site-nav.open{display:flex}.site-nav a{padding:10px 0}}
/* ── 홈페이지와 같은 푸터 ── */
.site-ft{background:#1f1a3a;color:#d9d1e6;padding:56px 24px 32px;font-family:"Bitter",serif}
.site-ft a{color:#d9d1e6;text-decoration:none}.site-ft a:hover{text-decoration:underline}
.ft-in{max-width:1080px;margin:0 auto}
.ft-cols{display:flex;gap:32px}.ft-cols>div{flex:1}.ft-cols>div:first-child{flex:0 0 34%}
.ft-brand{color:#e8a0b4;font-size:22px;font-weight:700;margin:0 0 16px;text-transform:uppercase}.ft-brand a{color:#e8a0b4}
.ft-tag{font-size:14px;line-height:1.7;margin:0}
.ft-h{color:#e8a0b4;font-size:12px;font-weight:600;letter-spacing:.15em;margin:0 0 12px}
.ft-cols ul{list-style:none;padding:0;margin:0;font-size:14px;line-height:2}
.ft-hr{border:0;height:1px;background:#3a3360;margin:28px 0}
.ft-biz{text-align:center;color:#9b93b3;font-size:12px;line-height:1.8;margin:0 0 16px}.ft-biz a{color:#9b93b3}
@media(max-width:781px){.ft-cols{flex-direction:column;gap:28px}.ft-cols>div:first-child{flex-basis:auto}}
main{flex:1;padding:24px 16px 36px}
.wrap{max-width:520px;margin:0 auto}
.brand{text-align:center;color:var(--pink);font-size:12px;letter-spacing:.3em;margin:4px 0 14px}
.card{background:var(--card);border-radius:22px;padding:24px 22px 28px;box-shadow:0 18px 50px rgba(0,0,0,.35)}
h1{font:400 30px/1.25 "Young Serif",serif;margin:6px 0 10px;text-align:center}
.lead{color:#5d575b;text-align:center;margin:0 0 20px}
.btn{display:block;width:100%;border:0;border-radius:14px;padding:15px 18px;font:600 16px system-ui,sans-serif;cursor:pointer;text-align:center;text-decoration:none}
.main{background:var(--rose);color:#fff}.main:hover{background:#b45a6d}
.opt{background:var(--soft);color:var(--ink);border:1.5px solid var(--line);text-align:left;margin-top:10px;font-weight:500;transition:transform .08s,border-color .15s}
.opt:hover{border-color:var(--pink)}.opt:active{transform:scale(.98)}
.opt.on{border-color:var(--rose);background:#fbe4ea}
.top{display:flex;justify-content:space-between;align-items:center;margin:-4px 0 12px}
.back{background:none;border:0;color:var(--rose);font:600 14px system-ui,sans-serif;cursor:pointer;padding:6px 0}
.meta{font-size:13px;color:var(--muted)}
.bar{height:6px;background:var(--line);border-radius:3px;overflow:hidden;margin-bottom:22px}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--pink),var(--rose));transition:width .3s}
.q{font:400 22px/1.4 "Young Serif",serif;margin:0 0 8px}
.hearts{color:var(--rose);font-size:30px;text-align:center;letter-spacing:4px;margin:4px 0}
.meter{position:relative;height:12px;background:var(--line);border-radius:6px;margin:14px 0 6px;overflow:hidden}.meter i{position:absolute;inset:0 auto 0 0;background:linear-gradient(90deg,var(--pink),var(--rose));border-radius:6px;animation:g 1s ease-out}@keyframes g{from{width:0}}
.pct{text-align:center;font-size:13px;color:var(--muted)}
.tag{text-align:center;color:var(--rose);font-size:12px;letter-spacing:.25em}
.res h2{font:400 28px/1.3 "Young Serif",serif;text-align:center;margin:6px 0 12px}
.res p{margin:0 0 12px}
.tips{background:var(--soft);border-radius:14px;padding:14px 16px;margin:14px 0}.tips b{display:block;font-size:12px;letter-spacing:.18em;color:var(--rose);margin-bottom:6px}
.tips li{margin:4px 0}
.mix{margin:14px 0 4px}.mix .r{display:grid;grid-template-columns:120px 1fr 38px;gap:8px;align-items:center;font-size:13px;margin:6px 0}.mix .t{height:8px;background:var(--line);border-radius:4px;overflow:hidden}.mix .t i{display:block;height:100%;background:linear-gradient(90deg,var(--pink),var(--rose));animation:g 1s ease-out}.mix .r.top{font-weight:600;color:var(--rose)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:14px 0}.two>div{background:var(--soft);border-radius:14px;padding:12px 14px;font-size:14px}.two b{display:block;font-size:11px;letter-spacing:.16em;color:var(--rose);margin-bottom:4px}
.cta{background:var(--bg);color:#fff;border-radius:16px;padding:18px;margin-top:16px;text-align:center}
.cta p{color:#d9d3e8;font-size:14px;margin:0 0 12px}.cta strong{color:#fff;font:400 19px/1.4 "Young Serif",serif;display:block;margin-bottom:6px}
.alt{display:block;text-align:center;color:#d9d3e8;font-size:13px;margin-top:10px}
.row{display:flex;gap:10px;margin-top:12px}.row .btn{flex:1;padding:12px;font-size:14px}
.ghost{background:var(--soft);color:var(--ink)}
.small{font-size:12px;color:var(--muted);text-align:center;margin-top:14px}
.fade{animation:f .25s ease}@keyframes f{from{opacity:0;transform:translateY(6px)}to{opacity:1}}
@media(max-width:420px){.two{grid-template-columns:1fr}.mix .r{grid-template-columns:104px 1fr 34px}}"""

CATS = ["연애", "궁합", "짝사랑", "사주", "운세", "타로"]
NEW = ' target="_blank" rel="noopener"'

HEADER = (
    f'<header class="site-hd"><a class="site-logo" href="{HOME}/">szszszsz</a>'
    '<button class="site-menu" aria-label="메뉴" onclick="document.querySelector(\'.site-nav\').classList.toggle(\'open\')">'
    '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>'
    '<nav class="site-nav">' + "".join(f'<a href="{HOME}/{c}/">{c}</a>' for c in CATS)
    + f'<a href="{CAFE}"{NEW}>커뮤니티</a></nav>'
    f'<div class="site-act"><a class="site-cafe" href="{CAFE}"{NEW}>네이버 카페 가입하기</a></div></header>'
)

FOOTER = (
    '<footer class="site-ft"><div class="ft-in"><div class="ft-cols">'
    f'<div><p class="ft-brand"><a href="{HOME}/">szszszsz</a></p><p class="ft-tag">연애·궁합·짝사랑·사주·운세·타로까지, 마음 이야기를 무료로 나누는 공간이에요.</p></div>'
    '<div><p class="ft-h">카테고리</p><ul>' + "".join(f'<li><a href="{HOME}/{c}/">{c}</a></li>' for c in CATS) + '</ul></div>'
    f'<div><p class="ft-h">커뮤니티</p><ul><li><a href="{CAFE}"{NEW}>네이버 카페 가입하기</a></li><li><a href="{CAFE}"{NEW}>카페에서 고민 나누기</a></li></ul></div>'
    f'<div><p class="ft-h">안내</p><ul><li><a href="{HOME}/소개/">szszszsz 소개</a></li><li><a href="{HOME}/개인정보처리방침/">개인정보처리방침</a></li><li><a href="mailto:contact@haeclass.com">문의하기</a></li></ul></div>'
    '</div><hr class="ft-hr">'
    '<p class="ft-biz">이메일: <a href="mailto:contact@haeclass.com">contact@haeclass.com</a></p>'
    '<p class="ft-biz" style="margin:0;line-height:1.7">© 2026 szszszsz. 모든 콘텐츠는 무료예요.<br>재미와 자기 이해를 위한 내용이며, 전문 상담을 대신하지 않아요.</p>'
    '</div></footer>'
)

# 결과 화면 끝: 네이버 카페 안내 (모든 테스트 공통)
CTA_HEAD = "혼자 고민하지 말고, 함께 이야기해요"
CTA_TEXT = "비슷한 결과를 받은 사람들이 szszszsz 네이버 카페에서 이야기를 나누고 있어요. 내 이야기를 털어놓고 다른 사람들의 생각도 들어 보세요."

# 공통 화면 흐름: -1 시작, 0~(문항수-1) 질문, 문항수 결과. 휴대폰 뒤로가기도 이전 질문으로
ENGINE = r"""
const CAFE=CFG.cafe,HOME=CFG.home,Q=CFG.q;
const app=document.getElementById('app');let ans=[];
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function go(step){history.pushState({step},'');render(step)}
window.onpopstate=e=>render(e.state?e.state.step:-1);
const backBtn='<button class="back" onclick="history.back()">← 이전</button>';
function render(step){if(step<0)return start();if(step>=Q.length)return result();show(step);window.scrollTo(0,0)}
function start(){ans=[];app.innerHTML=`<div class="fade"><div class="hearts">${CFG.icon}</div><h1>${esc(CFG.title)}</h1><p class="lead">${esc(CFG.lead)}</p><button class="btn main" id="go">테스트 시작하기 →</button><p class="small">회원가입도, 이메일도 필요 없어요.</p></div>`;document.getElementById('go').onclick=()=>go(0)}
function show(i){const [q,opts]=Q[i];app.innerHTML=`<div class="fade"><div class="top">${backBtn}<span class="meta">질문 ${i+1} / ${Q.length}</span></div><div class="bar"><i style="width:${i/Q.length*100}%"></i></div><p class="q">${esc(q)}</p>${opts.map((o,k)=>`<button class="btn opt${ans[i]===k?' on':''}" data-k="${k}">${esc(o[0])}</button>`).join('')}</div>`;
app.querySelectorAll('.opt').forEach(b=>b.onclick=()=>{app.querySelectorAll('.opt').forEach(x=>x.classList.remove('on'));b.classList.add('on');ans[i]=+b.dataset.k;setTimeout(()=>go(i+1),180)})}
function tail(name){return `<div class="cta"><strong>${esc(CFG.ctaHead)}</strong><p>${esc(CFG.ctaText)}</p><a class="btn main" href="${CAFE}" target="_blank" rel="noopener">네이버 카페 가입하기 →</a><a class="alt" href="${HOME}/">다른 무료 테스트 더 보기 →</a></div>
<div class="row"><button class="btn ghost" id="sh">결과 공유하기</button><button class="btn ghost" id="re">다시 하기</button></div>`}
function bind(name){document.getElementById('re').onclick=()=>{ans=[];go(0)};
document.getElementById('sh').onclick=async()=>{const txt=CFG.share.replace('{R}',name),url=location.href.split('?')[0].split('#')[0];
try{if(navigator.share){await navigator.share({title:CFG.title,text:txt,url});return}await navigator.clipboard.writeText(txt+' '+url);document.getElementById('sh').textContent='링크가 복사됐어요 ✓'}catch(e){}}}
function result(){if(ans.filter(x=>x!==undefined).length<Q.length)return start();
if(CFG.mode==='score'){
const sc=ans.reduce((s,k,n)=>s+Q[n][1][k][1],0),max=Q.length*3,pct=Math.round(sc/max*100),r=CFG.results.find(x=>sc>=x.min);
app.innerHTML=`<div class="fade res"><div class="top">${backBtn}<span class="tag">${esc(CFG.tag)}</span></div><div class="hearts">${r.h}</div><h2>${esc(r.t)}</h2><div class="meter"><i style="width:${pct}%"></i></div><div class="pct">${esc(CFG.meter)}: ${pct}%</div><p style="margin-top:14px">${esc(r.s)}</p><div class="tips"><b>${esc(CFG.tipsLabel)}</b><ul style="margin:0;padding-left:18px">${r.tips.map(t=>`<li>${esc(t)}</li>`).join('')}</ul></div>${tail(r.t)}</div>`;
return bind(r.t)}
const T=CFG.types,ORDER=Object.keys(T).join('');
const c={};Object.keys(T).forEach(k=>c[k]=0);ans.forEach((k,n)=>c[Q[n][1][k][1]]++);
const last=Q[Q.length-1][1][ans[Q.length-1]][1];
const top=Object.keys(c).sort((a,b)=>c[b]-c[a]||(b===last)-(a===last)||ORDER.indexOf(a)-ORDER.indexOf(b))[0],r=T[top];
const mix=Object.keys(c).sort((a,b)=>c[b]-c[a]||(a===top?-1:b===top?1:0)).map(k=>`<div class="r${k===top?' top':''}"><span>${esc(T[k].short)}</span><span class="t"><i style="width:${Math.round(c[k]/Q.length*100)}%"></i></span><span>${Math.round(c[k]/Q.length*100)}%</span></div>`).join('');
app.innerHTML=`<div class="fade res"><div class="top">${backBtn}<span class="tag">${esc(CFG.tag)}</span></div><div class="hearts">${r.e}</div><h2>${esc(r.name)}</h2><p>${esc(r.s)}</p><div class="mix">${mix}</div>
<div class="two"><div><b>${esc(CFG.labels[0])}</b>${esc(r.str)}</div><div><b>${esc(CFG.labels[1])}</b>${esc(r.watch)}</div></div><div class="tips"><b>${esc(CFG.labels[2])}</b>${esc(r.tip)}</div><p class="small" style="margin-top:0">${esc(r.saju)}</p>${tail(r.name)}</div>`;
bind(r.name)}
history.replaceState({step:-1},'');start();
"""

from tests import TESTS  # 테스트 내용 (질문·결과)


def page(slug, t):
    cfg = dict(t["cfg"], cafe=CAFE, home=HOME, ctaHead=CTA_HEAD, ctaText=CTA_TEXT)
    url = f"{BASE}/{slug}/"
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['seo_title']} | szszszsz</title>
<meta name="description" content="{t['desc']}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{cfg['title']}">
<meta property="og:description" content="{t['desc']}">
<meta property="og:url" content="{url}">
{seo_head(slug, t['seo_title'], t['desc'], url)}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bitter:wght@400;500;600;700&family=Young+Serif&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
{HEADER}
<main><div class="wrap">
  <div class="brand">{t['brand']}</div>
  <div class="card" id="app"></div>
  <p class="small" style="color:#9d95b8">{t['note']}</p>
</div></main>
{FOOTER}
<script>
const CFG={json.dumps(cfg, ensure_ascii=False)};
{ENGINE.strip()}
</script>
</body>
</html>
"""


NAVER_VERIFY = '<meta name="naver-site-verification" content="ae3f82f22de0e5cc1af71d34288a0f4fbc46f3ea" />'


def index_page():
    """quiz.szszszsz.com 첫 화면: 무료 테스트 목록 (네이버 소유확인 태그 포함)."""
    items = "".join(
        f'<a class="btn opt" href="{BASE}/{s}/" style="display:block;text-decoration:none">'
        f'<b>{t["cfg"]["icon"]} {t["cfg"]["title"]}</b><br><span class="small" style="text-align:left;display:block;margin:4px 0 0">{t["desc"]}</span></a>'
        for s, t in TESTS.items())
    items += (f'<a class="btn opt" href="{BASE}/tarot/" style="display:block;text-decoration:none">'
              f'<b>🔮 무료 연애 타로</b><br><span class="small" style="text-align:left;display:block;margin:4px 0 0">카드 한 장으로 보는 지금 그 사람의 마음</span></a>')
    desc = "연애·썸·짝사랑·이별 무료 심리 테스트와 연애 타로. 회원가입 없이 1분이면 결과를 볼 수 있어요."
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>무료 연애 심리 테스트 모음 | szszszsz</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}/">
{NAVER_VERIFY}
<meta property="og:title" content="무료 연애 심리 테스트 모음 | szszszsz">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bitter:wght@400;500;600;700&family=Young+Serif&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
{HEADER}
<main><div class="wrap">
  <div class="brand">무료 연애 테스트</div>
  <div class="card">
    <h1>무료 연애 심리 테스트</h1>
    <p class="lead">썸, 짝사랑, 연애, 이별까지. 회원가입 없이 1분이면 결과를 볼 수 있어요.</p>
    {items}
  </div>
</div></main>
{FOOTER}
</body>
</html>
"""


def main():
    for slug, t in TESTS.items():
        os.makedirs(os.path.join(HERE, slug), exist_ok=True)
        with open(os.path.join(HERE, slug, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(page(slug, t))
    import tarot
    os.makedirs(os.path.join(HERE, "tarot"), exist_ok=True)
    with open(os.path.join(HERE, "tarot", "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(tarot.page(CSS, HEADER, FOOTER, CAFE, HOME, BASE, seo_head))
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(index_page())
    with open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        f.write(f'  <url><loc>{BASE}/</loc><lastmod>2026-10-09</lastmod></url>\n')
        f.writelines(f'  <url><loc>{BASE}/{s}/</loc><lastmod>2026-10-08</lastmod></url>\n' for s in list(TESTS) + ["tarot"])
        f.write('</urlset>\n')
    import share  # 결과 화면 공유 바 (카카오톡·라인·스레드 등)
    share.apply(HERE, "ko")
    print("만든 테스트:", ", ".join(TESTS))


if __name__ == "__main__":
    main()
