#include <stdio.h>
#include <string.h>

void reverseString(char str[]) {
    int n = strlen(str);
    for (int i = 0; i < n / 2; i++) {
        char temp = str[i];
        str[i] = str[n - i - 1];
        str[n - i - 1] = temp;
    }
}

int main() {
    char str[100];

    // Entrada da string
    printf("Digite uma string: ");
    fgets(str, sizeof(str), stdin);

    // Remover o caractere de nova linha, se presente
    str[strcspn(str, "\n")] = '\0';

    // Invertendo a string
    reverseString(str);

    // Exibindo a string invertida
    printf("String invertida: %s\n", str);

    return 0;
}