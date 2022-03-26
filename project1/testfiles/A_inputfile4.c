/*
* My program
*/
{
    int x = 1;
    while (x < 10) {
        int result = x * 2;
        if ( x > 5) {
            result = result * x;
        }
        printf(result); //show the result
        x = x + 1;
    }
}

