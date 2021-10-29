#include <iostream>
#include <vector>
#include <cmath>

int main()
{
  unsigned long long limit = 1ULL << 50;
//   std::cin >> limit;

  // largest prime factor that may appear as a square
  unsigned long long root  = (unsigned long long)sqrt(limit);

  // count number of distinct prime factors
  std::vector<unsigned char> numPrimeFactors(root, 0);
  // does any prime factor occurs multiple times ?
  std::vector<bool> ignore(root, false);
  for (unsigned long long prime = 2; prime < root; prime++)
  {
    // skip if not a prime number
    if (numPrimeFactors[prime] != 0)
      continue;

    // add the prime factor to all multiples
    for (auto j = prime; j < root; j += prime)
      numPrimeFactors[j]++;

    // all multiples have at least one prime factor multiples times, mark as invalid
    auto square = prime * prime;
    for (auto j = square; j < root; j += square)
      ignore[j] = true;
  }

  // count all numbers that are not squarefree
  unsigned long long notSquarefree = 0;
  for (unsigned long long base = 2; base < root; base++)
  {
    // at least one prime factor occurs multiple times ?
    if (ignore[base])
      continue;

    // all multiples are not squarefree
    auto square = base * base;
    auto numMultiples = limit / square;

    // if the number of prime factors is odd, then these multiples are new
    if (numPrimeFactors[base] % 2 == 1)
      notSquarefree += numMultiples;
    else // else: when even number of prime factors, then we have seen these numbers before
      notSquarefree -= numMultiples;
  }

  // display result
  auto result = limit - notSquarefree;
  std::cout << result << std::endl;
  return 0;
}