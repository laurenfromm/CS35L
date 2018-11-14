//
//  switch.c
//  hw2
//
//  Created by Lauren Fromm on 4/19/17.
//  Copyright © 2017 Lauren Fromm. All rights reserved.
//

long switch_prob(long x, long n)
{
    long result = x;
    switch(n){
            
        case 60:
        case 62:
            result = 8 * x;
            break;
        case 63:
            
            result >>= 3;
            break;
            
        case 64:
            result <<=4;
            result -= x;
            x = result;
        case 65:
            x = x * x;
        default:
            result = 75 + x;
            
    }
    return result;
}
