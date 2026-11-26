#!/usr/bin/env bash
# Launcher: AGY Job Hunter & CV Commander (localhost:8080)
set -e
cd "$(dirname "$0")"
PY=".venv/bin/python"
[ -x "$PY" ] || PY="python3"
if lsof -nP -iTCP:8080 -sTCP:LISTEN >/dev/null 2>&1; then
  echo "Server sudah berjalan di http://localhost:8080"
  exit 0
fi
nohup "$PY" server.py > logs/server.log 2>&1 &
echo "Server PID $! -> http://localhost:8080 (log: logs/server.log)"
