# 결과 공유 바 (s2s2s2s2 · szszszsz 테스트 페이지 공통)
# 사용법: python share.py <폴더> <ko|en>  → 폴더 안 모든 */index.html 결과 화면에 같은 공유 바를 넣습니다.
# 버튼: 카카오톡 · 라인 · 스레드 · 페이스북 · X · 링크 복사 · 더보기(휴대폰 공유창: 인스타그램·문자 등)
# KAKAO_KEY에 카카오 JavaScript 키를 넣으면 카카오톡 버튼이 카톡 공유창을 바로 엽니다.
# 키가 없으면 휴대폰에서는 공유창(카카오톡 선택 가능), PC에서는 링크를 복사합니다.
import glob, io, os, re, sys

KAKAO_KEY = ""

TEXT = {
    "ko": dict(title="결과 공유하기", labels=["카카오톡", "라인", "스레드", "페이스북", "X", "링크 복사", "더보기"],
               msg="{T} 결과는 '{R}'! 너도 해 봐 🔮", copied="복사됐어요 ✓", kakao="링크 복사됨! 카톡에 붙여넣기"),
    "en": dict(title="Share your result", labels=["KakaoTalk", "LINE", "Threads", "Facebook", "X", "Copy link", "More"],
               msg='{T}: I got "{R}". Try it yourself!', copied="Copied ✓", kakao="Link copied ✓"),
}

CSS = (".shr{margin:16px 0 4px;text-align:center}.shr p{margin:0 0 10px;font:600 13px system-ui,sans-serif;color:#8a8488;letter-spacing:.08em}"
       ".shr-b{display:flex;justify-content:center;gap:10px 8px;flex-wrap:wrap}"
       ".shr-b button{background:none;border:0;padding:0;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:5px;width:58px;font:12px system-ui,sans-serif;color:#5d575b}"
       ".shr-b i{width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;font:700 17px system-ui,sans-serif;font-style:normal;transition:transform .1s}"
       ".shr-b button:active i{transform:scale(.92)}#sh{display:none!important}")

ICONS = [
    ("k", "background:#FEE500;color:#3c1e1e",
     '<svg width="24" height="24" viewBox="0 0 24 24"><path fill="#3c1e1e" d="M12 4C7 4 3 7.1 3 11c0 2.5 1.7 4.7 4.2 5.9l-.9 3.3c-.1.3.3.6.6.4l3.9-2.6c.4 0 .8.1 1.2.1 5 0 9-3.1 9-7.1S17 4 12 4z"/></svg>'),
    ("l", "background:#06C755;color:#fff;font-size:11px", "LINE"),
    ("t", "background:#000;color:#fff", "@"),
    ("f", "background:#1877F2;color:#fff", "f"),
    ("x", "background:#111;color:#fff", "𝕏"),
    ("c", "background:#f0eaec;color:#2a2728", "🔗"),
    ("m", "background:#f0eaec;color:#2a2728", "⋯"),
]

JS = r"""(function(){var L=__L__,K=__K__,app=document.getElementById('app');if(!app)return;
function u(){return location.href.split('?')[0].split('#')[0]}
function t(){var h=document.querySelector('.res h2'),n=document.title.split(' | ')[0].split(' - ')[0];return h?L.msg.replace('{T}',n).replace('{R}',h.textContent.trim()):n}
function flash(b,m){var s=b.querySelector('span'),o=s.textContent;s.textContent=m;setTimeout(function(){s.textContent=o},2200)}
function copy(){var v=t()+' '+u();if(navigator.clipboard)return navigator.clipboard.writeText(v).then(function(){return true},function(){return old(v)});return Promise.resolve(old(v))}
function old(v){var a=document.createElement('textarea');a.value=v;document.body.appendChild(a);a.select();var ok=false;try{ok=document.execCommand('copy')}catch(e){}a.remove();return ok}
function nat(){if(!navigator.share)return false;navigator.share({title:document.title,text:t(),url:u()}).catch(function(){});return true}
var mob=/Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
function kakao(b){if(K){var go=function(){if(!Kakao.isInitialized())Kakao.init(K);Kakao.Share.sendDefault({objectType:'text',text:t(),link:{mobileWebUrl:u(),webUrl:u()},buttonTitle:L.labels[0]})};
if(window.Kakao)return go();var s=document.createElement('script');s.src='https://t1.kakaocdn.net/kakao_js_sdk/2.7.4/kakao.min.js';s.onload=go;document.head.appendChild(s);return}
if(mob&&nat())return;copy().then(function(){flash(b,L.kakao)})}
function open(w){window.open(w,'_blank','noopener,width=600,height=520')}
function act(a,b){if(a==='k')return kakao(b);if(a==='f')return open('https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(u()));
if(a==='l')return open('https://social-plugins.line.me/lineit/share?url='+encodeURIComponent(u())+'&text='+encodeURIComponent(t()));
if(a==='t')return open('https://www.threads.net/intent/post?text='+encodeURIComponent(t()+' '+u()));
if(a==='x')return open('https://twitter.com/intent/tweet?text='+encodeURIComponent(t())+'&url='+encodeURIComponent(u()));
if(a==='m'&&nat())return;copy().then(function(){flash(b,L.copied)})}
function add(){var sh=document.getElementById('sh');if(!sh||app.querySelector('.shr'))return;var row=sh.closest('.row')||sh.parentNode;
row.insertAdjacentHTML('beforebegin',__BAR__);app.querySelectorAll('.shr-b button').forEach(function(b){b.onclick=function(){act(b.dataset.a,b)}})}
new MutationObserver(add).observe(app,{childList:true,subtree:true});add()})();"""


def block(lang):
    L = TEXT[lang]
    bar = '<div class="shr"><p>' + L["title"] + '</p><div class="shr-b">' + "".join(
        f'<button type="button" data-a="{a}"><i style="{st}">{ic}</i><span>{lab}</span></button>'
        for (a, st, ic), lab in zip(ICONS, L["labels"])) + "</div></div>"
    import json
    js = (JS.replace("__L__", json.dumps(L, ensure_ascii=False)).replace("__K__", json.dumps(KAKAO_KEY))
          .replace("__BAR__", json.dumps(bar, ensure_ascii=False)))
    return f"<!--SHARE--><style>{CSS}</style><script>{js}</script><!--/SHARE-->"


def apply(folder, lang):
    done = []
    for p in sorted(glob.glob(os.path.join(folder, "*", "index.html"))):
        s = io.open(p, encoding="utf-8").read()
        if 'id="sh"' not in s:
            continue
        s = re.sub(r"<!--SHARE-->.*?<!--/SHARE-->", "", s, flags=re.S)
        s = s.replace("</body>", block(lang) + "\n</body>", 1)
        io.open(p, "w", encoding="utf-8", newline="\n").write(s)
        done.append(os.path.basename(os.path.dirname(p)))
    return done


if __name__ == "__main__":
    print(apply(sys.argv[1], sys.argv[2]))
