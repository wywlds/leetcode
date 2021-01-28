class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []
        prime_states = [True] * n
        for i in range(2, n):
            if prime_states[i]:
                primes.append(i)
            for prime in primes:
                if i * prime >= n:
                    break
                prime_states[i * prime] = False
                if i % prime == 0:
                    break
        return len(primes)


if __name__=="__main__":
    solution = Solution()
    print(solution.countPrimes(10))