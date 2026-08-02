#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int *data;
    int size;
    int capacity;
} DynamicArray;

/* Essential Functions Only */
DynamicArray *create_array(int capacity);
void destroy_array(DynamicArray *dyn_arr);
void append(DynamicArray *arr, int data);
int remove_from_index(DynamicArray *arr, int index);
int remove_from_end(DynamicArray *arr);
int get_from_index(DynamicArray *arr, int index);
void set_at_index(DynamicArray *arr, int index, int data);
int get_current_size(DynamicArray *arr);
int get_current_capacity(DynamicArray *arr);
void print_array(DynamicArray *arr);

/* Internal helper */
void resize_array(DynamicArray *arr, int new_capacity);

/* Demo Main */
void demo_dynamic_array()
{
    printf("🚀 DYNAMIC ARRAY DEMONSTRATION\n");
    printf("===============================\n\n");

    // Create array with small capacity to show resizing
    printf("1. Creating array with capacity 2\n");
    DynamicArray *arr = create_array(2);
    printf("   Initial: size=%d, capacity=%d\n", get_current_size(arr), get_current_capacity(arr));

    // Demonstrate appending and auto-resize
    printf("\n2. Appending elements (watch it resize!):\n");
    for (int i = 1; i <= 5; i++)
    {
        append(arr, i * 10);
        printf("   Append %2d -> size=%d, capacity=%d\n",
               i * 10, get_current_size(arr), get_current_capacity(arr));
    }
    printf("   Final array: ");
    print_array(arr);

    // Demonstrate access and modification
    printf("\n3. Access and modify elements:\n");
    printf("   arr[0] = %d\n", get_from_index(arr, 0));
    printf("   arr[2] = %d\n", get_from_index(arr, 2));
    set_at_index(arr, 1, 999);
    printf("   After set_at_index(1, 999): ");
    print_array(arr);

    // Demonstrate removal from end
    printf("\n4. Remove from end:\n");
    int removed = remove_from_end(arr);
    printf("   Removed: %d\n", removed);
    printf("   After removal: ");
    print_array(arr);

    // Demonstrate removal from middle
    printf("\n5. Remove from middle (index 1):\n");
    removed = remove_from_index(arr, 1);
    printf("   Removed: %d\n", removed);
    printf("   After removal: ");
    print_array(arr);
    printf("   Note how elements shifted left!\n");

    // Show final state
    printf("\n6. Final state:\n");
    printf("   Array: ");
    print_array(arr);
    printf("   Size: %d, Capacity: %d\n", get_current_size(arr), get_current_capacity(arr));

    // Cleanup
    destroy_array(arr);
    printf("\n🎉 Demo completed successfully!\n");
}

int main()
{
    demo_dynamic_array();
    return 0;
}

/* IMPLEMENTATION */

DynamicArray *create_array(int capacity)
{
    DynamicArray *arr_ptr = malloc(sizeof(DynamicArray));
    if (arr_ptr == NULL)
        return NULL;

    arr_ptr->data = malloc(capacity * sizeof(int));
    if (arr_ptr->data == NULL)
    {
        free(arr_ptr);
        return NULL;
    }

    arr_ptr->size = 0;
    arr_ptr->capacity = capacity;
    return arr_ptr;
}

void destroy_array(DynamicArray *dyn_arr)
{
    free(dyn_arr->data);
    free(dyn_arr);
}

void append(DynamicArray *arr, int data)
{
    if (arr->size >= arr->capacity)
    {
        int new_capacity = arr->capacity * 2;
        resize_array(arr, new_capacity);
    }
    arr->data[arr->size] = data;
    arr->size++;
}

int remove_from_index(DynamicArray *arr, int index)
{
    if (index < 0 || index >= arr->size)
    {
        printf("Index out of bounds!\n");
        return -1;
    }
    int result = arr->data[index];

    for (int i = index; i < arr->size - 1; i++)
    {
        arr->data[i] = arr->data[i + 1];
    }
    arr->size--;
    return result;
}

int remove_from_end(DynamicArray *arr)
{
    if (arr->size == 0)
    {
        printf("Empty Array!\n");
        return -1;
    }
    arr->size--;
    return arr->data[arr->size];
}

int get_from_index(DynamicArray *arr, int index)
{
    if (index < 0 || index >= arr->size)
    {
        printf("Invalid index!\n");
        return -1;
    }
    return arr->data[index];
}

void set_at_index(DynamicArray *arr, int index, int data)
{
    if (index < 0 || index >= arr->size)
    {
        printf("Index out of bounds!\n");
        return;
    }
    arr->data[index] = data;
}

int get_current_size(DynamicArray *arr)
{
    return arr->size;
}

int get_current_capacity(DynamicArray *arr)
{
    return arr->capacity;
}

void print_array(DynamicArray *arr)
{
    printf("[");
    for (int i = 0; i < arr->size; i++)
    {
        printf(" %d", arr->data[i]);
    }
    printf(" ]\n");
}

void resize_array(DynamicArray *arr, int new_capacity)
{
    int *new_data = malloc(new_capacity * sizeof(int));
    if (new_data == NULL)
    {
        printf("Resize failed!\n");
        return;
    }

    for (int i = 0; i < arr->size; i++)
    {
        new_data[i] = arr->data[i];
    }

    free(arr->data);
    arr->data = new_data;
    arr->capacity = new_capacity;
}