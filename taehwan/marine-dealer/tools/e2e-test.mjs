// 크롬 원격 제어(CDP)로 마린딜러 등록 흐름을 실제로 돌려 본다.
import { spawn } from 'node:child_process';
import { mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PAGE = 'file:///C:/Users/GG/OneDrive/Documents/llm-academy/marine-dealer/index.html';
const ASSETS = 'C:\\Users\\GG\\OneDrive\\Documents\\llm-academy\\marine-dealer\\assets\\';
const SHOT = process.argv[2];
const prof = mkdtempSync(join(tmpdir(), 'md-e2e-'));
const ch = spawn(CHROME, ['--headless=new', '--remote-debugging-port=9333', `--user-data-dir=${prof}`, '--window-size=1280,1000', 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));

let ws, id = 0; const pend = new Map(); const errors = [];
async function connect() {
  for (let i = 0; i < 40; i++) { try { const l = await (await fetch('http://127.0.0.1:9333/json')).json(); const p = l.find(x => x.type === 'page'); if (p) return p.webSocketDebuggerUrl; } catch {} await sleep(250); }
  throw new Error('no chrome');
}
const send = (method, params = {}) => new Promise((ok, no) => { const i = ++id; pend.set(i, { ok, no }); ws.send(JSON.stringify({ id: i, method, params })); });
const ev = async (expr) => { const r = await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true }); if (r.exceptionDetails) throw new Error(JSON.stringify(r.exceptionDetails).slice(0, 400)); return r.result.value; };

try {
  ws = new WebSocket(await connect());
  await new Promise(r => ws.onopen = r);
  ws.onmessage = m => { const d = JSON.parse(m.data); if (d.id && pend.has(d.id)) { const p = pend.get(d.id); pend.delete(d.id); d.error ? p.no(d.error) : p.ok(d.result); }
    if (d.method === 'Runtime.exceptionThrown') errors.push(d.params.exceptionDetails.exception?.description || d.params.exceptionDetails.text);
    if (d.method === 'Log.entryAdded' && /Content Security|Refused/i.test(d.params.entry.text)) errors.push('CSP: ' + d.params.entry.text); };
  await send('Runtime.enable'); await send('Log.enable'); await send('Page.enable'); await send('DOM.enable');
  await send('Page.navigate', { url: PAGE }); await sleep(2500);

  const run = async (label, nm, owner, idName, man, file) => {
    await ev(`document.getElementById('sellBtn').click()`); await sleep(300);
    await ev(`(()=>{const f=document.getElementById('sellForm'); f.type.value='motor'; f.nm.value=${JSON.stringify(nm)}; f.ft.value=36; f.yr.value=2018; f.port.value='gwangan'; f.man.value=${man}; f.owner.value=${JSON.stringify(owner)}; f.idName.value=${JSON.stringify(idName)}; f.d1.value='no'; f.d2.value='unk'; f.agree.checked=true; return 1;})()`);
    const { root } = await send('DOM.getDocument'); const { nodeId } = await send('DOM.querySelector', { nodeId: root.nodeId, selector: '#sfPhotos' });
    await send('DOM.setFileInputFiles', { nodeId, files: [ASSETS + file] });
    await ev(`document.getElementById('sfPhotos').dispatchEvent(new Event('change')); document.getElementById('sfSubmit').click(); 1`);
    await sleep(2500);
    const res = await ev(`(()=>{const b=document.getElementById('sellResult'); return b.hidden?('FORM ERR: '+document.getElementById('ferr').textContent):b.innerText.replace(/\\s+/g,' ').slice(0,400);})()`);
    console.log(`\n[${label}]`, res);
    await ev(`document.getElementById('sellDlg').close(); 1`);
  };

  await run('정상 등록 (새 사진·명의 일치·시세 범위)', '파도소리', '홍길동', '홍길동', 98000, 'listing-03.jpg'.replace('listing-03','yacht-06-cabin'));
  await run('사기 의심 (하늘빛 사진 재사용·명의 불일치·저가)', '푸른바다', '김OO', '이OO', 3000, 'fraud-027.jpg');

  const cards = await ev(`[...document.querySelectorAll('#cards .lcard')].map(c=>c.querySelector('.nm').textContent+' | '+(c.classList.contains('blocked')?'BLOCKED':'')+' '+(c.querySelector('.badges').innerText.replace(/\\s+/g,' '))).join('\\n')`);
  console.log('\n[목록]\n' + cards);
  const tx = await ev(`[...document.querySelectorAll('#txlist .tx b')].map(b=>b.textContent).join(' / ')`);
  console.log('\n[사기 탐지 목록]', tx);

  // 새로 고침 뒤에도 남는지
  await send('Page.reload'); await sleep(3000);
  const after = await ev(`[...document.querySelectorAll('#cards .lcard .nm')].map(n=>n.textContent).join(' / ')`);
  console.log('\n[새로 고침 뒤 목록]', after);

  // 에스크로 진행 저장
  await ev(`document.getElementById('tab-t2').click(); document.getElementById('nextBtn').click(); document.getElementById('nextBtn').click(); 1`); await sleep(300);
  await send('Page.reload'); await sleep(2500);
  console.log('\n[새로 고침 뒤 에스크로]', await ev(`document.getElementById('mHeld').textContent+' | '+document.getElementById('navStep').textContent`));

  // 사기 탐지 화면 캡처
  await ev(`document.getElementById('tab-t3').click(); 1`); await sleep(800);
  const shot = await send('Page.captureScreenshot', { format: 'png' });
  (await import('node:fs')).writeFileSync(SHOT, Buffer.from(shot.data, 'base64'));
  console.log('\n[에러]', errors.length ? errors.join('\n') : '없음');
} catch (e) { console.log('TEST ERROR', e.message, '\n', errors.join('\n')); }
finally { try { ws && ws.close(); } catch {} ch.kill(); }
