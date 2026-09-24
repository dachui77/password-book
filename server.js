// Password Book 本地静态服务器
//
// 安全说明（2026-09 修复）：
//   原实现用 path.join(__dirname, decodeURIComponent(req.url)) 直接拼路径，
//   没有校验结果是否仍在项目目录内 —— 请求 /%2e%2e%2f 之类就能读取
//   项目目录之外的任意文件。而且原来监听 0.0.0.0，同一局域网内
//   任何人都能利用该漏洞。
//
//   现在：解析真实路径并强制校验必须位于本目录内，且默认只监听 127.0.0.1。
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3457;
// 如需在手机/平板上访问，显式设置 HOST=0.0.0.0（会暴露到局域网，请谨慎）
const HOST = process.env.HOST || '127.0.0.1';
const ROOT = fs.realpathSync(__dirname);

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.css': 'text/css',
  '.webmanifest': 'application/manifest+json',
};

function resolveSafe(urlPath) {
  let decoded;
  try {
    decoded = decodeURIComponent(urlPath.split('?')[0]);
  } catch {
    return null; // 非法百分号编码
  }
  if (decoded === '/' || decoded === '') decoded = '/index.html';

  // path.resolve 会规范化 ".."，再用 realpath 消除符号链接影响
  const target = path.resolve(ROOT, '.' + decoded);
  if (target !== ROOT && !target.startsWith(ROOT + path.sep)) return null;
  return target;
}

const server = http.createServer((req, res) => {
  const filePath = resolveSafe(req.url || '/');
  if (!filePath) {
    res.writeHead(403, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Forbidden');
    return;
  }

  fs.readFile(filePath, (err, content) => {
    if (err) {
      res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
      res.end('Not found');
      return;
    }
    const ext = path.extname(filePath).toLowerCase();
    res.writeHead(200, {
      'Content-Type': MIME[ext] || 'application/octet-stream',
      'X-Content-Type-Options': 'nosniff',
    });
    res.end(content);
  });
});

server.listen(PORT, HOST, () => {
  console.log(`密码本运行于 http://${HOST}:${PORT}`);
  if (HOST === '0.0.0.0') {
    console.log('⚠️ 已监听所有网卡，同一局域网内的设备都能访问，请仅在可信网络下使用');
  }
});
