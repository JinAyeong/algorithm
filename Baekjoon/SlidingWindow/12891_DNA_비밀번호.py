class DnaPasswordChecker:
    def __init__(self, S, P, dna, required_counts):
        self.S = S
        self.P = P
        self.dna = dna
        self.required = {
            'A': required_counts[0],
            'C': required_counts[1],
            'G': required_counts[2],
            'T': required_counts[3]
        }
        self.current_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        self.result = 0

    def is_valid(self):
        for nucleotide in 'ACGT':
            if self.current_count[nucleotide] < self.required[nucleotide]:
                return False
        return True

    def add(self, char):
        self.current_count[char] += 1

    def remove(self, char):
        self.current_count[char] -= 1

    def check_passwords(self):
        for i in range(self.S):
            self.add(self.dna[i])
            if i >= self.P:
                self.remove(self.dna[i - self.P])
            if i >= self.P - 1 and self.is_valid():
                self.result += 1
        return self.result


def main():
    S, P = map(int, input().split())
    dna = input()
    required_counts = list(map(int, input().split()))

    checker = DnaPasswordChecker(S, P, dna, required_counts)
    result = checker.check_passwords()
    print(result)


if __name__ == "__main__":
    main()