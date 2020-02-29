#include <stdio.h>

struct BinaryTreeNode
{
    int data;
    struct BinaryTreeNode *left;
    struct BinaryTreeNode *right;
};

typedef struct BinaryTreeNode BinaryTree;

BinaryTree *Insert(BinaryTree *root, int data)
{
    if (root == NULL)
    {
        root = (BinaryTree *)malloc(sizeof(BinaryTree));

        if (root == NULL)
        {
            printf("memory error");
            return;
        }
        else
        {
            root->data = data;
            root->left = root->right = NULL;
        }
    }
    else
    {
        if (data < root->data)
            root->left = Insert(root->left, data);
        else if (data > root->data)
            root->right = Insert(root->right, data);
    }
}

BinaryTree *Create(int data)
{
    BinaryTree *root = (BinaryTree *)malloc(sizeof(BinaryTree));
    root->data = data;
    root->left = NULL;
    root->right = NULL;
    return (root);
}

void preorder(BinaryTree *root)
{
    if (root)
    {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void inorder(BinaryTree *root)
{
    if (root)
    {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

void postorder(BinaryTree *root)
{
    if (root)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}

int main()
{
    BinaryTree *root = Create(1);
    root->left = Create(2);
    root->right = Create(3);
    root->left->left = Create(4);
    root->left->right = Create(5);
    root->right->left = Create(6);
    root->right->right = Create(7);
    /* Insert(root, 10);
    Insert(root, 22\);
    Insert(root, 19);
    Insert(root, 31);
    Insert(root, 67);
    Insert(root, 9);*/

    printf("Preorder traversal of the tree : \n");
    preorder(root);
    printf("\n");
    printf("inorder traversal of the tree : \n");
    inorder(root);
    printf("\n");
    printf("postorder traversal of the tree  : \n ");
    postorder(root);
    printf("\n");
    return 0;
}