#!/bin/bash

uvicorn --ssl-version 5 --timeout-keep-alive 300 --host 0.0.0.0 --port 3001 api:app