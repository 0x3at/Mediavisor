# Mediavisor


# Bash Command for running Celery
```bash
cd <flask_venv>/app

celery -A app worker --loglevel=info
```

# Bash Commands for Running and Managing Memurai (Redis)

## Starting and Stopping the Memurai Service
```bash
# Starts the Memurai service
memurai --service-start

# Stops the Memurai service
memurai --service-stop

# CLI interface
memurai-cli
```

## Basic Data Operations
```bash
# Inserts a value at the head of the list stored at the key (useful for adding tasks to a queue)
LPUSH [list] [value]

# Inserts a value at the tail of the list stored at the key
RPUSH [list] [value]

# Removes and returns the first element of the list stored at the key
LPOP [list]

# Removes and returns the last element of the list stored at the key
RPOP [list]

# Gets a range of elements from the list stored at the key
LRANGE [list] [start] [stop]

# Gets the length of the list stored at the key
LLEN [list]
```

## Monitoring and Debugging
```bash
# Real-time capture of the commands being executed (useful for debugging)
MONITOR

# Provides information and statistics about the server
INFO

# Finds all keys matching the given pattern
KEYS [pattern]
```