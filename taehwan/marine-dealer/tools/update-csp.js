// index.html 안의 <script> 내용으로 CSP 해시를 계산해 <meta http-equiv="Content-Security-Policy">를 넣거나 고친다.
// 스크립트를 고친 뒤에는 반드시 다시 실행: node tools/update-csp.js
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const file = path.join(__dirname, '..', 'index.html');
let html = fs.readFileSync(file, 'utf8');

const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
if (!scripts.length) throw new Error('inline <script> not found');
const hashes = scripts.map(js => `'sha256-${crypto.createHash('sha256').update(js, 'utf8').digest('base64')}'`);

const policy = [
  "default-src 'none'",
  `script-src ${hashes.join(' ')}`,
  "style-src 'unsafe-inline'",          // 단일 파일이라 <style>과 style 속성을 씀. 서버로 옮기면 해시/nonce로 바꾼다.
  "img-src 'self' data: blob: file:",   // file: 은 발표용 로컬 실행 때문. 서버에 올릴 때 지운다.
  "font-src 'self'",
  "manifest-src 'self' file:",
  "worker-src 'self'",
  "connect-src 'none'",
  "base-uri 'none'",
  "form-action 'none'",
  "object-src 'none'"
].join('; ');

const meta = `<meta http-equiv="Content-Security-Policy" content="${policy}">`;
if (/<meta http-equiv="Content-Security-Policy"[^>]*>/.test(html)) {
  html = html.replace(/<meta http-equiv="Content-Security-Policy"[^>]*>/, meta);
} else {
  html = html.replace('<meta charset="utf-8">', `<meta charset="utf-8">\n${meta}`);
}
fs.writeFileSync(file, html);
console.log('CSP updated:', hashes.join(' '));
