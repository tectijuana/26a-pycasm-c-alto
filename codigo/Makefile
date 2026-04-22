all:
	rm -rf build/*
	mkdir -p build
	clang -fPIC -Wall -g src/bridge.c src/ops.s -shared -o build/libops.so

clean:
	rm -rf build/*
