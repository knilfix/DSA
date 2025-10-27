#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

typedef struct Queue
{
    int head;
    int tail;
    int *arr;

    int capacity;
    int size;
} Queue;

Queue *initialize_queue(int capacity);
void destroy_queue(Queue *q);

// INSERTIONS
void enqueue(Queue *q, int data);
int dequeue(Queue *q);

// UTILITY FUNCS
void print_queue(Queue *q);
bool is_empty(Queue *q);
void print_array(int *arr, int head, int tail, int capacity, int size);

int main()
{
    int queue_capacity = 5; // Smaller capacity to see wraps more clearly
    Queue *q = initialize_queue(queue_capacity);

    printf("=== Initial empty queue ===\n");
    print_queue(q);

    printf("\n=== Filling queue (0-4) ===\n");
    for (int i = 0; i < queue_capacity; i++)
    {
        enqueue(q, i);
    }
    print_queue(q);

    printf("\n=== Dequeue 2 elements ===\n");
    for (int i = 0; i < 2; i++)
    {
        int value = dequeue(q);
        printf("Dequeued: %d\n", value);
    }

    print_queue(q);
    printf("\n=== Enqueue 2 more (showing wrap) ===\n");
    for (int i = 10; i < 12; i++)
    {
        enqueue(q, i);
    }
    print_queue(q);

    printf("\n=== Dequeue 2 more ===\n");
    for (int i = 0; i < 2; i++)
    {
        int value = dequeue(q);
        printf("Dequeued: %d\n", value);
    }
    print_queue(q);

    printf("\n=== Enqueue 2 more (wrap again) ===\n");
    for (int i = 20; i < 22; i++)
    {
        enqueue(q, i);
    }
    print_queue(q);

    destroy_queue(q);
    return 0;
}

Queue *initialize_queue(int capacity)
{

    // Initialize the queue
    Queue *q = malloc(sizeof(Queue));
    if (q == NULL)
    {
        puts("Null queue. Aborting allocation");
        return NULL;
    }

    // Initialize Queue attributes

    q->head = 0;
    q->tail = 0;

    q->capacity = capacity;
    q->size = 0;

    int *arr = malloc(capacity * sizeof(int));
    q->arr = arr;

    return q;
}

void destroy_queue(Queue *q)
{
    if (is_empty(q))
    {
        return;
    }
    free(q->arr);
    free(q);
    puts("Queue  Freed");
}

// Insertions
void enqueue(Queue *q, int data)
{

    if (q->capacity == q->size)
    {
        puts("Queue is full cant enqueue");
        return;
    }

    // Eligible to add to queue
    q->arr[q->tail] = data;
    q->tail = (q->tail + 1) % q->capacity;
    q->size++;
}

int dequeue(Queue *q)
{
    if (is_empty(q))
    {
        puts("Empty queue. Aborting dequeue!");
        return INT_MIN;
    }

    int data = q->arr[q->head];
    q->head = (q->head + 1) % q->capacity;
    q->size--;

    return data;
}

// UTILITY FUNCTIONS
void print_queue(Queue *q)
{
    if (is_empty(q))
    {
        puts("Queue is Empty!");
        return;
    }

    puts("---------------------------------------");
    puts("Queue Data");
    printf("Size: %d\n", q->size);
    printf("Capacity: %d\n", q->capacity);
    printf("Head: %d\n", q->head);
    printf("tail: %d\n", q->tail);
    puts("Elements: ");
    print_array(q->arr, q->head, q->tail, q->capacity, q->size);
}

bool is_empty(Queue *q)
{
    return q->size == 0;
}

void print_array(int *arr, int head, int tail, int capacity, int size)
{
    printf("[");

    if (size == 0)
    {
        // Empty queue - print nothing
    }
    else if (head < tail)
    {
        // Normal case - one contiguous block
        for (int i = head; i < tail; i++)
        {
            printf(" %d", arr[i]);
        }
    }
    else if (head > tail)
    {
        // Wrapped case - two blocks
        for (int i = head; i < capacity; i++)
        {
            printf(" %d", arr[i]);
        }
        for (int i = 0; i < tail; i++)
        {
            printf(" %d", arr[i]);
        }
    }
    else
    { // head == tail
        // Full queue - print entire circular buffer
        for (int i = head; i < capacity; i++)
        {
            printf(" %d", arr[i]);
        }
        for (int i = 0; i < tail; i++)
        {
            printf(" %d", arr[i]);
        }
    }

    printf(" ]\n");
}
