#!/bin/sh

case "$1" in
  "web")
    uvicorn src.app:app --reload --host 0.0.0.0 --port 80
    ;;
  *)
    echo "Unknown service: $1"
    ;;
esac