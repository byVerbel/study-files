#include <stdio.h>
#include <stdlib.h>

typedef struct _trie
{
    char university[20];
    struct _trie *paths[10];
} trie;