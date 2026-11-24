// 마린딜러 PWA 서비스 워커 (오프라인에서도 첫 화면이 열리게 함)
// https:// 또는 http://localhost 에서만 동작한다. 파일을 더블클릭해 연 file:// 에서는 등록하지 않는다.
const CACHE = 'marinedealer-v3';
const SHELL = [
  './', './index.html', './manifest.webmanifest',
  './assets/logo-64.png', './assets/logo-128.png', './assets/icon-192.png', './assets/icon-512.png',
  './assets/character-sheet.jpg', './assets/yacht-01-main.jpg', './assets/us-oceanis-evansmogor.jpg', './assets/fonts/PretendardVariable.woff2'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// 같은 출처의 GET 요청만 다룬다. 먼저 네트워크, 실패하면 캐시.
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  e.respondWith(
    fetch(req)
      .then(res => {
        if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
        return res;
      })
      .catch(() => caches.match(req).then(hit => hit || caches.match('./index.html')))
  );
});
