# 🔐 Password Book

一个单文件密码管理器，支持离线使用，无需服务器。

## 使用方法

### 直接打开

1. 打开 Safari 浏览器
2. 按 `Cmd + O`（或 文件 → 打开...）
3. 选择文件：`/Users/linus/Documents/Codex/password-book/index.html`
4. 输入密码：**admin123**

### 终端快速打开

```bash
open /Users/linus/Documents/Codex/password-book/index.html
```

## 功能

- 保存网站账号密码（谷歌、甲骨文等）
- 密码强度检测与生成
- 从浏览器/密码管理器导入（Chrome/Firefox/Safari CSV，Bitwarden/1Password JSON）
- 导出为 CSV/JSON
- **支持 TOTP 双因素认证（2FA）**
- 数据存储在浏览器本地（IndexedDB）

## 双因素认证 (2FA)

### 启用步骤（在登录页面操作）

1. 打开应用，在密码输入框下方找到 **"+ 启用 2FA"** 按钮
2. 点击后会出现二维码和密钥
3. 用 Authenticator App 扫描二维码（支持 Google/Microsoft Authenticator、1Password、Authy）
4. 在 App 中查看生成的 6 位验证码
5. 输入验证码，点击 **"确认已添加"** 完成设置

### 登录时

1. 输入访问密码（默认：`admin123`）
2. 如已启用 2FA，需再输入 Authenticator App 中的 6 位验证码

### 重要提示

- 请妥善保管恢复密钥，丢失将无法找回账户
- 可在登录页面点击 **"关闭 2FA"** 随时禁用
- 2FA 密钥保存在浏览器本地，不上传任何服务器

## 导入密码

### Chrome / Edge
1. 访问 `chrome://settings/passwords`
2. 点击右上角 ⋮ → **导出密码**
3. 下载 CSV 后在本应用上传

### Firefox
1. 访问 `about:logins`
2. 右上角 ⋮ → **导出登录名**
3. 下载 CSV 后上传

### Bitwarden
1. Bitwarden → 设置 → 导出账户数据
2. 选择 JSON 格式
3. 在本应用上传

## GitHub Pages 部署（多设备同步）

1. 将本仓库推送到 GitHub
2. 进入 Settings → Pages → Source: main branch
3. 访问 `https://用户名.github.io/password-book`
