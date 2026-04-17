CC = clang
CFLAGS = -fPIC -Wall -g
LDFLAGS = -shared

SRC = src/bridge.c src/ops.s
OUT = build/libops.so

all:
	mkdir -p build
	$(CC) $(CFLAGS) $(SRC) $(LDFLAGS) -o $(OUT)

clean:
	rm -rf build/*
