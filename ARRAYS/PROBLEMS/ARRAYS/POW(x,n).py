class Solution:
    def myPow_Brute(self, x: float, n: int) -> float:
        ans = 1
        for i in range(1, abs(n) + 1):
            ans *= x

        return ans if n > 0 else (1 / ans)


    def myPow_Better(self, x: float, n: int) -> float:

        def divide_and_product(low, high, cache, total_n):
            if total_n in cache:
                return cache[total_n]
                
            else:
                prod = 1

                total_n = (high - low) + 1

                mid = low + (high - low) // 2

                prod *= divide_and_product(low, mid, cache, (mid - low) + 1)     
                prod *= divide_and_product(mid + 1, high, cache, (high - mid))

                cache[total_n] = prod
                return cache[total_n]

        cache = {0 : 1.0, 1 : x}

        ans = divide_and_product(1, abs(n), cache, abs(n))

        print(cache)

        return ans if n > 0 else (1 / ans)


    def myPow_Optimal_iterative(self, x: float, n: int) -> float:

        ans = 1
        m = abs(n)

        while m > 0:

            if m % 2 != 0:
                ans *= x

            m = m // 2
            x = x * x
            
        return ans if n > 0 else (1 / ans)



    def myPow_Optimal_recursive(self, x: float, n: int) -> float:

        m = abs(n)

        def pow(x, m):
            if m == 0:
                return 1.0
            elif x == 0:
                return 0.0
            elif m == 1:
                return x
            else:
                ans = 1

                if m % 2 != 0:
                    ans *= x

                ans *= pow(x * x, m // 2)
                return ans


        ans = pow(x, m)
        return ans if n > 0 else 1 / ans



    

S = Solution()
x = 2.0000; n = -5
x = 3.0000; n = 10                 
# x = 2.00; n = -200000000
# x = 0.44528; n = 0
print(S.myPow_Brute(x, n))
print(S.myPow_Better(x, n))
print(S.myPow_Optimal_iterative(x, n))
print(S.myPow_Optimal_recursive(x, n))
print(x ** n)