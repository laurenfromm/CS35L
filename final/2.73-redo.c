#include <stdio.h> 

int saturating_add(int x, int y){
  int sum = x + y;
  int size = (sizeof(int) << 3) -1;
  int of = (__builtin_add_overflow(x,y, &sum) - 1);
  int max_min = ~((1 << size) ^ (sum >> size));
  int finalSol = (~of & sum) + (of & max_min);
  return finalSol;

}


