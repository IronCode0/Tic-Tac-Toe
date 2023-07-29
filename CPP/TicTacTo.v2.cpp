#include<iostream>
#include<string>
using namespace std;

string board[10] = {" "};
void display() {
    system("cls");
    cout << "             +-------------+" << endl;
    cout << "             |             |"  << endl;
    cout << "             |    " + board[7] + '|' + board[8] + '|' + board[9] + "    |" << endl;
    cout << "             |    " + board[4] + '|' + board[5] + '|' + board[6] + "    |" << endl;
    cout << "             |    " + board[1] + '|' + board[2] + '|' + board[3] + "    |" << endl;
    cout << "             |             |" << endl;
    cout << "             +-------------+" << endl;
}
char player_input() {
    char marker='A';
    while (marker != 'X' && marker != 'O') {
        try {
            cout << "\nPlayer 1: Do you want to be X or O: ";
            cin >> marker;
        } catch(...) {
            marker='A';
        }
        if(marker == 'x') marker = 'X';
        if(marker == 'o') marker = 'O';
    }
    return marker;
}
void place_marker(char marker,int position) {
    board[position] = marker;
}
bool win_check(char mark) {
    string m(1, mark);
    return( (board[7] == m && board[8] == m && board[9] == m) ||  // across the top
            (board[4] == m && board[5] == m && board[6] == m) ||  // across the middle
            (board[1] == m && board[2] == m && board[3] == m) ||  // across the bottom
            (board[7] == m && board[4] == m && board[1] == m) ||  // down the left 
            (board[8] == m && board[5] == m && board[2] == m) ||  // down the middle
            (board[9] == m && board[6] == m && board[3] == m) ||  // down the right 
            (board[7] == m && board[5] == m && board[3] == m) ||  // 2 diagnols
            (board[9] == m && board[5] == m && board[1] == m) );
}
bool space_check(int position) {
    return (position >= 1 && position <= 9) ? (board[position] == " ") : false;
}
int choose_first() {
    if (rand()%2 == 0) return 1;
    else return 2;
}
bool full_board_check() {
    int empty_space = 0;
    for (int i=1; i<10; i++) {
        if (space_check(i)) empty_space++;
    }
    return (empty_space == 0);
}
int player_choice() {
    int position = 0;
    while (!space_check(position)) {
        try {
            cout << "Please Enter position (1-9): ";
            cin >> position;
        } catch(...) {
            position = 0;
        }
    }
    return position;
}
bool replay() {
    string b;
    cout << "You want to play again (yes , no): ";
    cin >> b;
    if (b[0] == 'Y' || b[0] == 'y') return true;
    else return false;
}
int main() {
    system("mode con:cols=40 lines=12");
    cout << "+------------------------------+" << endl;
    cout << "|         Tic Tac Toe          |" << endl;
    cout << "+------------------------------+" << endl;
    cout << " Positions on board" << endl;
    cout << "                  7|8|9" << endl;
    cout << "                  4|5|6" << endl;
    cout << "                  1|2|3" << endl;
    while (true) {
        for(int i=1; i<10; board[i++]=" ");     // clean board
        char arr = player_input();
        char player1_marker = arr, player2_marker = (arr == 'X') ? 'O' : 'X';
        int turn = choose_first();
        while (true) {
            system("cls");
            if (turn == 1) {
                display();
                cout << "Player 1 turn [ " << player1_marker << " ]" << endl;
                place_marker(player1_marker,player_choice());
                if (win_check(player1_marker)) {
                    display();
                    cout << "Congratulation! \nPlayer 1 '" << player1_marker << "' have won the game" << endl;
                    break;
                } else if (full_board_check()) {
                    display();
                    cout << "the game is a draw!!" << endl;
                    break;
                } else turn = 2;
            } else {
                display();
                cout << "Player 2 turn [ " << player2_marker << " ]" << endl;
                place_marker(player2_marker,player_choice());
                if (win_check(player2_marker)) {
                    display();
                    cout << "Congratulation! \nPlayer 2 '" << player2_marker << "' have won the game" << endl;
                    break;
                } else if (full_board_check()) {
                    display();
                    cout << "the game is a draw!!" << endl;
                    break;
                } else turn = 1;
            }
        }
        if (!replay()) break;
        system("cls");
    }
    return 0;
}
