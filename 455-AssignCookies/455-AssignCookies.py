# Last updated: 1/2/2026, 12:18:04 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort children's greed factors in ascending order
        s.sort()  # Sort cookie sizes in ascending order
        content_children = 0
        cookie_index = 0

        for child_greed in g:
            # Iterate through each child's greed factor
            while cookie_index < len(s):
                # Iterate through available cookies
                if s[cookie_index] >= child_greed:
                    # Found a suitable cookie for the current child
                    content_children += 1
                    cookie_index += 1  # Move to the next cookie
                    break  # Move to the next child
                else:
                    # Current cookie is too small, try the next one
                    cookie_index += 1

        return content_children
