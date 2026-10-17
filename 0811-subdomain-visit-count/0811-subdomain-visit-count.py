class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        count = {}

        for cpdomain in cpdomains:
            visits, domain = cpdomain.split()
            visits = int(visits)
            parts = domain.split(".")
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                count[subdomain] = count.get(subdomain, 0) + visits    #counting visits

        return [f"{visits} {domain}" for domain, visits in count.items()]
        