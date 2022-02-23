
gobuild:
	go build -buildmode=c-shared -o libdemo.so shared.go

cbuild:
	gcc main.c -ldemo -o main_from_c

cclean:
	rm ./main_from_c

crun: cbuild
	./main_from_c
