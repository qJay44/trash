gcc -DSQLITE_ENABLE_RTREE -c sqlite3.c -o sqlite3.o
ar rcs libsqlite3.a sqlite3.o
gcc -DSQLITE_ENABLE_RTREE -c sqlite3.c -o sqlite3.exe