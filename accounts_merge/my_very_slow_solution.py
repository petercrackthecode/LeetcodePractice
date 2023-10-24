from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

        Have a dictionary called get_people_email_with_same_name:
        - key: str: the name of the person.
        - value: List[Set[str]]: A list of sets of emails, each set represents one distinct person (can have same name)

        - Iterate through accounts. Each time we iterate through an account, get the person name and their list of emails:
        - Find if there exist a person with the given name in the get_people_email_with_same_name:
            - No: Initialize the key, and add emails to the said key in the get_people_email_with_same_name immediately
            - Yes: people_with_given_name = get_people_email_with_same_name[name]
              Iterate through people_with_given_name (it's a list of sets) and see if we find any set that has at least 1 string in emails. If we find one, stop the iteration immediately. combine the sets of emails, then adjust to the list of sets with the said key correspondingly.

            for account in accounts:
                name = account[0]
                emails = set(account[1:])
                if name not in get_people_email_with_same_name:
                    get_people_email_with_same_name[name] = [emails]
                else:
                    people_with_given_name = get_people_email_with_same_name[name]
                    has_existing_person = False
                    for person_emails in people_with_given_name:
                        common_emails = person_emails.intersection(emails)
                        if len(common_emails) > 0:
                            person_emails = person_email.union(emails)
                            has_existing_person = True
                            break
                    if not has_existing_person:
                        people_with_given_name.append(emails)

            ans = []
            for (name, sets_of_emails) in get_people_email_with_same_name:
                one_person = [name] + sorted(sets_of_emails)
                ans.append(one_person)

            return ans

        - Every time we add a set of emails at a certain name, there will be from 0 to many sets of emails
        overlapped with that added set of email.
        - It's helpful to have a list of unique emails under a given name, so that we can iterate through a 
        new added set of emails and see if all the emails in them are unique.

        accounts = [
        0  ["David","David0@m.co","David1@m.co"],
        1  ["David","David3@m.co","David4@m.co"],
        2  ["David","David4@m.co","David5@m.co"],
        3  ["David","David2@m.co","David3@m.co"],
        4  ["David","David1@m.co","David2@m.co"]
        ]

        new_accounts = [
          0 ["David","David0@m.co","David1@m.co"],
          1 ["David","David3@m.co","David4@m.co", "David5@m.co", "David2@m.co"],
        ]

        ["David","David1@m.co","David2@m.co"]

        expected = [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]

        have a dictionary called account_idx_lookup_by_name_email where:
        - key: a tuple (name: str, email: str)
        - value: index: int- the index within the list people_with_given_name[name] that contains email 
        (in other words, email in people_with_given_name[name][index])
        """
        ans = []
        get_people_email_with_same_name = dict()
        account_idx_lookup_by_name_email = dict()

        for account in accounts:
            name = account[0]
            emails = set(account[1:])
            if name not in get_people_email_with_same_name:
                get_people_email_with_same_name[name] = [emails]
                for email in emails:
                    name_email = (name, email)
                    account_idx_lookup_by_name_email[name_email] = 0
            else:  # name in get_people_email_with_same_name
                people_with_given_name = get_people_email_with_same_name[name]
                new_emails_list = set()
                merged_emails_indices = set()
                for email in emails:
                    name_email = (name, email)
                    if name_email not in account_idx_lookup_by_name_email:
                        new_emails_list.add(email)
                    else:  # name_email in account_idx_lookup_by_name_email
                        idx = account_idx_lookup_by_name_email[name_email]
                        same_person_remaining_emails = people_with_given_name[idx]
                        new_emails_list = new_emails_list.union(
                            same_person_remaining_emails)
                        merged_emails_indices.add(idx)

                new_list_of_emails_group = [emails for (idx, emails) in enumerate(
                    people_with_given_name) if idx not in merged_emails_indices]
                new_list_of_emails_group.append(new_emails_list)
                for idx, emails in enumerate(new_list_of_emails_group):
                    for email in emails:
                        account_idx_lookup_by_name_email[(name, email)] = idx
                get_people_email_with_same_name[name] = new_list_of_emails_group

            # print('get_people_email_with_same_name = ',
            #       get_people_email_with_same_name)
            # print('account = ', account)
            # print(
            #     f'account_idx_lookup_by_name_email = ', account_idx_lookup_by_name_email)
            # print(
            #     '_________________________________________________________________________________')

        for (name, sets_of_emails) in get_people_email_with_same_name.items():
            for person_emails in sets_of_emails:
                one_person = [name] + sorted(person_emails)
                ans.append(one_person)

        return ans


accounts = [["Hanzo", "Hanzo2@m.co", "Hanzo3@m.co"], ["Hanzo", "Hanzo4@m.co", "Hanzo5@m.co"], ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo4@m.co"],
            ["Hanzo", "Hanzo7@m.co", "Hanzo8@m.co"], ["Hanzo", "Hanzo1@m.co", "Hanzo2@m.co"], ["Hanzo", "Hanzo6@m.co", "Hanzo7@m.co"], ["Hanzo", "Hanzo5@m.co", "Hanzo6@m.co"]]
ans = Solution().accountsMerge(accounts)
print('ans = ', ans)
