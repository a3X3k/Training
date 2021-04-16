#include<iostream>

using namespace std;

struct Node
{
    int data;
    Node* next;
    int flag;
};

void push(struct Node** head,int data)
{
    struct Node* new_node = new Node;
    new_node->data = data;
    new_node->next = *head;
    new_node->flag = 0;
    *head = new_node;
}

void find(struct Node* head)
{
    while(head != NULL)
    {
        if(head->flag == 1)
        {
            cout<<"There is a Loop in the Linked List.";
            break;
        }
        head->flag = 1;
        head = head->next;
    }
    if(head==NULL)
    {
        cout<<"No Loop is found in the Linked List.";
    }
}

int main()
{
    struct Node* head;
    push(&head,10);
    push(&head,20);
    push(&head,30);
    push(&head,40);
    
    find(head);
}