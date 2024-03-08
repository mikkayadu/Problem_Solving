class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(root):
            if not root:
                return 0
            option1, option2 = 0, 0
            if root.left:
                option1 = dp(root.left.left) + dp(root.left.right)
                
            if root.right :
                option2 = dp(root.right.right) +dp(root.right.left)
                # print("Option2", option2)
            option3 = dp(root.left) + dp(root.right)

            return max(root.val + option1 + option2, option3)
        return dp(root)