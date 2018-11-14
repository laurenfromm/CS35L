//
//  main.c
//  hw2
//
//  Created by Lauren Fromm on 4/18/17.
//  Copyright © 2017 Lauren Fromm. All rights reserved.
//

// Consider the folowing assembly code:
// long loop(long x int n)
// x in %rdi, n in %esi
// loop:
//      movl %esi, %ecx
//      movl $1, %edx
//      movl $0, %eax
//      jmp .L2
// .L3:
//      movq %rdi, %r8
//      andq %rdx, %r8
//      orq  %r8, %rax
//      salq %cl, %rdx
// .L2:
//      testq %rdi, %rdx
//      jne   .L3
//      rep;ret

long loop(long x, int n)
{
    long result = 0 ;
    long mask;
    for(mask = 1 ; mask != 0; mask = mask << n)
    {
        result |= (x&mask) ;
    }
    return result;
}
