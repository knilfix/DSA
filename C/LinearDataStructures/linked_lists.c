#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node
{
    struct Node *next;
    int data;
} Node;

typedef struct LinkedList
{
    Node *head;
    Node *tail;
    int size;
} LinkedList;

/* CREATION/DESTRUCTION */
LinkedList *create_list();
void destroy_linked_list(LinkedList *ll);

/* INSERTION OPERATIONS */
void append(LinkedList *ll, int data);
void prepend(LinkedList *ll, int data);
void insert_after(LinkedList *ll, int data, int new_value);

/* DELETION OPERATIONS */
void delete_front(LinkedList *ll);
void delete_end(LinkedList *ll);
void delete_at_value(LinkedList *ll, int value);
void clear_list(LinkedList *ll);

/* ACCESS AND SEARCH */

/* UTILITY FUNCTIONS */
void print_list(LinkedList *ll);
bool is_empty(LinkedList *ll);
void reverse_list(LinkedList *ll);

int main()
{
    puts("============== Linked List =================");

    LinkedList *ll = create_list();
    printf("Size of Linked List struct: %zu bytes\n", sizeof(LinkedList));
    puts("");

    if (ll == NULL)
    {
        return 0;
    }

    for (int i = 1; i < 11; i++)
    {
        append(ll, i * i);
    }

    print_list(ll);

    prepend(ll, 3);
    print_list(ll);

    insert_after(ll, 16, 23);
    print_list(ll);
    puts("");

    puts("Reversing List");
    reverse_list(ll);
    print_list(ll);
    puts("");

    puts("Reversing List");
    reverse_list(ll);
    print_list(ll);
    puts("");

    delete_front(ll);
    print_list(ll);
    puts("");

    delete_end(ll);
    print_list(ll);
    puts("");

    delete_at_value(ll, 25);
    print_list(ll);
    puts("");

    clear_list(ll);
    print_list(ll);
    puts("");

    // Test edge cases
    printf("=== Testing Edge Cases ===\n");

    // Test single element operations
    LinkedList *single = create_list();
    append(single, 999);
    printf("Single element list: ");
    print_list(single);

    delete_front(single); // Should work
    printf("After delete_front: ");
    print_list(single);

    // Test delete non-existent value
    append(ll, 100);
    printf("Before deleting non-existent value: ");
    print_list(ll);
    delete_at_value(ll, 12345); // Should not crash
    printf("After: ");
    print_list(ll);

    destroy_linked_list(ll);
    destroy_linked_list(single);

    // Add this test after your existing tests
    printf("=== Testing Tail Pointer Optimization ===\n");
    LinkedList *test = create_list();

    // Test append with tail
    printf("Appending 3 elements:\n");
    append(test, 100);
    printf("After 1st append - Head: %d, Tail: %d\n", test->head->data, test->tail->data);
    append(test, 200);
    printf("After 2nd append - Head: %d, Tail: %d\n", test->head->data, test->tail->data);
    append(test, 300);
    printf("After 3rd append - Head: %d, Tail: %d\n", test->head->data, test->tail->data);

    // Test delete_end updates tail
    printf("\nTesting delete_end tail update:\n");
    delete_end(test);
    printf("After delete_end - Head: %d, Tail: %d\n", test->head->data, test->tail->data);

    // Test delete_front updates tail
    printf("\nTesting delete_front tail update:\n");
    delete_front(test);
    printf("After delete_front - Head: %d, Tail: %d\n", test->head->data, test->tail->data);

    destroy_linked_list(test);

    return 0;
}

/* CREATION/DESTRUCTION */
LinkedList *create_list()
{
    LinkedList *ll = malloc(sizeof(LinkedList));
    if (ll == NULL)
    {
        puts("Memory Allocation for Linked List failed!");
        return NULL;
    }

    ll->head = NULL;
    ll->tail = NULL;
    ll->size = 0;
    return ll;
}

void destroy_linked_list(LinkedList *ll)
{
    Node *current = ll->head;
    while (current != NULL)
    {
        Node *next = current->next;
        free(current);
        current = next;
    }
    free(ll);
    puts("List Destroyed - Memory freed");
}

/* INSERTION OPERATIONS */

