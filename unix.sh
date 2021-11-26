#!/usr/bin/env bash
python "ChatCollector.py" &
python "TelegramBot.py" &
python "orderCount.py" &
