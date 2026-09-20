const http = require('http');
const fs = require('fs');
const path = require('path');
const PORT = process.env.PORT || 18923;

const server = http.createServer((req, res) => {
  let filePath = path.join(__dirname, req.url === '/' ? 'index.html' : req.url);
  const ext = path.extname(filePath);
  const types = {'.html':'text/html', '.js':'application/javascript', '.css':'text/css', '.json':'application/json'};
  fs.readFile(filePath, (err, content) => {
    if(err){ res.writeHead(404); res.end('Not found'); }
    else{ res.writeHead(200, {'Content-Type': types[ext]||'text/plain'}); res.end(content); }
  });
});
server.listen(PORT, '0.0.0.0', () => {
  console.log('Password Book running at:');
  console.log('  Local:   http://localhost:' + PORT);
  console.log('  Network: http://192.168.3.229:' + PORT);
});
