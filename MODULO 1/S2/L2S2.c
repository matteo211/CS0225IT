#include <stdio.h>

// la scelta di dividere i due esercizi in due funzioni distinte e' stata presa per aumentare la leggibilita'.

void esercizio_moltiplicazione(){
    short int num1, num2;

    printf("inserisci 2 numeri da moltiplicare separati da spazio (n1 n2) > ");
    scanf("%hi %hi", &num1, &num2);

    printf("la tua moltiplciazione e': %hi x %hi = %hi", num1, num2, num1 * num2);
}

void esercizio_media_aritmetica(){
    short int somma = 0;
    short int num;
    short int quantity; // why just 2 numbers? :)

    printf("indica la quantita' di numeri di cui calcolare la media > ");
    scanf("%hi", &quantity);

    for(short i = 0; i < quantity; i++){
        printf("inserisci la cifra n.%hi > ", i + 1);
        scanf("%hi", &num);
        somma += num;
    }

    printf("la media aritmetica dei tuoi numeri e': %hi / %hi = %f", somma, quantity, (float) somma / quantity);

}

int main(){
    esercizio_moltiplicazione();
    printf("\n\n");
    esercizio_media_aritmetica();
}