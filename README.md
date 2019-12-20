# How to memory leak

* `docker-compose build && docker-compose up`
* Open url http://127.0.0.1:8000/gc/
* update it and see Instana objects will append, but not deleting from memory
