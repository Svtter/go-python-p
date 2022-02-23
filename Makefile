
gobuild:
	go build -buildmode=c-shared -o libdemo.so shared.go

cbuild:
	gcc main.c -ldemo -o main_from_c

clean:
	rm libdemo.h libdemo.so

cclean:
	rm ./main_from_c

crun: cbuild
	./main_from_c
