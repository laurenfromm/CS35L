#include <stdio.h>
int saturating_add(int x, int y)
{
  int sum = x + y; //find the sum
  int size = (sizeof(int) << 3) - 1; //create a size int to use the masks
  int mask = (~(x^y) & (y^sum) & (x^sum) >> size); // use a mask to check if the variables have the same signs as the sum

  int limits = (1 << size) ^ (sum >> size); // create a variable to check if th e limits were reached

  int finalSol = (~mask & sum) + (mask & limits);
  return finalSol;//return the final results
 }
