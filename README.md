# Mediavisor


# Bash Command for running Celery
```bash
cd <flask_venv>/app

celery -A app worker --loglevel=info -E -P threads
```
# Celery CLI args
```
Commands:
  amqp     AMQP Administration Shell.
  beat     Start the beat periodic task scheduler.
  call     Call a task by name.
  control  Workers remote control.
  events   Event-stream utilities.
  graph    The ``celery graph`` command.
  inspect  Inspect the worker at runtime.
  list     Get info from broker.
  logtool  The ``celery logtool`` command.
  migrate  Migrate tasks from one broker to another.
  multi    Start multiple worker instances.
  purge    Erase all messages from all known task queues.
  report   Shows information useful to include in bug-reports.
  result   Print the return value for a given task id.
  shell    Start shell session with convenient access to celery symbols.
  status   Show list of workers that are online.
  upgrade  Perform upgrade between versions.
  worker   Start worker instance.
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
