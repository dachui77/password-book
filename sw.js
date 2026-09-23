// Service Worker - 禁用缓存
self.addEventListener('install', function(event) {
  self.skipWaiting();
});

self.addEventListener('activate', function(event) {
  event.waitUntil(
    clients.claim()
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    fetch(event.request).then(function(response) {
      return response;
    }).catch(function() {
      return caches.match(event.request);
    })
  );
});
