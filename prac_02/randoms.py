"""
Line 1:
I saw a single, positive integer
The smallest number I could have seen was 5, and the largest number I could have seen was 19

Line 2:
I saw a single, positive, odd integer
The smallest number I could have seen was 3, and the largest number I could have seen was 9
No, line 2 could not have produced a 4 as it is increasing from 3 by 2, meaning only odd numbers can be produced

Line 3: I saw a single, positive floating-point number The smallest number I could have seen was 2.5000000000000000,
and the largest number I could have seen was \n 5.4999999999999999 """

import random
print(random.randint(1, 101))
