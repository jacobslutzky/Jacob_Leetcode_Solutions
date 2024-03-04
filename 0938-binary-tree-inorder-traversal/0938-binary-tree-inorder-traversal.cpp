/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<int> result;
        if(root==NULL){
            return result;
        }
        stack<TreeNode*> st;
        st.push(root);
        while(!st.empty()){
            TreeNode *node=st.top();
            while(node!=NULL){
                node=node->left;
                st.push(node);
            }
            node=st.top();
            st.pop();
            result.push_back(node->val);
            st.push(node->right);
        }
        return result;
    }
};