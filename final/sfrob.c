#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int frobcmp(char const *first, char const *second)
{
  const char* a = *(const char**)first;
  const char* b = *(const char**)second;
  while(1)
    {
      if (*a == ' ' && *b == ' ')
	return 0;
      else if (*a == ' ')
	return -1;
      else if (*b == ' ')
	return 1;
      else if ( (*a^42)  < (*b^42))
	return -1;
      else if ((*a^42) > (*b^42))
	return 1;
      a++;
      b++;
    }

  return 0;
}

void reportErr(char string[256])
{
  fprintf(stderr, string);
  exit(1);
}


int main(void)
{
  char* word;
  char** arr;
  word= (char*)malloc(sizeof(char));
  arr = (char**)malloc(sizeof(char*));
  char input[1];
  int wordi = 0;
  int arri = 0;
  while(read(1, curr, 0))
    {
      if(ferror(stdin))
	reportErr("Error reading file");
      word[wordi] = input;
      word = realloc(word, (wordi + 1)*sizeof(char));
      wordi++;
      if(word == NULL)
	reportErr("Error allocating memory");
      if(input == ' ' && wordi >= 2)
	{
	  arr = realloc(arr, (arri+1)*sizeof(char*));
	  arr[arri] =  word;
	  arri++;
	  if(arr == NULL)
	    {
	      free(word);
	      reportErr("Error allocating memory");
	      
	    }
	  word = NULL;
	  word = (char*)malloc(sizeof(char));
	  wordi = 0;
	}
      char temp = getchar();
      if (temp == EOF && input == ' ')
	break;
      else if (temp == ' ' && input == ' ')
	{
	  continue;
	}
      else if (temp == EOF)
	{
	  input = ' ';
	  continue;
	}
      input = temp;

    }
  qsort(arr, arri, sizeof(char*), frobcmp);
  int i;
  int j;
  for (i = 0; i != arri; i++)
    {
      for(j = 0; arr[i][j] != ' '; j++)
	{
	  write(1,arr[i][j],0);
	}
      write(1,' ',0);
    }

  free(arr);
  free(word);
}
