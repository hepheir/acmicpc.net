// 15707번: exceed or not

#include <cstdio>
#include <cstring>

#define MAX_STRING_LENGTH (64)
#define MAX_BIGINT_SIZE (128)

using namespace std;
typedef unsigned char *bigint;

unsigned int bigint_size(const bigint x);
void bigint_mul(const bigint a, const bigint b, bigint dst);
bool bigint_leq(const bigint a, const bigint b);
void bigint_parse(const char *src, bigint dst);
void bigint_to_string(const bigint src, char *dst);

char a_str[MAX_STRING_LENGTH];
char b_str[MAX_STRING_LENGTH];
char r_str[MAX_STRING_LENGTH];
char result_str[MAX_STRING_LENGTH];

unsigned char a_bigint[MAX_BIGINT_SIZE];
unsigned char b_bigint[MAX_BIGINT_SIZE];
unsigned char r_bigint[MAX_BIGINT_SIZE];
unsigned char result_bigint[MAX_BIGINT_SIZE];

int main()
{
    scanf("%s %s %s", a_str, b_str, r_str);

    bigint_parse(a_str, a_bigint);
    bigint_parse(b_str, b_bigint);
    bigint_parse(r_str, r_bigint);

    bigint_mul(a_bigint, b_bigint, result_bigint);

    if (!bigint_leq(result_bigint, r_bigint))
    {
        printf("overflow\n");
        return 0;
    }

    bigint_to_string(result_bigint, result_str);
    printf("%s\n", result_str);

    return 0;
}

unsigned int bigint_size(const bigint x)
{
    unsigned int i = MAX_BIGINT_SIZE - 1;
    while (i > 0 && x[i] == 0)
        i--;
    return i + 1;
}

void bigint_mul(const bigint a, const bigint b, bigint dst)
{
    memset(dst, 0, MAX_BIGINT_SIZE);
    unsigned int a_size = bigint_size(a);
    unsigned int b_size = bigint_size(b);

    for (unsigned int i = 0; i < a_size; i++)
    {
        for (unsigned int j = 0; j < b_size; j++)
        {
            unsigned int k = i + j;
            dst[k] += a[i] * b[j];
            while (dst[k] >= 10 && k < MAX_BIGINT_SIZE - 1)
            {
                dst[k + 1] += dst[k] / 10;
                dst[k] %= 10;
                k++;
            }
        }
    }

    // lazy carry handling
    for (unsigned int i = 0; i < MAX_BIGINT_SIZE - 1; i++)
    {
        dst[i + 1] += dst[i] / 10;
        dst[i] %= 10;
    }
}

bool bigint_leq(const bigint a, const bigint b)
{
    unsigned int a_size = bigint_size(a);
    unsigned int b_size = bigint_size(b);

    if (a_size < b_size)
        return true;
    if (a_size > b_size)
        return false;

    for (int i = a_size - 1; i >= 0; i--)
    {
        if (a[i] < b[i])
            return true;
        if (a[i] > b[i])
            return false;
    }
    return true;
}

void bigint_parse(const char *src, bigint dst)
{
    unsigned int src_len = strlen(src);
    memset(dst, 0, MAX_BIGINT_SIZE);
    for (unsigned int i = 0; i < src_len; i++)
    {
        dst[i] = src[src_len - 1 - i] - '0';
    }
}

void bigint_to_string(const bigint src, char *dst)
{
    unsigned int src_size = bigint_size(src);
    for (unsigned int i = 0; i < src_size; i++)
    {
        dst[i] = src[src_size - 1 - i] + '0';
    }
    dst[src_size] = '\0';
}
