#ifndef CONF_H
#define CONF_H

#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <time.h> 

#include "util.h"
#include "lib/fs/fs.h"

#define MAX_SIZE 0xFFFFF

typedef struct bf_Program bf_Program;

struct bf_Program {
	char *inst;
	char *name;
	char *mem;
	size_t len;
	size_t ic;
	size_t dp;
};

bf_Program *bf_new_program(char *name, size_t len);
void bf_close_program(bf_Program *program);
bf_Program *bf_parse_program(char *name, char *source);
size_t *bf_compute_jumptable(bf_Program *program);
void bf_run_program(bf_Program *program);

#endif
