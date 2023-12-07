#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def remove_multiples(nums, prime):
        for i in range(len(nums)):
            if nums[i] is not None and nums[i] % prime == 0:
                nums[i] = None

    def get_winner(n):
        primes = [num for num in range(2, n + 1) if is_prime(num)]
        nums = [i for i in range(1, n + 1)]
        maria_turn = True

        while True:
            valid_primes = [prime for prime in primes if prime in nums]

            if not valid_primes:
                return "Ben" if maria_turn else "Maria"

            prime = min(valid_primes)
            remove_multiples(nums, prime)
            maria_turn = not maria_turn

    winners = [get_winner(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
