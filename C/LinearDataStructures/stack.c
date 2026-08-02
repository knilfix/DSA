#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Stack
{
    int *arr;

    int size;
    int capacity;
} Stack;

/* CREATION/DELETION */
Stack *create_stack(int capacity);
void destroy_stack(Stack *stack);

/* INSERTION OPERATIONS*/
void push(Stack *stack, int data);

/* DELETION OPERATIONS*/
int pop(Stack *stack);

/* UTILITY FUNCTION */
void resize(Stack *stack);
void print_stack(Stack *stack);

int main()
{
    int stack_capacity = 10;
    Stack *stack = create_stack(stack_capacity);

    for (int i = 1; i <= 22; i++)
    {
        push(stack, i * i);
    }

    print_stack(stack);
    for (int i = stack->size; i > 10; i--)
    {
        int popped = pop(stack);
        printf("Popped %d\n", popped);
    }
    puts("");
    print_stack(stack);
    puts("");
    destroy_stack(stack);
}

Stack *create_stack(int capacity)
{
    // create space for the array
    int *array = malloc(capacity * sizeof(int));
    if (array == NULL)
    {
        puts("Memory Allocation for Array failed!");
        return NULL;
    }

    // create space for the Stack
    Stack *stack = malloc(sizeof(Stack));
    if (stack == NULL)
    {
        puts("Memory Allocation for Stack failed!");
        return NULL;
    }

    stack->arr = array;
    stack->size = 0;
    stack->capacity = capacity;

    // return pointer to stack
    return stack;
}

/* INSERTION OPERATIONS*/
void push(Stack *stack, int data)
{
    if (stack->size == stack->capacity)
    {
        resize(stack);
    }
    stack->arr[stack->size] = data;
    stack->size++;
    return;
}

int pop(Stack *stack)
{
    int data = stack->arr[stack->size - 1];
    stack->size--;
    return data;
}

/* DELETION OPERATIONS*/
void destroy_stack(Stack *stack)
{
    if (stack == NULL) // ← Check FIRST
    {
        puts("Stack is Null ... Operation Aborted");
        return;
    }

    if (stack->arr != NULL)
    {
        free(stack->arr);
    }

    printf("Stack at %p destroyed!\n", (void *)stack);
    free(stack);
}

/* UTILITY FUNCTION */
void resize(Stack *stack)
{
    int new_capacity = stack->capacity * 2;

    // Copy contents to new array
    int *new_array = malloc(new_capacity * sizeof(int));

    for (int i = 0; i < stack->size; i++)
    {
        new_array[i] = stack->arr[i];
    }
    // free old array
    free(stack->arr);

    // change stuct to point to new array
    stack->arr = new_array;
    stack->capacity = new_capacity;
}

void print_stack(Stack *stack)
{
    if (stack == NULL)
    {
        printf("Stack is NULL!\n");
        return;
    }

    printf("Top Element: %d\n", stack->arr[stack->size - 1]);

    printf("Stack (size: %d, capacity: %d): ", stack->size, stack->capacity);

    if (stack->size == 0)
    {
        printf("EMPTY\n");
        return;
    }

    printf("[");
    for (int i = 0; i < stack->size; i++)
    {
        printf("%d", stack->arr[i]);
        if (i < stack->size - 1)
        {
            printf(", ");
        }
    }
    printf("] <- top\n");
}