// Adds to end of list
void append(LinkedList *ll, int data)
{

    // If list is empty, create the head
    if (is_empty(ll))
    {
        prepend(ll, data);
        return;
    }
    else
    {
        Node *new_node = malloc(sizeof(Node));
        if (new_node == NULL)
        {
            puts("Memory Allocation Failed!");
            return;
        }

        new_node->data = data;

        ll->tail->next = new_node;
        ll->tail = new_node;
        ll->size++;
    }
}

// Adds to head of list
void prepend(LinkedList *ll, int data)
{
    Node *new_node = malloc(sizeof(Node));
    if (new_node == NULL)
    {
        puts("Memory Allocation Failed!");
        return;
    }

    new_node->data = data;
    new_node->next = ll->head;
    ll->head = new_node;

    if (ll->tail == NULL)
    {
        ll->tail = new_node;
    }
    ll->size++;
}

void insert_after(LinkedList *ll, int target_data, int new_value)
{
    if (is_empty(ll))
    {
        puts("Linked List Empty!");
        return;
    }

    Node *current = ll->head;

    // Traverse to find the target node
    while (current != NULL)
    {
        if (current->data == target_data)
        {
            Node *new_node = malloc(sizeof(Node));
            if (new_node == NULL)
            {
                puts("Memory allocation Failed!");
                return;
            }

            new_node->data = new_value;
            new_node->next = current->next;
            current->next = new_node;
            ll->size++;
            return;
        }
        current = current->next;
    }

    printf("Value %d not found in list!\n", target_data);
}

/* DELETION OPERATIONS*/

void delete_front(LinkedList *ll)
{
    if (is_empty(ll))
    {
        puts("Linked List Empty!");
        return;
    }

    Node *current = ll->head;
    ll->head = current->next;

    // Update tail if this was the only node
    if (current == ll->tail)
    {
        ll->tail = NULL;
    }

    free(current);
    ll->size--;
}

void delete_end(LinkedList *ll)
{
    if (is_empty(ll))
    {
        puts("Linked List Empty!");
        return;
    }

    // Single node case
    if (ll->head->next == NULL)
    {
        free(ll->head);
        ll->head = NULL;
        ll->tail = NULL;
        ll->size--;
        return;
    }

    Node *current = ll->head;

    while (current->next != ll->tail)
    {
        current = current->next;
    }

    // On Node before the tail
    free(ll->tail);
    current->next = NULL;
    ll->tail = current;

    ll->size--;
}

void delete_at_value(LinkedList *ll, int value)
{
    if (is_empty(ll))
    {
        puts("Linked List Empty!");
        return;
    }

    // Special case: head node matches
    if (ll->head->data == value)
    {
        delete_front(ll);
        return;
    }

    Node *current = ll->head;
    Node *prev = NULL;

    while (current != NULL)
    {
        if (current->data == value)
        {
            prev->next = current->next;

            // If we're deleting the tail, update tail pointer
            if (current == ll->tail)
            {
                ll->tail = prev;
            }

            free(current);
            ll->size--;
            return;
        }
        prev = current;
        current = current->next;
    }

    printf("Value %d not found!\n", value);
}

void clear_list(LinkedList *ll)
{
    if (is_empty(ll))
    {
        puts("Linked List Empty!");
        return;
    }
    Node *current = ll->head;

    while (current != NULL)
    {
        Node *next = current->next;
        free(current);
        current = next;
    }
    ll->head = NULL;
    ll->tail = NULL;
    ll->size = 0;
    puts("List successfully cleared");
}

/* UTILITY FUNCTIONS */
void print_list(LinkedList *ll)
{
    if (is_empty(ll))
    {
        printf("💔 List is Empty!"
               "\n");
        return;
    }

    printf("📋 List Size: %d"
           "\n",
           ll->size);
    Node *current = ll->head;
    while (current != NULL)
    {
        printf("%d", current->data);
        if (current->next != NULL)
        {
            printf(" → ");
        }
        current = current->next;
    }
    printf(" ⏹"
           "\n");
}

bool is_empty(LinkedList *ll)
{
    return ll->head == NULL;
}

void reverse_list(LinkedList *ll)
{
    if (is_empty(ll))
    {
        printf("💔 List is Empty!"
               "\n");
        return;
    }

    if (ll->head->next == NULL)
    {
        return;
    }

    Node *next = NULL;
    Node *current = ll->head;
    Node *prev = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    ll->tail = ll->head;
    ll->head = prev;

    printf("✅ List reversed! New head: %d, New tail: %d"
           "\n",
           ll->head->data, ll->tail->data);
}