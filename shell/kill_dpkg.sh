lsof -ti:1025 /var/lib/dpkg/lock | xargs kill -9
