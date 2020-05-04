class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse(s):
            local, domain = s.split('@')
            local = local.split('+')[0].replace('.', '')
            return f'{local}@{domain}'

        return len(set(map(parse, emails)))
