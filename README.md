# Anuneko OpenAI Proxy

[简体中文](./README_zh.md)

A lightweight proxy that converts Anuneko services into a standard OpenAI API format.

## ✨ Features

*   **Full Compatibility**: Supports both streaming and non-streaming OpenAI responses.
*   **Smart Context**: Automatically manages upstream `chat_id` based on conversation history for seamless continuity.
*   **Multi-Model**: Switch between "Orange Cat" and "Exotic Shorthair" via model names.
*   **Access Control**: Secure your proxy with custom API Keys.

## 🚀 Deployment

1. Create a `.env` file:
   ```dotenv
   ANUNEKO_TOKEN=your_upstream_token
   PROXY_API_KEYS=["sk-your-api-key"]
   ```

2. Build and run the container:
   ```bash
   docker build -t anuneko-proxy .
   ```

   ```bash
   docker run -d \
     --name my-anuneko \
     -p 8000:8000 \
     --env-file .env \
     anuneko-proxy
   ```
3. OR run directly:
   ```bash
   python -m app.main

## ⚙️ Configuration

### Environment Variables (.env)
| Variable | Description | Example |
| :--- | :--- | :--- |
| `ANUNEKO_TOKEN` | **Required**. The x-token from Anuneko | `eyJh...` |
| `ANUNEKO_COOKIE` | Optional. Required by some accounts | `session=...` |
| `PROXY_API_KEYS` | List of valid keys for clients | `["sk-123456"]` |

### Client Setup (e.g., NextChat)
*   **Endpoint**: `http://your-server-ip:8000`
*   **API Key**: The value you set in `PROXY_API_KEYS` (e.g., `sk-123456`).
*   **Custom Models**: `orange-cat` (Default), `black-cat` (Exotic Shorthair).

## ⚠️ Disclaimer

This project is for educational and research purposes only.
1. This is a third-party wrapper; no data is stored locally. All requests are forwarded upstream.
2. Do not use this project for commercial or illegal purposes.
3. The developers are not responsible for any account bans or damages resulting from the use of this tool.

## 📄 License

This project is licensed under the [GNU General Public License v3.0 (GPLv3)](./LICENSE).