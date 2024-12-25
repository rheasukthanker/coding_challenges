'''Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.'''
'''Here N is the number of accounts and K is the maximum length of an account.

Time complexity: O(NKlogNK)

In the worst case, all the emails will end up belonging to a single person. The total number of emails will be N∗K, and we need to sort these emails. DFS traversal will take NK operations as no email will be traversed more than once.

Space complexity: O(NK)

Building the adjacency list will take O(NK) space. In the end, visited will contain all of the emails hence it will use O(NK) space. Also, the call stack for DFS will use O(NK) space in the worst case.

The space complexity of the sorting algorithm depends on the implementation of each programming language. For instance, in Java, Collections.sort() dumps the specified list into an array this will take O(NK) space then Arrays.sort() for primitives is implemented as a variant of quicksort algorithm whose space complexity is O(logNK). In C++ sort() function provided by STL is a hybrid of Quick Sort, Heap Sort, and Insertion Sort with the worst-case space complexity of O(logNK).'''
from collections import defaultdict

class Solution:
    def __init__(self):
        self.visited = set()
        self.adjacent = defaultdict(list)
        
    def DFS(self, merged_account, email):
        self.visited.add(email)
        merged_account.append(email)
        
        for neighbor in self.adjacent[email]:
            if neighbor not in self.visited:
                self.DFS(merged_account, neighbor)
        
    def accountsMerge(self, account_list):
        # Build the adjacency list
        for account in account_list:
            account_first_email = account[1]
            for j in range(2, len(account)):
                account_email = account[j]
                self.adjacent[account_first_email].append(account_email)
                self.adjacent[account_email].append(account_first_email)
                
        # List to store merged accounts
        merged_accounts = []
        
        # Traverse all accounts to perform DFS and collect components
        for account in account_list:
            account_name = account[0]
            account_first_email = account[1]
            
            if account_first_email not in self.visited:
                merged_account = [account_name]
                self.DFS(merged_account, account_first_email)
                
                # Sort emails and add to merged_accounts
                merged_account[1:] = sorted(merged_account[1:])
                merged_accounts.append(merged_account)
                
        return merged_accounts
