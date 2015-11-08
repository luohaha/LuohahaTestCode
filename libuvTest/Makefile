TARGET=app
CC=gcc
UFLAGS="/usr/local/lib/libuv.a -framework CoreFoundation -framework CoreServices"
OBJS = uv_main.o
SOUR = uv_main.c

$(TARGET):uv_main.o
	$(CC) uv_main.o -o $(TARGET) $(UFLAGS)
uv_main.o :
	$(CC) -c uv_main.c
clean :
	rm -f *.o $(TARGET) *~
