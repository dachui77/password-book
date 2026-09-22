const http = require('http');
const fs = require('fs');
const path = require('path');
const PORT = process.env.PORT || 3457;
const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.css': 'text/css',
};
const server = http.createServer((req, res) => {
  let filePath = path.join(__dirname, req.url === '/' ? 'index.html' : decodeURIComponent(req.url.split('?')[0]));
  const ext = path.extname(filePath);
  fs.readFile(filePath, (err, content) => {
    if (err) { res.writeHead(404); res.end('Not found'); }
    else { res.writeHead(200, { 'Content-Type': MIME[ext] || 'text/plain' }); res.end(content); }
  });
});
server.listen(PORT, '0.0.0.0', () => {
  console.log('密码本运行于 http://localhost:' + PORT);
});
